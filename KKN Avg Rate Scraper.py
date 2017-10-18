import urllib
import urllib.request
from bs4 import BeautifulSoup

avg_rates = []
average_rates = []
number_of_listings = 0

theurl = 'https://www.homeaway.com/results/keywords:Kihei+Kai+Nani+%28Kihei%2C+HI%2C+USA%29'

thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, 'html.parser')

print(soup.title.text)

# print(soup.find('div', {'class': 'rate'}).find('a').text)

for rates in soup.findAll('div', {'class': 'rate'}):
    avg_rates.append(rates.find('a').text)

for items in avg_rates:
    number_of_listings += 1
    print(items)

print('Total Number of Listings = {}'.format(number_of_listings))


def remove_dollar_signs(rates_lst):
    for rate in rates_lst:
        average_rates.append(rate.strip('$'))


def calculate_average_rates(avg_rate_lst):
    rate_sum = 0
    for amounts in avg_rate_lst:
        rate_sum += int(amounts)

    avg_nightly_rate = int(rate_sum) / len(avg_rate_lst)
    print('Total Sum of Avg Rates = ${}'.format(rate_sum))
    print('Average Nightly Rate = ${}'.format(avg_nightly_rate))


remove_dollar_signs(avg_rates)
calculate_average_rates(average_rates)
