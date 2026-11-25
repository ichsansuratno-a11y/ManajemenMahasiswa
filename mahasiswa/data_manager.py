def tampilkan_data(data):
    if not data:
        return "Belum ada data mahasiswa."

    hasil = []
    for mhs in data:
        hasil.append(
            f"NIM: {mhs['nim']} | Nama: {mhs['nama']} | "
            f"Prodi: {mhs['prodi']} | Nilai: {mhs['nilai']}"
        )
    return "\n".join(hasil)


def tambah_data(data, mahasiswa):
    nim_terdaftar = {mhs["nim"] for mhs in data}
    if mahasiswa["nim"] in nim_terdaftar:
        return data, False
    data_baru = data + [mahasiswa]
    return data_baru, True


def cari_data(data, kata_kunci):
    kata_kunci = kata_kunci.lower()
    hasil = [
        mhs for mhs in data
        if kata_kunci in mhs["nim"].lower()
        or kata_kunci in mhs["nama"].lower()
    ]
    return hasil


def filter_prodi(data, prodi):
    return [mhs for mhs in data if mhs["prodi"].lower() == prodi.lower()]


def hitung_rekap(data):
    rekap = {}
    for mhs in data:
        prodi = mhs["prodi"]
        rekap[prodi] = rekap.get(prodi, 0) + 1
    return rekap


def hapus_data(data, nim):
    data_baru = [mhs for mhs in data if mhs["nim"] != nim]
    return data_baru, len(data_baru) != len(data)


def data_nilai_lulus(data):
    return {mhs["nim"]: mhs["nilai"] for mhs in data if mhs["nilai"] >= 75}