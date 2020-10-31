i = 0
j = 0
k = 0
while True:
    i += 1
    if(i % 2 != 0):
        print(i)
        j += 1
        k += i
    if(i >= 100):
        break
print("Banyaknya bilangan ganjil:", j)
print("Jumlah seluruh bilangan:", k)
