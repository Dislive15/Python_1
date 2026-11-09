Sum = 64

Count_g = 32
Count_c = 0

Count = 0

while Count_c <= 16:
    Count += 1
    print(f"Количество гусей: {Count_g}, количество кроликов: {Count_c}",Count)

    Count_g -= 2
    Count_c += 1