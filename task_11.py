import math

a, b, c = map(int, input('Введите длины сторон треугольника: ').split())

if a < b+c and b < a+c and c < a+b:
    cos_a = (b**2 + c**2 - a**2) / (2 * b * c)
    angle_a = math.degrees(math.acos(cos_a))
    cos_b = (a**2 + c**2 - b**2) / (2 * a * c)
    angle_b = math.degrees(math.acos(cos_b))
    cos_c = (b**2 + a**2 - c**2) / (2 * a * b)
    angle_c = math.degrees(math.acos(cos_c))

    print(f'Угол напротив a = {round(angle_a)}, угол напротив b = {round(angle_b)}, угол напротив c = {round(angle_c)}')
    
else:
    print('Неверные длины')
