import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)        #створення упакованих двійкових даних
print(packed)                                       #10 байтів, ні об'єкти і не текст

file = open('data.bin', 'wb')                       #відкрити двійковий файл для запису
file.write(packed)                                  #запис упакованих двійкових даних
file.close()

data = open('data.bin', 'rb').read()                #відкрити/прочитати двійковий файл даних
print(data)
print(data[4:8])                                    #нарізання байтів всередині
print(list(data))                                   #послідовність 8-бітних байтів
print(struct.unpack('>i4sh', data))                 #знову розпакувати в об'єкти