path = input()
l = [1, 2, 3, 4, 5, 6, 7]

with open(path, 'w') as file:
    for x in l:
        file.write(str(x) + '\n')