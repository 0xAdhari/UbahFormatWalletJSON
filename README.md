# Wallet JSON Formatter

Skrip Python ini digunakan untuk mengonversi file JSON yang berisi daftar alamat, private key dan mnemonic ke dalam format yang dipilih pengguna. Output dapat disimpan dalam format JSON atau TXT.

## 📌 Fitur
- **Memilih format data output:**
  1. Address & PrivateKey
  2. Address saja
  3. PrivateKey saja
- **Memilih format file output:**
  - JSON (format array)
  - TXT (hanya menyimpan nilai utama per baris)

## 📂 Persyaratan
- Python 3.x
- Instal dependensi dari `requirements.txt`

## ⚙️ Instalasi
Pastikan Anda memiliki Python 3.x terinstal. Kemudian, instal library yang dibutuhkan dengan perintah berikut:
```bash
pip install -r requirements.txt
```

## 🚀 Cara Penggunaan
1. Jalankan skrip dengan perintah:
   ```bash
   python script.py
   ```
2. Pilih format data yang diinginkan.
3. Pilih format output (JSON atau TXT).
4. File hasil akan disimpan dengan nama sesuai pilihan:
   - `output_address_privatekey.json` atau `.txt`
   - `output_address.json` atau `.txt`
   - `output_privatekey.json` atau `.txt`

## 📜 Contoh Format File
### **Format input_file.json**
```json
[
    {
        "address": "************",
        "privateKey": "************",
        "mnemonic": "**** **** ****"
    },
    {
        "address": "************",
        "privateKey": "************",
        "mnemonic": "**** **** ****"
    }
]
```

### **Output JSON (jika memilih Address saja)**
```json
[
    {
        "address": "0x123456789"
    },
    {
        "address": "0x987654321"
    }
]
```

### **Output TXT (jika memilih Address saja)**
```
0x123456789
0x987654321
```

## ❗ Catatan
- Pastikan `input_file.json` memiliki format yang benar.
- Jika file input tidak ditemukan atau formatnya tidak valid, program akan menampilkan pesan kesalahan.

---
🛠️ Dibuat untuk mempermudah pengelolaan data JSON! 🚀

