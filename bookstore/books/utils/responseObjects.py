class Book():
  def __init__(self, title, isbn13, price):
    self.title = title
    self.isbn13 = isbn13
    self.price = price
  def toJSON(self):
    return self.__dict__
    
class FullBookHistory():
  def __init__(self, title, isbn13, details, publisher, year, price):
    self.title = title
    self.isbn13 = isbn13
    self.details = details
    self.publisher = publisher
    self.year = year
    self.price = price
  def toJSON(self):
    return self.__dict__