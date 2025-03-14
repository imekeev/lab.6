import string

for letter in string.ascii_uppercase: //проходимся по всем заглавынм буквам алфавита
    file_name = f"{letter}.txt" //создаем имя файла начиная с A.txt
    with open(file_name, 'w') as file:
        file.write(f"This is {file_name}") //открываем файл на запись и записываем 
