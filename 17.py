path = input()

with open(path, "r") as file:
    content = file.read() //открываем файл на чтение

with open("copy.txt", "w") as file:
    file.write(content) //копируем контент и вставляем в новый файл 
