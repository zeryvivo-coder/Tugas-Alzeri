# Quiz Algoritma Python - Input, Percabangan, Perulangan (while)

# 1. Input nama mahasiswa dan tampilkan target nilainya
nama = input("Nama : ")

# Tentukan target berdasarkan nama
if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    # Kalau nama baru, minta input target sendiri
    target = int(input("Target nilai : "))

print(f"Target {nama} adalah {target}")

# 2 & 3. Minta input nilai ujian, cek terhadap target, ulangi maks 3x
percobaan = 1
lulus = False

while percobaan <= 3:
    nilai = int(input(f"Nilai {percobaan} : "))

    if nilai >= target:
        lulus = True
        break
    else:
        if percobaan < 3:
            print(f"Belum mencapai target {target}, silahkan remedial!")
        percobaan += 1

# 4. Tampilkan pesan sesuai hasil akhir
if lulus:
    print(f"{nama} berhasil lulus setelah {percobaan} kali percobaan!")
else:
    print(f"{nama} tidak lulus setelah 3 kali percobaan!")