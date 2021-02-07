from datetime import timedelta, date

from db import Session
from models import Stock, StockPrice


def populate():
  session = Session()

  apple = Stock('AAPL', 'Apple')
  apple_today     = StockPrice(apple, date.today(), 100, 150, 70, 180, 5000.)
  apple_yesterday = StockPrice(apple, date.today() - timedelta(days=1), 50, 90, 40, 100, 2000.)

  session.add(apple)
  session.add(apple_today)
  session.add(apple_yesterday)

  session.commit()
  session.close()


if __name__ == '__main__':
  print("Start populating database")
  populate()
