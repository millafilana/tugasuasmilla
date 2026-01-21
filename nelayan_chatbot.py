def jawab_pertanyaan(pertanyaan: str) -> str:
    t = pertanyaan.lower()

    if "cuaca" in t:
        return (
            "Cuaca laut hari ini diperkirakan berangin sedang dengan gelombang moderat. "
            "Suhu udara sekitar 28°C, kelembapan 75%, dan angin bertiup 5 m/s dari arah timur. "
            "Kondisi ini cukup aman untuk melaut, namun nelayan tetap harus waspada terhadap perubahan mendadak."
        )

    elif "januari" in t or "ikan" in t:
        return (
            "Pada bulan Januari, hasil tangkapan biasanya melimpah ikan pelagis kecil seperti tongkol, kembung, dan tembang. "
            "Selain itu, cakalang dan tuna kecil juga sering muncul, serta cumi-cumi di malam hari. "
            "Namun hasil tangkapan bisa berbeda tergantung arus laut dan kondisi cuaca."
        )

    elif "apd" in t or "alat pelindung diri" in t:
        return (
            "APD nelayan meliputi:\n"
            "- Life jacket (pelampung)\n"
            "- Sepatu/boot anti-slip\n"
            "- Sarung tangan tahan air\n"
            "- Lampu dan reflektor\n"
            "- Radio/HT dan peluit\n"
            "- Kotak P3K\n"
            "- Tabir surya dan kacamata polarized\n"
            "- Helm ringan bila perlu"
        )

    elif "perahu" in t or "kapal" in t:
        return (
            "Perahu yang cocok:\n"
            "- Pelagis kecil: perahu kayu/fiberglass 5–10 m, mesin 15–40 HP\n"
            "- Tuna/cakalang: perahu 8–12 m, mesin 40–90 HP, fish finder, GPS\n"
            "- Cumi-cumi: perahu 6–10 m dengan lampu kuat dan generator\n"
            "Semua perahu wajib punya navigasi dasar, palka es, APD, dan alat komunikasi."
        )

    elif "alat tangkap" in t or "jaring" in t or "pancing" in t:
        return (
            "Alat tangkap nelayan:\n"
            "- Jaring insang (gillnet)\n"
            "- Pukat cincin (purse seine)\n"
            "- Pancing ulur (handline)\n"
            "- Rawai (longline)\n"
            "- Bubu/perangkap\n"
            "Pemilihan alat harus sesuai regulasi agar ramah lingkungan."
        )

    elif "waktu" in t or "jadwal" in t:
        return (
            "Waktu terbaik melaut: pagi hingga siang saat angin tenang. "
            "Musim timur (Juni–Agustus) lebih bersahabat, musim barat (Desember–Februari) lebih berombak. "
            "Selalu cek prakiraan cuaca dan pasang surut sebelum berangkat."
        )

    elif "hasil tangkapan" in t or "penanganan" in t:
        return (
            "Penanganan hasil tangkapan:\n"
            "- Simpan ikan dalam kotak es/palka berinsulasi\n"
            "- Hindari sinar matahari langsung\n"
            "- Pisahkan ikan berdasarkan ukuran/jenis\n"
            "- Gunakan air laut dingin atau es curah\n"
            "Penanganan baik menjaga kualitas dan harga jual."
        )

    elif "komunikasi" in t or "radio" in t or "ht" in t:
        return (
            "Komunikasi nelayan:\n"
            "- Radio VHF/HT untuk koordinasi\n"
            "- Peluit/lampu sinyal untuk darurat\n"
            "- GPS dan peta digital untuk navigasi\n"
            "- Sediakan baterai cadangan atau generator\n"
            "Komunikasi yang baik meningkatkan keselamatan."
        )

    else:
        return (
            "Aku chatbot nelayan. Pertanyaan yang bisa kamu coba:\n"
            "- Cuaca laut hari ini\n"
            "- Jenis ikan bulan Januari\n"
            "- APD nelayan\n"
            "- Perahu yang cocok\n"
            "- Alat tangkap nelayan\n"
            "- Waktu terbaik melaut\n"
            "- Penanganan hasil tangkapan\n"
            "- Komunikasi nelayan"
        )


def main():
    print("Chatbot Nelayan siap. Ketik pertanyaanmu (Ctrl+C untuk keluar).")
    try:
        while True:
            q = input("> ")
            print(jawab_pertanyaan(q))
    except KeyboardInterrupt:
        print("\nSelesai.")


if __name__ == "__main__":
    main()