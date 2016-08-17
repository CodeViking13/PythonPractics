x = int(input("Введите кол-во учащихся "))
if x:
    i = 1
    counter = 1
    print("На первый-второй рассчитайсь:")
    while i <= x:
        print(counter)
        i += 1
        counter += 1
        if counter > 2:
            counter = 1
