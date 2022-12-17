def calc_salt(weight):
    try:
      return int(weight) * 0.01
    except ValueError as e:
      print(e)
      return 0


# вызовы фукнции
print(calc_salt(2000))
print(calc_salt('2000'))
print(calc_salt('abc'))

# результаты вывода
#20.0
#20.0
#invalid literal for int() with base 10: 'abc'
#0.0
