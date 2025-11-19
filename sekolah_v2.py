import json
import random
import time
import os
from datetime import datetime

# ---------------------
# 1. Hitung Nilai Akhir
# ---------------------
def hitung_nilai_akhir():
    print("\n=== Hitung Nilai Akhir ===")
    try:
        tugas = float(input("Nilai Tugas (40%): "))
        uts   = float(input("Nilai UTS (30%): "))
        uas   = float(input("Nilai UAS (30%): "))
    except ValueError:
        print("Masukkan angka valid!\n")
        return
    nilai_akhir = 0.4*tugas + 0.3*uts + 0.3*uas
    print(f"Nilai akhir kamu: {nilai_akhir:.2f}\n")

# ----------------------------
# 2. Konversi Nilai ke Grade
# ----------------------------
def konversi_grade():
    print("\n=== Konversi Grade ===")
    try:
        nilai = float(input("Masukkan nilai: "))
    except ValueError:
        print("Masukkan angka valid!\n")
        return
    if nilai >= 90: grade = "A"
    elif nilai >= 80: grade = "B"
    elif nilai >= 70: grade = "C"
    elif nilai >= 60: grade = "D"
    else: grade = "E"
    print("Grade:", grade, "\n")

# ----------------------------
# 3. Kelola Jadwal Pelajaran
# ----------------------------
FILE_JADWAL = "jadwal.json"
def kelola_jadwal():
    print("\n=== Jadwal Pelajaran ===")
    try:
        with open(FILE_JADWAL) as f:
            jadwal = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        jadwal = {}
    hari = input("Masukkan hari (Senin–Jumat): ")
    if hari not in jadwal or len(jadwal[hari]) == 0:
        print("Belum ada jadwal untuk hari ini.")
    else:
        print("Jadwal hari", hari + ":")
        for pel in jadwal[hari]:
            print("-", pel)
    tambah = input("Tambah pelajaran? (y/n): ")
    if tambah.lower() == "y":
        pel = input("Nama pelajaran: ")
        jadwal.setdefault(hari, []).append(pel)
        with open(FILE_JADWAL, "w") as f:
            json.dump(jadwal, f, indent=2)
        print("Pelajaran ditambahkan!\n")

# ----------------------------
# 4. Catatan Pelajaran
# ----------------------------
def catatan_pelajaran():
    print("\n=== Catatan Pelajaran ===")
    judul = input("Nama pelajaran: ")
    catatan = input("Masukkan catatan: ")
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("catatan_sekolah.txt", "a") as f:
        f.write(f"[{waktu}] {judul}: {catatan}\n")
    print("Catatan disimpan!\n")

# ----------------------------
# 5. Kalkulator Matematika
# ----------------------------
def kalkulator():
    print("\n=== Kalkulator ===")
    while True:
        print("\n1: Tambah\n2: Kurang\n3: Kali\n4: Bagi\n5: Pangkat\n6: Kembali")
        pilih = input("Pilih: ")
        if pilih == "6":
            break
        try:
            a = float(input("Angka 1: "))
            b = float(input("Angka 2: "))
        except ValueError:
            print("Masukkan angka valid!")
            continue
        if pilih == "1": print("Hasil:", a + b)
        elif pilih == "2": print("Hasil:", a - b)
        elif pilih == "3": print("Hasil:", a * b)
        elif pilih == "4":
            if b == 0: print("Tidak bisa dibagi 0!")
            else: print("Hasil:", a / b)
        elif pilih == "5": print("Hasil:", a ** b)
        else: print("Pilihan tidak valid.")

# ----------------------------
# 6. Pengacak Soal Latihan
# ----------------------------
def pengacak_soal():
    print("\n=== Pengacak Soal ===")
    soal = [
        "Apa itu fotosintesis?",
        "Jelaskan Hukum Newton I.",
        "Apa fungsi inti sel?",
        "Sebutkan 3 planet luar!",
        "Hitung luas lingkaran radius 7."
    ]
    random.shuffle(soal)
    for s in soal:
        input("\nTekan Enter untuk soal berikutnya...")
        print(s)
    print()

# ----------------------------
# 7. Hitung Rata-rata Kelas
# ----------------------------
def rata_kelas():
    print("\n=== Rata-rata Kelas ===")
    nilai = []
    print("Masukkan nilai siswa ('x' untuk selesai)")
    while True:
        n = input("> ")
        if n.lower() == "x": break
        try:
            nilai.append(float(n))
        except ValueError:
            print("Masukkan angka valid!")
    if len(nilai) == 0:
        print("Tidak ada nilai yang dimasukkan.\n")
    else:
        print("Rata-rata kelas:", sum(nilai) / len(nilai), "\n")

# ----------------------------
# 8. Buat Absen Siswa
# ----------------------------
def buat_absen():
    print("\n=== Buat Absen Siswa ===")
    try:
        jumlah = int(input("Jumlah siswa: "))
    except ValueError:
        print("Masukkan angka valid!\n")
        return
    siswa = []
    for i in range(jumlah):
        while True:
            nama = input(f"Nama siswa {i+1}: ").strip()
            if nama != "":
                siswa.append(nama)
                break
            else:
                print("Nama tidak boleh kosong!")
    with open("absen.txt", "w") as f:
        for i, nama in enumerate(siswa, 1):
            f.write(f"{i}. {nama}\n")
    print("Absen tersimpan sebagai absen.txt\n")

# ----------------------------
# 9. Soal Matematika Acak
# ----------------------------
def gen_soal_mtk():
    print("\n=== Soal Matematika Acak ===")
    ops = ["+", "-", "*", "//"]
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(ops)
    print(f"Soal: {a} {op} {b} = ?")
    try:
        jawab = float(input("Jawab: "))
    except ValueError:
        print("Input tidak valid!\n")
        return
    jawaban_benar = float(eval(f"{a} {op} {b}"))
    if jawab == jawaban_benar:
        print("Benar!\n")
    else:
        print("Salah! Jawaban benar:", jawaban_benar, "\n")

# ----------------------------
# 10. Stopwatch Praktikum
# ----------------------------
def stopwatch():
    print("\n=== Stopwatch ===")
    input("Tekan Enter untuk mulai... ")
    start = time.time()
    input("Tekan Enter untuk berhenti... ")
    end = time.time()
    print(f"Waktu terukur: {end - start:.2f} detik\n")

# ----------------------------
# 11. Hapus Data Tersimpan
# ----------------------------
def hapus_data():
    print("\n=== Hapus Data Tersimpan ===")
    files = {
        "1": ("jadwal.json", "Jadwal Pelajaran"),
        "2": ("catatan_sekolah.txt", "Catatan Pelajaran"),
        "3": ("absen.txt", "Daftar Absen")
    }
    print("Pilih data yang ingin dihapus:")
    print("1. Jadwal Pelajaran")
    print("2. Catatan Pelajaran")
    print("3. Absen Siswa")
    print("0. Kembali")
    pilihan = input("Pilih: ")
    if pilihan == "0": return
    if pilihan not in files:
        print("Pilihan tidak valid.\n")
        return
    filename, label = files[pilihan]
    if os.path.exists(filename):
        confirm = input(f"Yakin ingin menghapus {label}? (y/n): ")
        if confirm.lower() == "y":
            os.remove(filename)
            print(f"{label} berhasil dihapus!\n")
        else:
            print("Dibatalkan.\n")
    else:
        print(f"{label} belum ada / sudah terhapus.\n")

# ----------------------------
# 12. Kelola Absen Siswa
# ----------------------------
def kelola_absen():
    print("\n=== Kelola Absen Siswa ===")
    absen_file = "absen.txt"
    siswa = []
    if os.path.exists(absen_file):
        with open(absen_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and ". " in line:
                    parts = line.split(". ", 1)
                    if len(parts) == 2:
                        _, nama = parts
                        siswa.append(nama)
    while True:
        print("\nMenu Kelola Absen:")
        print("1. Lihat Absen")
        print("2. Tambah Siswa")
        print("3. Hapus Siswa")
        print("0. Kembali")
        pilihan = input("Pilih: ")
        if pilihan == "0": break
        elif pilihan == "1":
            if len(siswa) == 0:
                print("Absen masih kosong.")
            else:
                print("\nDaftar Absen:")
                for i, nama in enumerate(siswa, 1):
                    print(f"{i}. {nama}")
        elif pilihan == "2":
            while True:
                nama_baru = input("Masukkan nama siswa baru: ").strip()
                if nama_baru == "":
                    print("Nama tidak boleh kosong!")
                elif nama_baru in siswa:
                    print("Nama sudah ada di absen!")
                else:
                    siswa.append(nama_baru)
                    print(f"{nama_baru} berhasil ditambahkan.")
                    break
            with open(absen_file, "w") as f:
                for i, n in enumerate(siswa, 1):
                    f.write(f"{i}. {n}\n")
        elif pilihan == "3":
            if len(siswa) == 0:
                print("Absen kosong, tidak ada yang bisa dihapus.")
                continue
            try:
                idx = int(input("Masukkan nomor siswa yang ingin dihapus: "))
                if 1 <= idx <= len(siswa):
                    hapus_nama = siswa.pop(idx-1)
                    print(f"{hapus_nama} berhasil dihapus.")
                    with open(absen_file, "w") as f:
                        for i, n in enumerate(siswa, 1):
                            f.write(f"{i}. {n}\n")
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Masukkan angka valid.")
        else:
            print("Pilihan tidak valid.")

# ===================================================
#              MENU UTAMA / MAIN PROGRAM
# ===================================================
def main():
    while True:
        print("""
===============================
   APLIKASI SEKOLAH CLI
===============================
1. Hitung Nilai Akhir
2. Konversi Nilai ke Grade
3. Kelola Jadwal Pelajaran
4. Catatan Pelajaran
5. Kalkulator Matematika
6. Pengacak Soal Latihan
7. Hitung Rata-rata Kelas
8. Buat Absen Siswa
9. Soal Matematika Acak
10. Stopwatch
11. Hapus Data Tersimpan
12. Kelola Absen Siswa
0. Keluar
""")
        pilihan = input("Pilih menu: ")
        if pilihan == "1": hitung_nilai_akhir()
        elif pilihan == "2": konversi_grade()
        elif pilihan == "3": kelola_jadwal()
        elif pilihan == "4": catatan_pelajaran()
        elif pilihan == "5": kalkulator()
        elif pilihan == "6": pengacak_soal()
        elif pilihan == "7": rata_kelas()
        elif pilihan == "8": buat_absen()
        elif pilihan == "9": gen_soal_mtk()
        elif pilihan == "10": stopwatch()
        elif pilihan == "11": hapus_data()
        elif pilihan == "12": kelola_absen()
        elif pilihan == "0":
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()
