Count_b = 10
Count_c = 0
Count_t = 0

Price = Count_b * 10 + Count_c * 5 + Count_t * 0.5

while Count_b + Count_c + Count_t != 100:
    Count_b -= 1

    Count_c = (100 - Count_b * 10) / 5

    while Count_c != 0:
        Count_t = (100 - (Count_b * 10 + Count_c * 5)) / 0.5
        if Count_b + Count_c + Count_t == 100:
            break
        Count_c -= 1

print(f"Количство быков: {Count_b}, количество коров: {Count_c}, количество телят: {Count_t}")