for x1 in range(0,29):
    x = 2 * x1 ** 2 + 29

    Count = 0
    for i in range(1,x+1):
        if x % i == 0:
            Count += 1
    if Count == 2:
        print(x)