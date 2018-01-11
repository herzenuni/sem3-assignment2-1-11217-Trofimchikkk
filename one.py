a = int(input('Введите первое число'))
b = int(input('Введите второе число'))

def function(a, b):
    while a != b:
      if a > b:
        a = a - b
      else:
        b = b - a
    return a
print('НОД: {}'.format(function(a, b)))
