def input_nilai(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if 0 <= nilai <= 100:
                return nilai
            print("Nilai harus berada di antara 0 sampai 100.")
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")


def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks:
            return teks
        print("Input tidak boleh kosong.")
