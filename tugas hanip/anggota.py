import json
import random
import os
import datetime

def generate_id_anggota():
    characters = "Z0123456789"
    id_anggota = ''.join(random.choice(characters) for _ in range(5))
    return id_anggota

def tambah_anggota():
    with open('anggotas.json') as file:
        data_anggota = json.load(file)
    
    id_anggota = input("Masukkan ID anggota: ")
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    telepon = input("Masukkan nomor telepon: ")

    tanggal = datetime.date.today().strftime("%Y-%m-%d")
    data_anggota[id_anggota] = {
        'idanggota': id_anggota,
        'nama': nama,
        'alamat': alamat,
        'tanggal': tanggal,
        'telepon': telepon
    }

    with open('anggotas.json', 'w') as file:
        json.dump(data_anggota, file)

    print("Berhasil menambahkan data anggota.")

tambah_anggota()