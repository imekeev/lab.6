path = input()
l = [1, 2, 3, 4, 5, 6, 7]

with open(path, 'w') as file: //открываем файл на запись данных чисел ))
    for x in l:
        file.write(str(x) + '\n') //каждое число с новой строки:)
