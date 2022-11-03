S = 'sp\xc4m'                                                   #текст Unicode, відмінний від ASCII
print(S)
print(S[2])

file = open('unidata.txt', 'w', encoding='utf-8')               #запис(кодування) тексту UTF-8
print(file.write(S))                                            #записано 4 символа
file.close()

text = open('unidata.txt', encoding='utf-8').read()             #прочитати(декодувати) текст UTF-8
print(text)
print(len(text))

raw = open('unidata.txt', 'rb').read()                          #читати закодовані байти
print(raw)
print(len(raw))                                                 #5 байтів в кодуванні UTF-8

print(text.encode('utf-8'))                                     #вручну кодувати в байти
print(raw.decode('utf-8'))                                      #вручну декодувати в строку

print(text.encode('latin-1'))                                   #байти відрізняються від інших
print(text.encode('utf-16'))
print(len(text.encode('latin-1')),len(text.encode('utf-16')))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))      #декодуються в таку ж строку