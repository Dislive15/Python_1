A = float(input("Степендия: "))
B = float(input("Растходы на проживание: "))

Sum = 0

for i in range(1,11):
    Sum += B - A

    B *= 1.03

print(Sum)