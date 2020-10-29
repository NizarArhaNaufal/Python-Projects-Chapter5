kode = input("Masukkan Kode Karyawan :")
nama = input("Masukkan Nama Karyawan :")
golongan = input("Masukkan Golongan Gaji :")

print("===================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("===================================")
print("Nama Karyawan : " , nama , " (Kode:" , kode , ")")
print("Golongan :" , golongan)

if(golongan == "A"):
    gajipokok = 10000000
    potongan = 2.5
    jumpotongan = gajipokok * (potongan/100)
    gajibersih = gajipokok - jumpotongan

elif(golongan == "B"):
    gajipokok = 8500000
    potongan = 2
    jumpotongan = gajipokok * (potongan/100)
    gajibersih = gajipokok - jumpotongan
    
elif(golongan == "C"):
    gajipokok = 7000000
    potongan = 1.5
    jumpotongan = gajipokok * (potongan/100)
    gajibersih = gajipokok - jumpotongan
    
elif(golongan == "D"):
    gajipokok = 5500000
    potongan = 1
    jumpotongan = gajipokok * (potongan/100)
    gajibersih = gajipokok - jumpotongan


print("Gaji Pokok : Rp.",gajipokok)
print("Potongan : Rp.",jumpotongan)
print("-----------------------------------")
print("Gaji Bersih : Rp.",gajibersih)

