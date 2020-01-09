"""
引数のコード値から、会社名と、株価を取得する。
返値のkeyのremarks,dateが空欄。
remarksはユーザに入力してもらう。
dateはmodels側で現在時間をdefaultで入力。

Parameters
-----
security_code:int
    銘柄コード。

Returns
-----
context: dictionary
    models.py stockと同じ枠を持った辞書型返値。
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
              'stock_price':stock_price,
              'remarks':'',
              'date':''
    }
    return content

"""
引数の辞書型に入っている銘柄すべての、現在の株価を取得する。
返値の辞書にはすべての銘柄に現在の株価を追記したものを返す。

Parameters
-----
context:dictionary


Returns
-----
context: dictionary
    引数と同じ型
"""

def get_now_stockprice(context):
    for company_info in context['stock_list']:
        stock_page = request.urlopen('https://minkabu.jp/stock/'+ str(company_info.code))
        soup = BeautifulSoup(stock_page,'html.parser')
        company_info.now_price = soup.find('div',id = 'stock-for-securities-company')['data-price']
    return context
