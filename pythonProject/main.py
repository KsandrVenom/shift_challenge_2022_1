import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import unittest
import test


class TestStringMethods(unittest.TestCase):
    def test_negative_connection(self):
        message = 'Status code is not equal 200 — problem in loading site'
        self.assertEqual(r.status_code, 200, message)


URL_TEPMPLATE = "https://zakupki.gov.ru/epz/order/extendedsearch/results.html"
r = requests.get(URL_TEPMPLATE)


soup = bs(r.text, "html.parser")
purchases_cards = soup.find_all("div", class_="search-registry-entry-block box-shadow-search-input")
result_list = {'number': [], 'cost': []}

for purchase in purchases_cards:
    purchase_number = purchase.find('div', 'registry-entry__header-mid__number').text
    purchase_cost = purchase.find('div', 'price-block__value').text

    result_list['number'].append(purchase_number)
    result_list['cost'].append(purchase_cost)

print(result_list)

df = pd.DataFrame(result_list)
df.to_csv('xxx1')

if __name__ == '__main__':
    unittest.main()

