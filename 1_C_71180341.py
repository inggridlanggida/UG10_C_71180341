print("========== Pilih Menu ==========")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

n1 = int(input('Masukkan Angka pertama: '))
n2 = int(input('Masukkan Angka kedua: '))
choice = input('Pilihan Anda: ')
if choice == "1" :
    penjmlhn = n1+n2
    print("Hasil :",penjmlhn)
elif choice == "2" :
    krg = n1-n2
    print("Hasil :",krg)
elif choice == "3" :
    kli = n1*n2
    print("Hasil :",kli)
else:
    bgi=(n1/n2)
    print("Hail :",bgi)
