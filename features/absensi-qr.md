---
layout: default
---

# EduCONNECT System

## 📷 Absensi Berbasis QR Code & Scanner Otomatis

Selamat tinggal absensi manual pemanggil nama satu per satu! Dengan teknologi QR Code EduConnect, proses presensi menjadi jauh lebih kilat dan terukur keakuratannya.

![QR Scanner Action](../assets/images/qr-scanner.png)
_(Gambar: Tampilan antarmuka Scanner QR di gerbang sekolah ketika siswa memindai kartu)_

## Bagaimana Cara Kerjanya?

Sistem EduConnect bekerja dalam 3 langkah sederhana yang revolusioner:

1. **Setiap Siswa Memiliki Kode Unik**  
   Ketika Admin mendaftarkan siswa ke dalam sistem, secara otomatis EduConnect akan membuatkan sebuah tiket/kartu yang memuat **QR Code** unik untuk masing-masing siswa. QR Code ini bisa dicetak di balik ID Card (kartu OSIS) siswa.
2. **Datang, Tunjukkan, Selesai**  
   Di pagi hari, siswa hanya perlu memposisikan ID Card mereka ke hadapan perangkat (Kamera Webcam / Scanner yang terhubung ke sistem). Dalam pecahan detik, sistem akan membaca dan memverifikasi wajah siswa atau kodenya.
3. **Konfirmasi Real-Time & Audio**  
   Sistem akan merespon pemindaian dengan antarmuka yang sangat jelas di layar monitor—menampilkan foto siswa dan tanda ceklis hijau. Tidak hanya itu, notifikasi suara akan memvalidasi bahwa "Siswa A berhasil Check-In", memastikan proses absensi dilakukan secara sah tanpa rekayasa.

## Mengapa Ini Luar Biasa Bagi Sekolah Anda?

- **Anti Antre Panjang:** Kapasitas pindai yang instan dapat memangkas waktu masuk kelas untuk sekolah dengan jumlah populasi ribuan siswa.
- **Teknologi Broadcasting (Reverb):** Menggunakan sokongan _WebSockets_ Laravel Reverb yang modern, seluruh log masuk siswa akan langsung terlihat di monitor ruangan Kepala Sekolah / Admin seketika saat kartu siswa berhasil memindai gerbang—tanpa perlu me-_refresh_ halaman komputer.

---

[⬅️ Kembali ke Halaman Utama](../index.html)
