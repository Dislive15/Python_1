import math

x = float(input("Длина палки: "))
h = int(input("Шаг расстояния от конца палки до стены: "))

Sum = 1

for y in range(2,3,h):
    a = math.acos(y/x)*180/math.pi

    print(f"Угол {a}")