import requests as  r
from bs4 import BeautifulSoup

# Using Google Finance URL
# https://www.google.com/finance/quote/MSFT:NASDAQ

# Get foreign exchange to US dollars
def get_fx_to_usd(currency):
    fx_url = f"https://www.google.com/finance/quote/{currency}-USD"
    resp = r.get(fx_url)
    soup = BeautifulSoup(resp.content, "html.parser")

    fx_rate = soup.find("div", attrs={"data-last-price": True})
    fx = float(fx_rate["data-last-price"])
    return fx

def get_price_information(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    resp = r.get(url)

    # Parse the HTML using BS4
    # There are some different parsers available HTML is default but should be specified
    soup = BeautifulSoup(resp.content, "html.parser")

    # There are multiple ways to search for attributes such as CSS, another is to set the value as true
    price_div = soup.find("div", attrs={"data-last-price": True})
    price = float(price_div["data-last-price"])
    currency = price_div["data-currency-code"]

    usd_price = price

    return {
        "ticker": ticker,
        "exchange": exchange,
        "price": price,
        "currency": currency,
        "usd_price": usd_price
    }

if __name__ == "__main__":
    print(get_price_information("MSFT", "NASDAQ").prettify())
