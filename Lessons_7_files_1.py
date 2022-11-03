f = open('data.txt', 'w')           #створити новий файл в режимі запису
f.write('Hello\n')                  #записати в нього строки символів
print(f)

f.write('world\n')
f.close()                           #закрити для скидування буферів виводу на диск
print(f)

f = open('data.txt')
text = f.read()                     #прочитати весь вміст файла
print(text)

for line in open('data.txt'):
    print(line)