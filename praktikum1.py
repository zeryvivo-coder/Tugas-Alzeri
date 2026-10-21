Tugas = float(input("Nilai tugas:  "))
UTS = float(input("Nilai UTS: "))
UAS = float(input("Nilai UAS: "))
Kehadiran = float(input("Kehadiran: "))

nilai_akhir = (0.20 * Tugas) + (0.30 * UTS) + (0.50 * UAS)

print("Nilai akhir:", nilai_akhir)

if nilai_akhir >= 85 and Kehadiran >= 90 and nilai_akhir % 2 == 0:
    print("Status:LULUS DENGAN PREDIKAT")
elif nilai_akhir >= 75 and kehadiran >= 80:
    print("Status:LULUS")
else:
    print("Status:BELUM LULUS")
