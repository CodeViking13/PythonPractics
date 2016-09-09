print("Введите слово 'stop' для получения результатов")
sum = 0
while True:
    x = input("Введите число: ")
    x = x.rstrip("\r")
    if x == "stop":
        break
    elif x == "":
        print("Вы не ввели число")
    if x[0] == "-":
        if not x[1:].isdigit():
            print("Нужно ввести число, а не строку")
    else:
        if not x.isdigit():
            print("Нужно ввести число, а не строку")
    x = int(x)
    sum += x
print("Сумма всех чисел, равна: " + str(sum))
input()
