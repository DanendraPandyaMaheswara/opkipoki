import json
import os

class TabunganSampah:
    with open('anggotas.json') as file:
        anggota = json.load(file)

    def __init__(self):
        self.anggota = {}
        self.harga_sampah = {}
        self.transaksi = {}

    def cari_anggota_by_id(self, id_anggota):
        with open('anggotas.json') as file:
            data_anggota = json.load(file)
        
        if os.path.exists('anggotas.json'):
            with open('anggotas.json', 'r') as file:
                anggotas = json.load(file)
            if id_anggota in anggotas:
                return anggotas[id_anggota]
        return {}

    def tampilkan_anggota(self, data_anggota):
        if data_anggota:
            print("ID Anggota:", data_anggota['idanggota'])
            print("Nama:", data_anggota['nama'])
            print("Alamat:", data_anggota['alamat'])
            print("Telepon:", data_anggota['telepon'])
            print("Tanggal Daftar:", data_anggota['tanggal'])
        else:
            print("Data anggota tidak ditemukan.")


    def ubah_anggota(self, id_anggota, nama, alamat, telepon):
        if id_anggota in self.anggota:
            data_anggota = self.anggota[id_anggota]
            data_anggota["nama"] = nama
            data_anggota["alamat"] = alamat
            data_anggota["telepon"] = telepon
            print("Data anggota berhasil diubah.")
        else:
            print("Data anggota tidak ditemukan.")

    def tampilkan_menu(self):
        print("--PROGRAM TABUNGAN SAMPAH--")
        print("Pilih berdasarkan Nomor:")
        print("1. Pengelolaan Keanggotaan")
        print("  1a. Penambahan Data Anggota")
        print("  1b. Pencarian Data Anggota")
        print("  1c. Pengubahan Data Anggota")
        print("2. Pengelolaan Tabungan Anggota")
        print("  2a. Penambahan Tabungan")
        print("  2b. Penarikan Tabungan")
        print("  2c. Menampilkan Tabungan")
        print("9. Exit")

    def jalankan_program(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("Masukkan pilihan Anda: ")
            if pilihan == "1a":
                from anggota import tambah_anggota
                tambah_anggota()
                konfirmasi = input("Ingin kembali ke menu awal? (Y/y = Ya, T/t = Tidak): ")
                if konfirmasi.lower() == "t":
                    break
                print()
            elif pilihan == "1b":
                id_anggota = input("Masukkan ID Anggota: ")
                data_anggota = self.cari_anggota_by_id(id_anggota) 
                self.tampilkan_anggota(data_anggota)
                konfirmasi = input("Ingin kembali ke menu awal? (Y/y = Ya, T/t = Tidak): ")
                if konfirmasi.lower() == "t":
                    break
                print()
            elif pilihan == "1c":
                id_anggota = input("Masukkan ID Anggota: ")
                nama = input("Masukkan Nama Anggota Baru: ")
                alamat = input("Masukkan Alamat Anggota Baru: ")
                telepon = input("Masukkan Telepon Anggota Baru: ")
                self.ubah_anggota(id_anggota, nama, alamat, telepon)
                print()
                konfirmasi = input("Ingin kembali ke menu awal? (Y/y = Ya, T/t = Tidak): ")
                if konfirmasi.lower() == "t":
                    break
            elif pilihan == "2a":
                from tabungansampah import tambah_tabungan
                id_anggota = input("Masukkan ID Anggota: ")
                kode_sampah = input("Masukkan Kode Sampah: ")
                kuantitas = float(input("Masukkan Kuantitas: "))
                tambah_tabungan(id_anggota, kode_sampah, kuantitas)
                print("Tabungan berhasil ditambahkan.")
                print()
            elif pilihan == "2b":
                from tabungansampah import tarik_tabungan
                id_anggota = input("Masukkan ID Anggota: ")
                jumlah_penarikan = float(input("Masukkan Jumlah Penarikan: "))
                tarik_tabungan(id_anggota, jumlah_penarikan)
                print()
            elif pilihan == "2c":
                from tabungansampah import tampilkan_tabungan
                id_anggota = input("Masukkan ID Anggota: ")
                tampilkan_tabungan(id_anggota)
                print()
            elif pilihan == "9":
                print("Terima kasih telah menggunakan program ini.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
                print()
            
tabungan = TabunganSampah()
tabungan.jalankan_program()