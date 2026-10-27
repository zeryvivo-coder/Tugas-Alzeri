# variabel tioe data
nama_mhs =  "Alzeri"
kelas = "C1"

nalgoritma = 90
nagama = 90
nbasisdata = 90

# rata_rata = (nalhoritma + nagama + nbasisdata) / 3
# print(rata_rata)
nilai = int(input("Masukkan Nilai:, "))

# penentuan lulus atau tidak
if nilai >=80 and nilai <=100:
    # kondisi jika terpenuhi
    # maka
    print("Nilai : A")
elif nilai >=70 and nilai <=80:
    print("Nilai: B")
elif nilai >=50 and nilai <=70:
    print("Nilai : C")
else:
    # cukup menampilkan hasil
    # maka
    print("Nilai Lebih Dari 100 Atau Dibawah 50")

    # nilai mata kuliah
nama_mhs = input("Masukkan Nama Mahasiswa: ")
kelas = input("Masukkan Kelas: ")
nalgoritma = int(input("Masukkan Nilai Algoritma: "))
nagama = int(input("Masukkan Nilai Agama: "))
nbasisdata = int(input("Masukkan Nilai Basis Data: "))
njaringan =  int(input("Masukkan nilai jaringan: "))
nkalkulus = int(input("Masukkan nilai kalkulus: "))
nstrukturdata = int(input("Masukkan nilai struktur data: "))
nvisualbasic = int (input("Masukkan nilai visual basic: "))

print("Nama Mahasiswa: ", nama_mhs)
print("Kelas: ", kelas)

rata_rata=( nalgoritma + nagama + nbasisdata + njaringan + nkalkulus + nstrukturdata + nvisualbasic) / 7
print("rata_rata: ", rata_rata)

# penentuan lulus atau tidak
if rata_rata >=90 and rata_rata <=100:
    print("Nilai : A")
elif rata_rata >=80 and rata_rata <=90:
    print("Nilai : B")
elif rata_rata >=70 and rata_rata <=80:
    print("Nilai : C")
elif rata_rata >=60 and rata_rata <=70:
    print("Nilai : D")
elif rata_rata >=50 and rata_rata <=60:
    print("Nilai E")
elif rata_rata >=20 and rata_rata <=50:
    print("Nilai : F")

else:
    print("Nilai lebih dari 100 atau dibawah 20")
