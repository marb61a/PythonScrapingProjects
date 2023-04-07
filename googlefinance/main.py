import requests as  r
from bs4 import BeautifulSoup

# Using Google Finance URL
# https://www.google.com/finance/quote/MSFT:NASDAQ

def get_price_information(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    resp = r.get(url)

    # Parse the HTML using BS4
    # There are some different parsers available HTML is default but should be specified
    soup = BeautifulSoup(resp.content, "html.parser")

    # There are multiple ways to search for attributes such as CSS, another is to set the value as true
    price_div = soup.find("div", attrs={"data-last-price": True})
    return price_div

if __name__ == "__main__":
    print(get_price_information("MSFT", "NASDAQ"))
