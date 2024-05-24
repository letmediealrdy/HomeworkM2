num = int(input('Введите число от 3 до 20: '))
result = ''
for i in range(1, 20):
    for v in range(1, 20):
        pair = i, v
        if num % sum(pair) == 0 and i < v:
            result += (str(i) + str(v))
print(result)