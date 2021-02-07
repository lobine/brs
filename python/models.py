from sqlalchemy import Column, String, Integer, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship, backref

from db import Base


class Stock(Base):
  __tablename__ = 'stocks'

  id = Column(Integer, primary_key=True)
  ticker = Column(String(10))
  name = Column(String(255))

  def __init__(self, ticker, name):
    self.ticker = ticker
    self.name = name


class StockPrice(Base):
  __tablename__ = 'stockprices'

  stock_id = Column(Integer, ForeignKey('stocks.id'), primary_key=True)
  stock = relationship('Stock', backref=backref('prices', uselist=True))
  date = Column(Date, primary_key=True)
  open_price = Column(Numeric)
  close_price = Column(Numeric)
  min_price = Column(Numeric)
  max_price = Column(Numeric)
  volume = Column(Numeric)

  def __init__(self, stock, date, open_price, close_price, min_price, max_price, volume):
    self.stock = stock
    self.date = date
    self.open_price = open_price
    self.close_price = close_price
    self.min_price = min_price
    self.max_price = max_price
    self.volume = volume
