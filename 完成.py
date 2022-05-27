import json
import requests
from bs4 import BeautifulSoup
import openpyxl
import time

def main():
    file=open('info.json','r')
    info = json.load(file) #jsonを書く際シングルクォーテーションではなくダブルクォーテーションにする
    import sys
    sys.path.append('/opt/anaconda3/lib/python3.9/site-packages')
    from linebot import LineBotApi
    from linebot.models import TextSendMessage
    CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
    from linebot import LineBotApi
    from linebot.models import TextSendMessage
    CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text=url)
    line_bot_api.push_message(USER_ID,messages=messages)

info = {'https://www.amazon.co.jp/Python-1%E5%B9%B4%E7%94%9F-%E4%BD%93%E9%A8%93%E3%81%97%E3%81%A6%E3%82%8F%E3%81%8B%E3%82%8B%EF%BC%81%E4%BC%9A%E8%A9%B1%E3%81%A7%E3%81%BE%E3%81%AA%E3%81%B9%E3%82%8B%EF%BC%81%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%81%AE%E3%81%97%E3%81%8F%E3%81%BF-%E6%A3%AE-%E5%B7%A7%E5%B0%9A-ebook/dp/B076DDBBK9/ref=sr_1_1?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=S1VVTJMOR2WB&keywords=Python+%E5%85%A5%E9%96%80&qid=1652603343&sprefix=python+%E5%85%A5%E9%96%80%2Cspecialty-aps%2C263&sr=8-1'
     :1000, 
     'https://www.amazon.co.jp/Python-%E3%82%BC%E3%83%AD%E3%81%8B%E3%82%89%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0-%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E5%AD%A6%E7%BF%92%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E4%B8%89%E8%B0%B7-%E7%B4%94/dp/4798169463/ref=sr_1_10?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=1S3J01PWHNB1M&keywords=Python&qid=1652603404&sprefix=python+%2Cspecialty-aps%2C203&sr=8-10'
     :2000, 
     'https://www.amazon.co.jp/Python-Flask%E3%81%AB%E3%82%88%E3%82%8BWeb%E3%82%A2%E3%83%97%E3%83%AA%E9%96%8B%E7%99%BA%E5%85%A5%E9%96%80-%E7%89%A9%E4%BD%93%E6%A4%9C%E7%9F%A5%E3%82%A2%E3%83%97%E3%83%AA-%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92API%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9-%E4%BD%90%E8%97%A4-ebook/dp/B09MQ5XHG5/ref=sr_1_9?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=1S3J01PWHNB1M&keywords=Python&qid=1652603404&sprefix=python+%2Cspecialty-aps%2C203&sr=8-9'
     :10000,
     'https://www.amazon.co.jp/Python%E3%81%A7%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92-%E2%80%95scikit-learn%E3%81%A7%E5%AD%A6%E3%81%B6%E7%89%B9%E5%BE%B4%E9%87%8F%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%A8%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AE%E5%9F%BA%E7%A4%8E-Andreas-C-Muller/dp/4873117984/ref=sr_1_6?crid=1FW9EQM7V25WJ&keywords=python+%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92&qid=1652430375&sprefix=python+kikaigakushuu%2Caps%2C311&sr=8-6'
     :5000}

values = [1000,2000,10000,5000]

prices=[]

def change():
    for url in info.keys():
        amazonPage = requests.get(url)
        soup = BeautifulSoup(amazonPage.text, "html.parser")
        price = soup.find('span', attrs={'class':'a-size-base a-color-price a-color-price'})
        while price is None:
            amazonPage = requests.get(url)
            soup = BeautifulSoup(amazonPage.text, "html.parser")
            price = soup.find('span', attrs={'class':'a-size-base a-color-price a-color-price'})
            #price = price.text.replace(',',"")
            if price is not None:
                price = price.text
                price = price.replace(',',"")
                price = price.replace('￥',"")
                price = int(price)
                prices.append(price)
change()
for price1, value,url in zip(prices, values,info.keys()):
    if price1 <= value:
        if __name__ =="__main__":
            main()
    else:
        print(price1, value)

    
   