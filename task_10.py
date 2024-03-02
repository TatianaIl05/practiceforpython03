import math

a, b, c = map(int, input('Введите длины сторон треугольника: ').split())
if a + b > c and a+c > b and b+c > a:
    alpha = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
    betta = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / 2 * a * c))
    gamma = math.degrees(int(math.acos((a**2+b**2-c**2)/2*a*b)))
    print(f'Угол напротив a = {alpha}, угол напротив b = {betta}, угол напротив c = {gamma}.')
