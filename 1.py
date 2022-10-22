# Вычислить число c заданной точностью d

from math import pi

d = float(input("d = "))
i = 0
while d < 1:
    d = d * 10
    i += 1
print(f'π = {round(pi, i)}')