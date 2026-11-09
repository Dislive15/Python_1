n = int(input("Количество часов: "))

Sum = 1

for i in range(3,(n+1)*3,3):
    Sum *= 2

    print(f"Количество {Sum}")