from random import randint
print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!")
bil = randint (0,100)
i = 0
while True:
    tebak = int(input("Silahkan masukkan tebakan anda:"))
    if(0 <= tebak < bil):  
        print("Bilangan tebakan anda terlalu kecil")
    elif(100 >= tebak > bil):
        print("Bilangan tebakan anda terlalu besar")
    elif(tebak == bil):
        break
    print("")
    i += 2
    nilai = 100 - i
print("Bilangan tebakan anda BENAR")
print("Skor Anda :",nilai)
