import os

path = input()
print(os.path.exists(path)) //проверяем путь к папке
print(os.access(path, os.R_OK)) //читать
print(os.access(path, os.W_OK)) //писать
print(os.access(path, os.X_OK)) //запускать
