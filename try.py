
import requests
from bs4 import BeautifulSoup
url = 'https://apexlegendsstatus.com/'
responce = requests.get(url).text
parser = BeautifulSoup(responce, 'html.parser')
status = parser.find('div',{'class': 'col-xs-3 up'})
ping = parser.find('div',{'class': 'col-xs-2'})
print()
