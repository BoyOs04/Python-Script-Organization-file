# Python File Organizer

Script Python sederhana untuk merapikan file secara otomatis berdasarkan ekstensi. Script memindai folder yang dipilih, menampilkan hasil pemindaian, lalu meminta konfirmasi sebelum memindahkan file.

## Fitur

- Membuat folder berdasarkan ekstensi, misalnya `PDF/`, `JPG/`, `MP4/`, dan `ZIP/`.
- File tanpa ekstensi dimasukkan ke folder `TANPA_EKSTENSI/`.
- Menampilkan daftar file yang akan dipindahkan sebelum tindakan dilakukan.
- Meminta konfirmasi pengguna sebelum memindahkan file.
- Mencegah file yang bernama sama tertimpa dengan menambahkan angka seperti `(1)`.
- Hanya memindai file yang berada langsung di folder target; tidak memindai subfolder.
- Mengabaikan file tersembunyi, symbolic link, dan file script `organize.py`.
- Menggunakan library bawaan Python; tidak perlu memasang package melalui `pip`.

## Persyaratan

- Python 3.8 atau lebih baru.
- Git untuk mengkloning repositori (opsional jika Anda mengunduh file ZIP).

## Instalasi

### Termux (Android)

Pasang Python dan Git:

```bash
pkg update
pkg install python git
termux-setup-storage
```

Kloning repositori:

```bash
git clone https://github.com/BoyOs04/Python-Script-Organization-file.git
cd Python-Script-Organization-file
```

### Linux

```bash
sudo apt update
sudo apt install python3 git
git clone https://github.com/BoyOs04/Python-Script-Organization-file.git
cd Python-Script-Organization-file
```

### Windows

1. Instal Python 3 dari [python.org](https://www.python.org/downloads/) dan aktifkan opsi **Add Python to PATH** saat instalasi.
2. Instal Git dari [git-scm.com](https://git-scm.com/downloads).
3. Buka Terminal, PowerShell, atau Command Prompt lalu jalankan:

```powershell
git clone https://github.com/BoyOs04/Python-Script-Organization-file.git
cd Python-Script-Organization-file
```

## Penggunaan

Berikan path folder yang ingin dirapikan sebagai argumen. Cara ini memungkinkan script tetap disimpan di folder repositori dan mengorganisasikan folder lain.

### Termux: merapikan folder Download

```bash
python organize.py "$HOME/storage/downloads"
```

### Linux: merapikan folder Downloads

```bash
python3 organize.py ~/Downloads
```

### Windows: merapikan folder Downloads

```powershell
python organize.py "$HOME\Downloads"
```

Anda juga bisa memasukkan path lengkap folder lain:

```bash
python organize.py "/path/ke/folder"
```

Jika argumen folder tidak diberikan, script akan memindai **folder kerja terminal saat ini**:

```bash
python organize.py
```

> **Penting:** Periksa path target sebelum menjalankan script. Jika argumen tidak diberikan saat Anda berada di folder repositori, file di folder repositori itulah yang akan dipindai.

## Contoh

Sebelum dijalankan:

```text
Download/
├── laporan.pdf
├── materi.pdf
├── foto.jpg
├── video.mp4
├── lagu.mp3
└── arsip.zip
```

Setelah Anda melihat daftar file dan memasukkan `y`:

```text
Download/
├── PDF/
│   ├── laporan.pdf
│   └── materi.pdf
├── JPG/
│   └── foto.jpg
├── MP4/
│   └── video.mp4
├── MP3/
│   └── lagu.mp3
└── ZIP/
    └── arsip.zip
```

Contoh konfirmasi di terminal:

```text
Move these files? [y/N]: y
```

Masukkan `y`, `yes`, atau `ya` untuk melanjutkan. Jawaban lain akan membatalkan proses tanpa memindahkan file.

## Keamanan dan perilaku

- Script hanya menangani file langsung di folder target, bukan file dalam subfolder.
- File tersembunyi (nama diawali titik) dan symbolic link dilewati.
- Folder kategori yang sudah ada akan digunakan kembali, tetapi isinya tidak dipindai ulang.
- Jika nama file tujuan sudah ada, script membuat nama alternatif seperti `laporan (1).pdf`; file tujuan yang sudah ada tidak ditimpa.
- Periksa hasil pemindaian sebelum menyetujui pemindahan.

## Lisensi

Belum ada lisensi yang ditetapkan. Hubungi pemilik repositori sebelum menggunakan atau mendistribusikan ulang kode jika Anda memerlukan ketentuan lisensi tertentu.
