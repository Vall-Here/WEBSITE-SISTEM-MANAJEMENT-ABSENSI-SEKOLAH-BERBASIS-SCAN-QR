---
layout: default
---

# 🤖 Sistem Auto-Alpha & Manajemen Hari Libur

Menangani catatan administratif ribuan siswa setiap harinya adalah mimpi buruk bagi operator tata usaha (TU). Di sinilah EduConnect memisahkan diri sebagai solusi cerdas.

![Auto Alpha Configuration](../assets/images/auto-alpha-cron.png)
*(Gambar: Menu Manajemen Hari Libur dan pengaturan otomatisasi di EduConnect)*

## Pekerja Tak Kenal Lelah di Latar Belakang (Cron Job)

Bayangkan Anda memiliki asisten virtual yang bekerja otomatis di penghujung hari sekolah. EduConnect dirancang menggunakan arsitektur penjadwalan *Cron Job* dari Laravel.

Setiap hari secara berulang pada waktu yang Anda tetapkan, sistem akan "menyapu bersih" dan memindai *database* absensi keseluruhan.
Sistem kemudian secara otomatis mencari: **Siapa saja siswa yang pada hari tersebut belum memiliki riwayat rekaman absen, belum mengajukan Surat Izin, atau belum tercatat Sakit?**

Siswa yang memenuhi semua syarat "hilang" tersebut akan di-_stamp_ dengan status **Alpha (Tanpa Keterangan)** secara mandiri oleh aplikasi, tanpa membutuhkan klik atau persetujuan operator admin sedikitpun. Ini memastikan tingkat akurasi presensi yang tidak bisa dicurangi.

## Cerdas Mengenali Hari Libur & Tanggal Merah

Sistem Auto-Alpha yang buta tanggal libur justru dapat menimbulkan kegaduhan (misalnya ketika murid diliburkan tetapi malah diberikan Alpha massal). Fitur **Manajemen Hari Libur** menuntaskan masalah tersebut:

- **Mengenali Akhir Pekan:** Sistem secara standar bawaannya sudah menonaktifkan hukuman Alpha untuk hari Sabtu dan Minggu (Akhir pekan).
- **Customisasi Tanggal Merah:** Apabila ada perayaan Hari Kemerdekaan, Cuti Lebaran, maupun Hari Libur Semester, Admin TU dapat mendata blok tanggal tersebut pada modul "Hari Libur".
- **Otomatisasi Lanjutan:** Auto-Alpha sistem cukup cerdas mendeteksi tabel libur ini. Jika hari ini dinyatakan sebagai Libur Nasional, Cron Job secara terprogram akan mematikan mesinnya selama rentang waktu yang diatur. Siswa Anda akan terbebas dari ancaman poin pelanggaran Alpha.

---
[⬅️ Kembali ke Halaman Utama](../index.html)
