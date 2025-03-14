import os

path = input()

if os.path.exists(path): //существует ли путь вообще проверка 
    if os.path.isfile(path): //это файл или папква
        if os.access(path, os.W_OK): //проверка на удаление файла
            os.remove(path) //удаляем файл если все ок
        else:
            print("Can't be removed") //если нет прав на удаление
    else:
        print("This is not a file") //если это не файл 
else:
    print("Path does not exist") //если нет пути к этому файлу
