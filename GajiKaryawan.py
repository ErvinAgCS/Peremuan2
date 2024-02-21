#Gaji pokok karyawan adalah 2.000.000 perbulan
#uang transpot 10.000 perhari
#uang makan 10.000 perhari
#tunjangan jabatan gaji pokok di kali jabatan
#honor lembur 15.000 perjam 

Nakar = input("Masukan Nama : ")
Jabatan = int(input("Masukan Jabatan : "))
Masuk = int(input("Berapa Hari Masuk Keja : "))
Jam = int(input("Berapa Jam Anda Lembur : "))

Gaji_Pokok = 2000000
Tunjangan = Gaji_Pokok * Jabatan
Transport = 10000 * Masuk
Makan = 10000 * Masuk
Lembur = 15000 * Jam
    
Total_Gaji = Gaji_Pokok + Tunjangan + Transport + Makan + Lembur
print("================================")
print("Gaji Pokok :",Gaji_Pokok)
print("Tunjangan Jabatan :",Tunjangan)
print("Total Transport Transport :",Transport)
print("Uang Makan :",Makan)
print("Uang Lembur :",Lembur)
print("keseluruhan gaji yang diterima adalah :%0.f"% Total_Gaji)





     




