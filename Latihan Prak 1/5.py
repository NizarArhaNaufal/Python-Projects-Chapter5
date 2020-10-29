kode = input("Masukkan Kode Karyawan :")
nama = input("Masukkan Nama Karyawan :")
golongan = input("Masukkan Golongan Gaji :")
status = input("Masukkan Status Menikah(1: Menikah, 2:Belum Menikah):")
if(status == "1"):
    anak = int(input("Masukkan Jumlah Anak :"))
    
print("===================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("===================================")
print("Nama Karyawan : " , nama , " (Kode:" , kode , ")")
print("Golongan :" , golongan)
if(status == "1"):
    print("Status Menikah : Menikah")
    print("Jumlah Anak :",anak)
elif(status == "2"):
    print("Status Menikah : Belum Menikah")
print("-----------------------------------")

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
    
persenSutri = 10
persenAnak = 5    
if(status == "1") and (anak == 0):
    tunjSutri = gajipokok * (persenSutri/100)
    gajikotor = gajipokok + tunjSutri
    gajiBersih = gajikotor - jumpotongan
elif(status == "1") and (anak > 0):
    tunjSutri = gajipokok * (persenSutri/100)
    tunjAnak = gajipokok * (persenAnak/100)
    gajikotor = gajibersih + tunjSutri + (tunjAnak * anak)
    gajiBersih = gajikotor - jumpotongan
    
print("Gaji Pokok : Rp.",gajipokok)
if(status == "2"):
    print("Potongan : Rp.",jumpotongan)
    print("----------------------------------")
    print("Gaji Bersih : Rp.",gajibersih)
elif(status == "1") and (anak == 0):
    print("Tunjangan Istri/Suami : Rp.",tunjSutri)
    print("----------------------------------")
    print("Gaji Kotor :Rp.",gajikotor)
    print("Potongan : Rp.",jumpotongan)
    print("----------------------------------")
    print("Gaji Bersih : Rp.",gajiBersih)
elif(status == "1") and (anak > 0):
    print("Tunjangan Istri/Suami : Rp.",tunjSutri)
    print("Tunjangan Anak : Rp.",tunjAnak)
    print("----------------------------------")
    print("Gaji Kotor :Rp.",gajikotor)
    print("Potongan : Rp.",jumpotongan)
    print("----------------------------------")
    print("Gaji Bersih : Rp.",gajiBersih)


