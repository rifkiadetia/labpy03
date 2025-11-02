# latihan3.py
# Program simulasi mesin ATM sederhana
# Saldo awal
saldo = 1000000  # Rp 1.000.000
# Loop utama untuk menu ATM
while True:
    print(f"\nSaldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    pilihan = input("Pilih menu (1/2): ")
    if pilihan == "1":
        # Tarik uang
        try:
            jumlah_tarik = int(input("Masukkan jumlah penarikan: "))
            if jumlah_tarik > saldo:
                print("Saldo tidak cukup!")
            elif jumlah_tarik <= 0:
                print("Jumlah penarikan harus lebih dari 0!")
            else:
                saldo -= jumlah_tarik
                print("Penarikan berhasil!")
                if saldo == 0:
                    print("Saldo habis. Terima kasih telah menggunakan ATM!")
                    break
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
    elif pilihan == "2":
        # Keluar
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid! Pilih 1 atau 2.")