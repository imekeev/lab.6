path = input()
count = 0
with open(path, "r") as file: //открываем файл на чтение 
    for line in file: //проходимся по каждой строке и ведем подсчет
        count += 1

print(count)
