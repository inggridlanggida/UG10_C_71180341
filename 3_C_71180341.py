dftr= input("Masukkan daftar pesanan : ")
nilai = dftr.title()
print ("Daftar Pesanan : ", nilai.split (","))
tmbh = input("Masukkan Pesanan yang ingin ditambahkan :")
selanjutnya = tmbh.upper()
if tmbh in dftr:
    print(selanjutnya,"Sudah berada dalam Daftar Pesanan.")
else:
    print("Hasil Penambahan pada Daftar Pesanan :",selanjutnya.split(","))
