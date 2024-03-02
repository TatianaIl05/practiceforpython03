raw = input('Enter number: ')
try:
    num = int(raw)
    print(num)
except ValueError:
    print('Ошибка, введите число, а не слово')
