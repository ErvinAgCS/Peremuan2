menu = { 
    "Jeruk   ": 15000,
    "Apel    ": 30000,
    "Mangga  ": 20000, 
    "Manggis ": 7000,
    "Durian  ": 50000,
}
print("daftar menu")
for i in menu :    
    print(i,"Harga","Rp.",menu[i],"Perkilo")
print("Pembelian diatas Rp.70000 mendapatkan diskon sebesar 10%")

BuahJeruk = int(input("Berapa kilo jeruk :"))
BuahApel = int(input("Berapa kilo apel :"))
BuahMangga = int(input("Berapa kilo mangga :"))
BuahManggis = int(input("Berapa kilo manggis :"))
BuahDurian = int(input("Berapa kilo durian :"))

Jeruk = 15000 
Apel = 30000 
Mangga = 20000 
Manggis = 7000 
Durian = 50000 

TotalJeruk = BuahJeruk * Jeruk
TotalApel = BuahApel * Apel
TotalMangga = BuahMangga * Mangga 
TotalManggis =BuahManggis * Manggis
TotalDurian = BuahDurian * Durian 
Jumlah = TotalJeruk + TotalApel + TotalMangga + TotalManggis + TotalDurian

if Jumlah > 70000 :
    diskon = Jumlah*10/100
    total  = Jumlah - diskon
else:
    total = Jumlah 

print("Total yang harus dibayar Rp.:%0.f"%total)


    
