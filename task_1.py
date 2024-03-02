cost_in_rub = int(input('Введите стоимость биткоина в рублях: '))
for i in range(2):
    cost_in_rub = (cost_in_rub - cost_in_rub % 10)/10
print(cost_in_rub % 10)
