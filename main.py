from pathlib import Path
from mahasiswa.data_manager import (
    tampilkan_data, tambah_data, cari_data, filter_prodi,
    hitung_rekap, hapus_data, data_nilai_lulus
)
from mahasiswa.file_handler import baca_csv, simpan_json
from mahasiswa.utils import input_nilai, input_teks

FOLDER = Path(__file__).parent
FILE_CSV = FOLDER / "data" / "mahasiswa.csv"
FILE_JSON = FOLDER / "data" / "hasil_mahasiswa.json"


def tampilkan_menu():
    print("APLIKASI MANAJEMEN DATA MAHASISWA")
    print("1. Tampilkan data")
    print("2. Tambah data")
    print("3. Cari data")
    print("4. Filter berdasarkan prodi")
    print("5. Rekap jumlah mahasiswa")
    print("6. Hapus data")
    print("7. Tampilkan mahasiswa dengan nilai >= 75")
    print("8. Simpan data ke JSON")
    print("0. Keluar")


def jalankan():
    try:
        data = baca_csv(FILE_CSV)
    except FileNotFoundError:
        print("File CSV tidak ditemukan. Program dimulai dengan data kosong.")
        data = []
    except (ValueError, OSError) as error:
        print(f"Gagal membaca data: {error}")
        data = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            print(tampilkan_data(data))

        elif pilihan == "2":
            mahasiswa = {
                "nim": input_teks("NIM: "),
                "nama": input_teks("Nama: "),
                "prodi": input_teks("Program studi: "),
                "nilai": input_nilai("Nilai (0-100): ")
            }
            data, berhasil = tambah_data(data, mahasiswa)
            if berhasil:
                print("Data berhasil ditambahkan.")
            else:
                print("NIM sudah terdaftar. Data tidak ditambahkan.")

        elif pilihan == "3":
            kata = input_teks("Masukkan NIM atau nama: ")
            hasil = cari_data(data, kata)
            print(tampilkan_data(hasil))

        elif pilihan == "4":
            prodi = input_teks("Masukkan nama prodi: ")
            hasil = filter_prodi(data, prodi)
            print(tampilkan_data(hasil))

        elif pilihan == "5":
            rekap = hitung_rekap(data)
            if not rekap:
                print("Belum ada data untuk direkap.")
            else:
                for prodi, jumlah in rekap.items():
                    print(f"{prodi}: {jumlah} mahasiswa")

        elif pilihan == "6":
            nim = input_teks("Masukkan NIM yang akan dihapus: ")
            data, berhasil = hapus_data(data, nim)
            print("Data berhasil dihapus." if berhasil else "NIM tidak ditemukan.")

        elif pilihan == "7":
            hasil = data_nilai_lulus(data)
            print("Daftar NIM dan nilai >= 75:", hasil if hasil else "Tidak ada data.")

        elif pilihan == "8":
            try:
                simpan_json(data, FILE_JSON)
                print(f"Data berhasil disimpan ke {FILE_JSON}")
            except OSError as error:
                print(f"Gagal menyimpan file: {error}")

        elif pilihan == "0":
            print("Terima kasih. Program selesai.")
            break

        else:
            print("Pilihan tidak tersedia. Masukkan angka 0 sampai 8.")


if __name__ == "__main__":
    jalankan()