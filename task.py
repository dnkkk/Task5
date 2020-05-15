def third_root(x):
    y = x
    y1 = 0.5 * (y + 3 * x / (2 * y ** 2 + x / y))
    while abs(y1 - y) >= pow(10, -5):
        y = y1
        y1 = 0.5 * (y + 3 * x / (2 * y ** 2 + x / y))

    return y1


print("Введите x: ", end="")
y = third_root(int(input()))
print("Ответ:", y)
