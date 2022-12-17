import csv


class Item:
  pay_rate = 0.8  # Уровень оплаты после скидки 20%
  all = []

  def __init__(self, name: str, price: float, quantity=0):
    self.__name = name
    self.price = price
    self.quantity = quantity

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    if len(value) > 10:
      raise Exception("Название слишком длинное!")
    else:
      self.__name = value

  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * self.pay_rate

  @classmethod
  def instantiate_from_csv(cls, file):
      with open(file, "r") as f:
          reader = csv.DictReader(f)
          items = list(reader)

      for item in items:
          cls.all.append(Item(name = item.get('name'), price = item.get('price'), quantity = item.get('quantity')))

  def __str__(self):
    return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'




Item.instantiate_from_csv('items.csv')

for item in Item.all:
  print(item)

       # Item('Phone', 100.0, 1)
       # Item('Laptop', 1000.0, 3)
       # Item('Cable', 10.0, 5)
       # Item('Mouse', 50.0, 5)
       # Item('Keyboard', 74.9, 5)
