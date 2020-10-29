BIndo = int(input("Masukkan nilai Bahasa Indonesia :"))
IPA = int(input("Masukkan nilai IPA :"))
Mat = int(input("Masukkan nilai Matematika :"))

if(100 > BIndo > 60) and (100 > IPA > 60) and (100 > Mat > 70):
    hasil = "Lulus"
elif(60 > BIndo > 0) or (60 > IPA > 0) or (70 > Mat > 0):
    hasil = "Tidak Lulus"

print("Kelulusan :", hasil)
