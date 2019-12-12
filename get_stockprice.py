"""
コマンドプロンプトから入力を受け取り、
コード値から、会社名と、株価を取得する。
"""

from urllib import request
import re
from bs4 import BeautifulSoup

try:
    security_code = int(input('銘柄コードを入力してください。:'))
except ValueError as e:
    print('銘柄コードが間違っています。')
    exit()

stock_page = request.urlopen('https://minkabu.jp/stock/'+ str(security_code))
soup = BeautifulSoup(stock_page,'html.parser')
company_name = soup.find('div',id = 'stock-for-securities-company')['data-short-name']
stock_price=soup.find('div',id = 'stock-for-securities-company')['data-price']
print('社名: '+ company_name)
print('株価: '+ stock_price)
