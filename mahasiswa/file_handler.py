import csv
import json
from pathlib import Path

def baca_csv(nama_file):
    data = []
    with open(nama_file, mode="r", newline="", encoding="utf-8") as file:
        pembaca = csv.DictReader(file)
        kolom_wajib = {"nim", "nama", "prodi", "nilai"}
        if not kolom_wajib.issubset(set(pembaca.fieldnames or [])):
            raise ValueError("Kolom CSV harus: nim, nama, prodi, nilai")

        for baris in pembaca:
            try:
                nilai = float(baris["nilai"])
            except (ValueError, TypeError):
                raise ValueError(f"Nilai mahasiswa tidak valid pada NIM {baris.get('nim', '')}")

            if not baris["nim"].strip() or not baris["nama"].strip():
                raise ValueError("NIM dan nama tidak boleh kosong.")
            if not 0 <= nilai <= 100:
                raise ValueError(f"Nilai harus 0 sampai 100 pada NIM {baris['nim']}.")

            data.append({
                "nim": baris["nim"].strip(),
                "nama": baris["nama"].strip(),
                "prodi": baris["prodi"].strip(),
                "nilai": nilai
            })
    return data


def simpan_json(data, nama_file):
    with open(nama_file, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    return True
