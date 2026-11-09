S = int(input("Сколько дней: "))

Sum = 10

for i in range(S):
    if i > 0:
        Sum *= 1.1

print(Sum)