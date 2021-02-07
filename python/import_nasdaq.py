import sys

from db import Session
from models import Stock


def test_query():
  session = Session()

  stocks = session.query(Stock).all()
  print(stocks)
  for s in stocks:
    prices = s.prices
    for p in prices:
      print(p.date)
      print(p.close_price)


if __name__ == '__main__':
  ticker, full_name, data_dir = sys.args[2:]

  print("import")
  test_query()
