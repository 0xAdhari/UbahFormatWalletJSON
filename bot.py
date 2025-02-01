import json
import pyfiglet

# Menampilkan banner
banner = pyfiglet.figlet_format("Soto Mak Erot", font="slant")
print(banner)

# Menampilkan pilihan format data
print("Pilih format yang diinginkan:")
print("1. Address & PrivateKey")
print("2. Address saja")
print("3. PrivateKey saja")

# Mendapatkan input pilihan
choice = input("Masukkan pilihan (1/2/3): ")

# Membaca file JSON yang ada
input_file = 'input_file.json'

# Menentukan nama file output berdasarkan pilihan
if choice == '1':
    base_filename = 'output_address_privatekey'
elif choice == '2':
    base_filename = 'output_address'
elif choice == '3':
    base_filename = 'output_privatekey'
else:
    print("Pilihan tidak valid!")
    exit()

# Memilih format output
print("\nPilih format output:")
print("1. JSON")
print("2. TXT")

output_format = input("Masukkan pilihan format output (1/2): ")

if output_format == '1':
    output_file = f"{base_filename}.json"
elif output_format == '2':
    output_file = f"{base_filename}.txt"
else:
    print("Pilihan format output tidak valid!")
    exit()

try:
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Mengubah format data sesuai pilihan
    new_data = []
    for item in data:
        if choice == '1':
            new_data.append({
                "address": item["address"],
                "privateKey": item["privateKey"]
            })
        elif choice == '2':
            new_data.append({
                "address": item["address"]
            })
        elif choice == '3':
            new_data.append({
                "privateKey": item["privateKey"]
            })

    # Menyimpan ke dalam file sesuai format yang dipilih
    if output_format == '1':
        with open(output_file, 'w') as file:
            json.dump(new_data, file, indent=4)
    elif output_format == '2':
        with open(output_file, 'w') as file:
            for item in new_data:
                file.write(f"{list(item.values())[0]}\n")  # Menulis hanya value utama

    print(f"Format file berhasil diubah! Hasil disimpan di {output_file}")

except FileNotFoundError:
    print(f"File {input_file} tidak ditemukan!")
except json.JSONDecodeError:
    print(f"File {input_file} tidak dalam format JSON yang valid!")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")