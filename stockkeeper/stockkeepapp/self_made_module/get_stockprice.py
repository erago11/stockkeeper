"""
引数のコード値から、会社名と、株価を取得する。

Parameters
-----
security_code:int
    銘柄コード。

Returns
-----
context: dictionary
    会社名と、株価を持った辞書型返値。
"""

from urllib import request
import re
from bs4 import BeautifulSoup

def getstockprice(stock_code):
    stock_page = request.urlopen('https://minkabu.jp/stock/'+ str(stock_code))
    soup = BeautifulSoup(stock_page,'html.parser')
    company_name = soup.find('div',id = 'stock-for-securities-company')['data-short-name']
    stock_price=soup.find('div',id = 'stock-for-securities-company')['data-price']
    content ={
              'stock_code':stock_code,
              'company_name':company_name,
              'stock_price':stock_price
    }
    return content
