import requests
import math
from newsapi import NewsApiClient


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

ALPendpoint = 'https://www.alphavantage.co/query'
apikey = "******************"
params_tsla = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "0BTF6NKKP0N0TNBM"
}

data = requests.get(ALPendpoint, params=params_tsla)
all_data = data.json()
list_keys =[]
[list_keys.append(k) for k in all_data["Time Series (Daily)"].keys()]


today_numbers = float(all_data["Time Series (Daily)"][list_keys[0]]['4. close'])
yesterday_numbers = float(all_data["Time Series (Daily)"][list_keys[1]]['4. close'])

is_News = False
result = abs((((today_numbers-yesterday_numbers)/yesterday_numbers)*100))

if result >= 1:
    is_News = True


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
newsapi = NewsApiClient(api_key='8*************')

def news():
    top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME,
                                              category='business',
                                              language='en',
                                             country='us')
    data = top_headlines["articles"][:3]

    dict_news = {}

    for d in data:

        dict_news["Title"] = d["title"]
        dict_news["Summary"] = d['description']
        dict_news["Author"] = d['author']

    # data ={
    #     Title: top_headlines["articles"][0] ,
    #     summary:top_headlines ,
    #     author: top_headlines ,
    # }

    return dict_news


if is_News:
    news = news()
    for k,v in news.items():
        print(f"{k}: {v}\n")



