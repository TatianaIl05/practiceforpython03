att, comp, yds, td, ints = map(int, input('Введите значения: ').split())
a = min(max(((comp/att) - 0.3) * 5, 0), 2.375)
b = min(max(((yds/att) - 3) * 0.25, 0), 2.375)
c = min(max((td/att) * 20, 0), 2.375)
d = min(max(2.375 - (ints/att) * 25, 0), 2.375)
qb_rating = (a + b + c + d) / 0.06
print(qb_rating)
