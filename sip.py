class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.spp_terbayar = False
        self.nilai_akhir = None

    def bayar_spp(self):
        print(f"{self.nama} sedang membayar SPP...")
        self.spp_terbayar = True
        print("SPP berhasil dibayar.\n")

    def ikuti_perkuliahan(self):
        if not self.spp_terbayar:
            print("Silakan bayar SPP terlebih dahulu sebelum mengikuti perkuliahan.\n")
            return
        print(f"{self.nama} mengikuti perkuliahan.")
        print("Mengikuti kuliah, mengerjakan tugas, dan mengikuti ujian...\n")

    def berikan_nilai(self, nilai):
        if not self.spp_terbayar:
            print("Mahasiswa belum membayar SPP. Tidak dapat memberikan nilai.\n")
            return
        self.nilai_akhir = nilai
        print(f"Nilai akhir untuk {self.nama} ({self.nim}): {self.nilai_akhir}\n")

# Simulasi proses
mahasiswa1 = Mahasiswa("Andi", "123456")
print("Proses mengikuti kuliah di informatika:\n")

# Langkah-langkah
mahasiswa1.bayar_spp()          # Langkah 1: Bayar SPP
mahasiswa1.ikuti_perkuliahan()  # Langkah 2: Mengikuti perkuliahan
mahasiswa1.berikan_nilai(85)    # Langkah 3: Mendapatkan nilai akhir