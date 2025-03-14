path = input()

with open(path, "r") as file:
    content = file.read()

with open("copy.txt", "w") as file:
    file.write(content)