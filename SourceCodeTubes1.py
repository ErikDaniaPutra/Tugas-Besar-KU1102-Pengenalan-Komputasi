# Judul: Program Lampu Penyebrangan
# Deskripsi: Membuat program yang dapat menyimulasikan sistem kerja dari lampu penyebrangan
# Dibuat oleh: Kelompok 1 KU-22

# KAMUS 
# list_pemilik_kartu = array [0,1000] of integer 
# i, waktu_A, waktu_B, kepadatan, kartu, detik, countdown = integer
# time = float function 
# random = integer function 
# kondisi_A, kondisi_B, masukan_awal = string
# nilai = boolean

# ALGORITMA
list_pemilik_kartu = [0 for i in range (1000)]

for i in range (0,1000):
  list_pemilik_kartu[i] = 165000 + (i+1)

import time
import random 

kepadatan = random.randint(0, 100)

def waktu_A(kepadatan): 
    if kepadatan >= 70:
        waktu_A = 20 
    elif 70 > kepadatan > 40: 
        waktu_A = 25
    else: 
        waktu_A = 30
    return waktu_A 

def kondisi_A(kepadatan): 
    if kepadatan >= 70:
        kondisi_A = "Jalanan sedang macet"
    elif 70 > kepadatan > 40: 
        kondisi_A = "Jalanan sedang padat merayap"
    else: 
        kondisi_A = "Jalanan sedang lancar"
    return kondisi_A

def waktu_B(kepadatan): 
    if kepadatan >= 70:
        waktu_B = 40
    elif 70 > kepadatan > 40: 
        waktu_B = 50
    else: 
        waktu_B = 60
    return waktu_B 

def kondisi_B(kepadatan): 
    if kepadatan >= 70:
        kondisi_B = "Jalanan sedang macet"
    elif 70 > kepadatan > 40: 
        kondisi_B = "Jalanan sedang padat merayap"
    else: 
        kondisi_B = "Jalanan sedang lancar"
    return kondisi_B

print("Anda sedang berada di depan lampu penyeberangan yang menggunakan teknologi Adaptive Traffic Management System. \n")
time.sleep(0.5)
print("Apakah Anda ingin menekan tombol lampu penyeberangan? \n")
time.sleep(1)
print("A = Iya, tekan tombolnya.")
print("B = Iya, tekan sekaligus gesek kartu, karena saya termasuk golongan lansia.")
print("C = Tidak, saya tidak ingin menekan tombol. \n")
masukan_awal = input("Apa yang akan Anda pilih? Masukkan huruf A / B / C : ")

if masukan_awal != "A" and masukan_awal != "B" and masukan_awal != "C":
  print("")
  while masukan_awal != "A" and masukan_awal != "B" and masukan_awal != "C":
    masukan_awal = input("Huruf yang Anda masukkan salah, pilih huruf A / B / C: ")
print("")
if masukan_awal == "A": 
    time.sleep(0.5)
    print("Kepadatan lalu lintas saat ini adalah " + str(kepadatan) + "%")
    time.sleep(0.5)
    print(kondisi_B(kepadatan))
    time.sleep(0.5)
    print("\nWaktu menyeberang adalah " + str(waktu_A(kepadatan)) + " detik\n")
    time.sleep(1)
    detik = 0
    countdown = waktu_A(kepadatan)
    for i in range(1,9):
      print("Merah")
      time.sleep(1)
    while detik < waktu_A(kepadatan):
        if detik< waktu_A(kepadatan) - 3:
            print("Hijau (" + str(countdown) + ")")
            countdown -= 1
            time.sleep(1)
        else: 
            print("Kuning (" + str(countdown) + ")")
            countdown -= 1
            time.sleep(1)
        detik += 1

elif masukan_awal == "B":
    try: 
      kartu = int(input("Masukkan nomor kartu penyeberangan Anda (165*** dengan 3 digit terakhir sebagai kode unik): \n\n"))
      nilai = False
      i = 0

      while nilai == False and i < 1000:
        if kartu == list_pemilik_kartu[i]:
          nilai = True
        else:
          nilai = False
        i += 1

      if nilai == True:
        time.sleep(0.5)
        print("\nKepadatan lalu lintas saat ini adalah " + str(kepadatan) + "%")
        time.sleep(0.5)
        print(kondisi_B(kepadatan))
        time.sleep(0.5)
        print("\nWaktu menyeberang adalah " + str(waktu_B(kepadatan)) + " detik\n")
        time.sleep(1)
        detik = 0
        countdown = waktu_B(kepadatan)
        for i in range (1, 9): 
          print("Merah")
          time.sleep(1)
        while detik < waktu_B(kepadatan):
            if detik< waktu_B(kepadatan) - 3:
                print("Hijau (" + str(countdown) + ")")
                countdown -= 1
                time.sleep(1)
            else: 
                print("Kuning (" + str(countdown) + ")")
                countdown -= 1
                time.sleep(1)
            detik += 1
      else:
          time.sleep(1)
          print("\nKartu Anda tidak terdaftar dalam sistem.")
    except ValueError: 
      time.sleep(1)
      print("\nAnda menggunakan kartu yang salah.")

elif masukan_awal == "C": 
    print("Hati-hati saat menyeberang. Selamat jalan.")