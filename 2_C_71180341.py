hitung = int(input ("Masukkan Bulan (1-12) : "))
if hitung ==1 or hitung ==3 or hitung ==5 or hitung ==7 or hitung ==8 or hitung ==10 or hitung ==12:
    print("Jumlah Hari: 31")
elif hitung ==4 or hitung ==6 or hitung ==9 or hitung ==11:
    print("Jumlah Hari: 30")
else:
    print("Jumlah Hari: 28")
