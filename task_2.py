time = int(input('Введите секунды: '))
hours = time//60**2
minutes = (time - hours*60**2)//60
seconds = time - hours*60**2 - minutes*60
print(f'{hours} ч. {minutes} мин. {seconds} с.')
