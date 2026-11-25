Aplikasi Manajemen Data Mahasiswa

Deskripsi : 
Aplikasi CLI sederhana untuk mengelola data mahasiswa menggunakan Python standard library.

Fitur : 
- Menampilkan, menambah, mencari, memfilter, dan menghapus data.
- Rekap jumlah mahasiswa per program studi.
- Menampilkan NIM dan nilai mahasiswa dengan nilai minimal 75.
- Membaca data dari CSV dan menyimpan hasil ke JSON.
- Validasi input dan penanganan kesalahan file/data.

Struktur folder :
```text
UTS_Manajemen_Mahasiswa/
├── main.py
├── mahasiswa/
│   ├── __init__.py
│   ├── data_manager.py
│   ├── file_handler.py
│   └── utils.py
├── data/
│   ├── mahasiswa.csv
│   └── hasil_mahasiswa.json  (dibuat saat menu 8 dipilih)
└── README.md
```

Kebutuhan :
- Python 3
- Tidak membutuhkan library tambahan karena menggunakan standard library.

Cara menjalankan :
1. Buka terminal pada folder `Manajemen_Mahasiswa`.
2. Jalankan:
   ```bash
   py main.py
   ```
   Pada beberapa sistem, gunakan `python3 main.py`.
3. Pilih menu sesuai kebutuhan.
4. Pilih menu 8 untuk menyimpan data ke `data/hasil_mahasiswa.json`.

Format data CSV :
Header wajib: `nim,nama,prodi,nilai`.
Nilai harus berupa angka dari 0 sampai 100.

Pengujian :
- Data normal: jalankan menu 1 untuk melihat data dari CSV.
- Pencarian: menu 3, masukkan nama atau NIM.
- Filter: menu 4, masukkan nama program studi.
- Duplikat: menu 2, gunakan NIM yang sudah ada.
- Input tidak valid: menu 2, masukkan nilai berupa huruf atau di luar 0-100.
- File hilang: ubah nama sementara `mahasiswa.csv`, lalu jalankan program. Program memberi pesan dan berjalan dengan data kosong.
- Format CSV salah: ubah header atau isi nilai, lalu jalankan program. Program menampilkan pesan kesalahan.

Struktur data :
- List: menyimpan kumpulan data mahasiswa.
- Dictionary: menyimpan atribut setiap mahasiswa dan hasil rekap.
- Set: memeriksa NIM yang sudah terdaftar agar tidak terjadi data ganda.

Module dan package :
Folder `mahasiswa` merupakan package buatan sendiri.
- `data_manager.py`: operasi pengelolaan data.
- `file_handler.py`: membaca CSV dan menulis JSON.
- `utils.py`: validasi input.
- `main.py`: menu dan penghubung antar-module.

Catatan referensi dan bantuan :
- Referensi teknis: dokumentasi resmi Python untuk `csv`, `json`, `pathlib`, dan struktur data bawaan.
- Library: Python standard library (`csv`, `json`, `pathlib`).
- Bantuan AI: digunakan untuk membantu penyusunan rancangan, kode.