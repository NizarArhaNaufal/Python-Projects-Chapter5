BIndo = int(input("Masukkan nilai Bhs Indonesia :"))
IPA = int(input("Masukan nilai IPA :"))
Mat = int(input("Masukan nilai matematika :"))

if(100 >= BIndo >= 60) and (100 >= IPA >= 60) and (100 >= Mat >= 70):
    hasil = "Lulus"
elif(60 > BIndo >= 0) or (60 > IPA >= 0) or (70 > Mat >= 0):
    hasil = "Tidak lulus"
    
if(100 >= BIndo >= 60) and (100 >= IPA >= 60) and (100 >= Mat >= 70) or (60 > BIndo >= 0) or (60 > IPA >= 0) or (70 > Mat >= 0):
    print("Kelulusan :" , hasil)
if(60 > BIndo >= 0):
    print("Nilai Bahasa Indonesia kurang dari 60")
if(60 > IPA >= 0):
    print("Nilai IPA kurang dari 60")
if(70 > Mat >=0):
    print("Nilai Matematika kurang dari 70")
