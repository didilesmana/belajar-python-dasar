# Program Manage Kontak

def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("=================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")
        print("=================")

def new_kontak():
    nama = input("Nama : ")
    email = input("Email : ")
    telepon = input("Telepon : ")
    kontak = {
        "nama" : nama,
        "email" : email,
         "telepon" : telepon
    }
    return kontak

def hapus_kontak(daftar_kontak):
    telepon = input("No Telepon yang dihapus : ")

    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon = daftar_kontak[i]
            index = i
            break
    if index == -1:
        print("data tidak ditemukan")
    else:
        del daftar_kontak[index]
        print("data berhasil dihapus")

def cari_kontak(daftar_kontak)
    nama_cari = input("Nama yang dicari : ")
            
    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.find(nama_cari) != -1:
        print("=================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")
        print("=================")
        break
    else:
        print("data tidak ditemukan")
