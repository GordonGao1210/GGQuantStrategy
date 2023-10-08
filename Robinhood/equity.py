import bs4 as bs
import os
import requests
import yfinance as yf


from utils import *

FILE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(FILE_PATH, "data")


def get_sp500_stock_ticker() -> list:
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    industry = {}
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker.replace('\n', ''))
        industry[tickers[-1]] = row.findAll('td')[3].text.replace('\n', '')
    return tickers


def find_high_corr_pair(ticker: list, start_date: str, end_date: str):
    stock_price = download_data(ticker, start_date, end_date)['Close']
    stock_price = stock_price.dropna(axis=1)
    
    with open(os.path.join(DATA_PATH, "stock_price.csv"), "wb") as fp:
        stock_price.to_csv(fp)

    stock_return = convert_price_to_return(stock_price)
    stock_corr = stock_return.corr()

    with open(os.path.join(DATA_PATH, "stock_corr.csv"), "wb") as fp:
        stock_corr.to_csv(fp)



def main():
    ticker = get_sp500_stock_ticker()
    find_high_corr_pair(ticker, "2023-01-01", "2023-08-31")
    
    print()


if __name__ == "__main__":
    main()

