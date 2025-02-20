# Oli Motor Management System

Sistem manajemen toko oli motor ini dirancang untuk mengelola data oli motor, termasuk melihat daftar oli, menambahkan, menghapus, memperbarui, dan melakukan sorting berdasarkan stok atau harga. Program ini memiliki fitur-fitur yang memudahkan admin dalam mengelola data oli.

## Fitur

### Submenu READ
- **Menampilkan Semua Daftar Oli**: Menampilkan semua data oli yang tersedia dalam bentuk tabel.
- **Mencari Oli Berdasarkan Unique ID**: Mencari oli berdasarkan kode unik yang dimasukkan oleh pengguna.
- **Urutkan Stok Oli**: Mengurutkan daftar oli berdasarkan stok (dari terendah ke tertinggi atau sebaliknya).
- **Urutkan Harga Oli**: Mengurutkan daftar oli berdasarkan harga (dari terendah ke tertinggi atau sebaliknya).

### Submenu CREATE
- **Menambah Data Oli**: Menambahkan data oli baru ke dalam daftar. Pengguna diminta untuk memasukkan nama oli, stok, harga, dan kategori oli (Sport/Reguler).

### Submenu DELETE
- **Menghapus Data Oli**: Menghapus data oli berdasarkan kode unik yang dimasukkan oleh pengguna.

### Submenu UPDATE
- **Mengubah Stok Oli**: Memperbarui stok oli berdasarkan kode unik yang dimasukkan oleh pengguna.
- **Mengubah Harga Oli**: Memperbarui harga oli berdasarkan kode unik yang dimasukkan oleh pengguna.

## Alur Program

### Menu Utama
1. **Menampilkan Daftar Oli**: Menampilkan semua data oli yang tersedia.
2. **Menambah Data Oli**: Menambahkan data oli baru ke dalam daftar.
3. **Menghapus Data Oli**: Menghapus data oli berdasarkan kode unik.
4. **Update Data Oli**: Memperbarui stok atau harga oli.
5. **Exit Program**: Keluar dari program.

### Submenu
- Setiap submenu memiliki opsi untuk kembali ke menu utama atau melanjutkan operasi lainnya.
- Setiap perubahan (tambah, hapus, update) memerlukan konfirmasi dari pengguna.

## Teknologi & Library

- **Python**: Bahasa pemrograman yang digunakan.
- **PrettyTable**: Library untuk menampilkan data dalam bentuk tabel.

## Cara Menjalankan

1. Pastikan Python sudah terinstal di sistem Anda.
2. Install library `PrettyTable` jika belum terinstal dengan perintah:
   ```bash
   pip install prettytable
