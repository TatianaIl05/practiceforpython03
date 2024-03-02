import math
x, y, n = map(int, input('Введите цену - рубли, копейки, количество заказов: ').split())
r = x*n
k = y*n
if k >= 100:
    r += math.floor(k/100)
    k %= 100
print(f'{r} руб. {k} коп.')
