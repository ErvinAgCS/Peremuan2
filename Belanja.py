BuahJeruk = float(input("Berapa kilo jeruk :"))
BuahApel = float(input("Berapa kilo apel :"))
BuahMangga = float(input("Berapa kilo mangga :"))
BuahManggis = float(input("Berapa kilo manggis :"))
BuahDurian = float(input("Berapa kilo durian :"))

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
TotalKeseluruhan = TotalJeruk + TotalApel + TotalMangga + TotalManggis + TotalDurian

print("Total yang harus dibayar adalah :")
print("Buah Jeruk :%0.f "% TotalJeruk )
print("Buah Apel :%0.f "% TotalApel )
print("Buah Mangga :%0.f "% TotalMangga )
print("Buah Manggis :%0.f"% TotalManggis )
print("Buah Durian :%0.f"% TotalDurian )
print("Semuanya jadi:%0.f"%TotalKeseluruhan)