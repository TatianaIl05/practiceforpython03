import math
n = float(input('Введите угол: '))
hours = math.floor(n/30)
minutes = math.floor(2*(n - 30*hours))
print(f'Прошло полных {hours} ч. и {minutes} мин.')
