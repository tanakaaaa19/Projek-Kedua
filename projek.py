# Tampilkan judul program dengan pemisah garis
print("=" * 40)
print("Menghitung Indeks Massa Tubuh (BMI)")
print("=" * 40)

# Loop utama untuk memungkinkan pengguna melakukan perhitungan berulang kali
while True:
    # Input data personal dari pengguna
    nama = input("Masukkan nama: ")
    usia = int(input("Masukkan usia: "))
    golongan_darah = input("Masukkan golongan darah: ")
    agama = input("Masukkan agama: ")
    nik = input("Masukkan NIK: ")
    status = input("Masukkan status: ")
    
    # Input pengukuran fisik untuk menghitung BMI
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (m): "))

    # Rumus BMI: berat (kg) / tinggi (m) kuadrat
    bmi = berat / (tinggi ** 2)
    
    # Tampilkan hasil perhitungan BMI yang telah dibulatkan
    print("=" * 40)
    print("BMI Anda adalah:", round(bmi))
    print("=" * 40)

    # Tentukan kategori BMI berdasarkan nilai yang telah dihitung
    # Kategori Underweight: BMI kurang dari 18.5
    if bmi < 18.5:
        print("-" * 40)
        kategori = "Underweight"
        print("-" * 40)
        print(f"Kategori BMI Anda: {kategori}")
        print("-" * 40)
        # Tampilkan saran untuk meningkatkan berat badan
        print("Saran dan Tips:")
        print("• Pola Makan: Tingkatkan asupan kalori dengan makanan bergizi tinggi seperti kacang-kacangan, daging tanpa lemak, telur, dan produk susu.")
        print("• Olahraga: Lakukan latihan kekuatan (strength training) 3x seminggu untuk membangun otot.")
        print("• Aktivitas: Konsumsi makanan sehat 3-4 kali sehari dengan porsi yang cukup.")
        print("• Lainnya: Konsultasikan dengan ahli gizi untuk program penambahan berat badan yang tepat.")
        print("-" * 40)
    # Kategori Normal: BMI antara 18.5 sampai 25
    elif 18.5 <= bmi < 25:
        kategori = "Normal"
        print("-" * 40)
        print(f"Kategori BMI Anda: {kategori}")
        print("-" * 40)
        # Tampilkan saran untuk mempertahankan berat badan ideal
        print("Saran dan Tips:")
        print("• Pola Makan: Pertahankan pola makan seimbang dengan 5 porsi buah dan sayuran setiap hari.")
        print("• Olahraga: Lakukan aktivitas fisik minimal 150 menit per minggu (jogging, bersepeda, atau berenang).")
        print("• Aktivitas: Tingkatkan aktivitas sehari-hari seperti berjalan kaki atau menggunakan tangga.")
        print("• Lainnya: Hindari makanan cepat saji dan minuman berkalori tinggi.")
        print("-" * 40)
    # Kategori Overweight: BMI 25 atau lebih
    else:
        kategori = "Overweight"
        print("-" * 40)
        print(f"Kategori BMI Anda: {kategori}")
        print("-" * 40)
        # Tampilkan saran untuk menurunkan berat badan
        print("Saran dan Tips:")
        print("• Pola Makan: Kurangi asupan kalori, hindari makanan berlemak, dan perbanyak sayuran serta buah-buahan.")
        print("• Olahraga: Lakukan olahraga ringan seperti jalan cepat 30 menit setiap hari atau berenang.")
        print("• Aktivitas: Tingkatkan aktivitas fisik bertahap dan hindari gaya hidup sedentary.")
        print("• Lainnya: Konsultasikan dengan dokter atau ahli gizi untuk program penurunan berat badan yang aman.")
        print("-" * 40)

    # Tanyakan kepada pengguna apakah ingin menghitung BMI lagi
    pilihan = input("\nApakah Anda ingin menghitung BMI lagi? (ya/tidak): ").lower()
    
    # Jika pengguna tidak memilih "ya", keluar dari loop dan tampilkan pesan terima kasih
    if pilihan != "ya":
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
        break

