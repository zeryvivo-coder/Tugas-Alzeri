def kasir_restoran():
    # 1. Mulai Program
    print("="*45)
    print("   APLIKASI KASIR RESTORAN SEDERHANA")
    print("="*45)
    
    total = 0  # inisialisasi variabel total = 0
    pesanan_list = [] # buat nyimpen rincian

    # Daftar Menu (sesuai gambar)
    menu = {
        1: ("Nasi Goreng", 25000),
        2: ("Mie Ayam", 15000),
        3: ("Ayam Geprek", 20000),
        4: ("Sate Ayam", 30000),
        5: ("Bakso", 18000)
    }

    # 3 & 4. Proses Pemesanan + Perulangan While
    while True:
        # 2. Tampilkan Menu Makanan
        print("\n--- DAFTAR MENU ---")
        for k, v in menu.items():
            print(f"{k}. {v[0]:<12} - Rp{v[1]:,}".replace(",", "."))
        print("0. Selesai Memilih")
        print(f"\nTotal Sementara: Rp{total:,}".replace(",", "."))

        try:
            pilihan = int(input("Apakah Pilihan (0-5)? : "))

            # 4. Apakah Pilihan 0?
            if pilihan == 0:
                print("\nSelesai memilih...")
                break  # Ya -> lanjut ke hitung diskon

            if pilihan not in menu:
                print("Pilihan tidak valid! Pilih 0-5 saja.")
                continue # Tidak -> kembali ke tampilkan menu

            # Pilih Menu & Jumlah
            jumlah = int(input(f"Jumlah pesanan {menu[pilihan][0]} : "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                continue

            nama, harga = menu[pilihan]
            subtotal = harga * jumlah # Operasi Aritmatika
            total += subtotal

            pesanan_list.append((nama, jumlah, harga, subtotal))
            print(f"-> Ditambahkan: {jumlah}x {nama} = Rp{subtotal:,}".replace(",", "."))

        except ValueError:
            print("Input harus angka! Coba lagi.")
            continue

    # Jika belum pesan apa-apa
    if total == 0:
        print("Tidak ada pesanan. Program selesai.")
        return

    # 5. Hitung Diskon (Percabangan if-else)
    if total > 200000:
        persen_diskon = 20
        potongan = total * 0.2
    else:
        persen_diskon = 0
        potongan = 0

    total_bayar = total - potongan

    # 6. Tampilkan Struk Pembayaran
    print("\n" + "="*45)
    print("        STRUK PEMBAYARAN")
    print("="*45)
    for nama, jml, hrg, sub in pesanan_list:
        print(f"{nama} {jml}x Rp{hrg:,} = Rp{sub:,}".replace(",", "."))
    print("-"*45)
    print(f"Total Belanja   : Rp {total:,}".replace(",", "."))
    print(f"Diskon          : {persen_diskon}% / 0%")
    print(f"Potongan        : Rp {potongan:,.0f}".replace(",", "."))
    print("-"*45)
    print(f"Total Bayar     : Rp {total_bayar:,.0f}".replace(",", "."))
    print("="*45)
    print("          Terima Kasih!")
    print("="*45)

# Jalankan program
if __name__ == "__main__":
    kasir_restoran()