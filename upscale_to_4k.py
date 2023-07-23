from PIL import Image

# Mendapatkan input nama file gambar
filename = input("Masukkan nama file gambar (dengan ekstensi): ")

# Mendapatkan input lokasi dan nama file output
output_filename = input("Masukkan nama file output (dengan ekstensi): ")

# Membuka gambar menggunakan Pillow
image = Image.open(filename)

# Menghitung resolusi gambar asli
width, height = image.size

# Menghitung resolusi 4K (3840x2160)
new_width, new_height = 3840, 2160

# Menghitung faktor skala untuk upscaling
scale_factor = max(new_width / width, new_height / height)

# Menghitung ukuran gambar setelah di-upscale
upscaled_width = int(width * scale_factor)
upscaled_height = int(height * scale_factor)

# Melakukan upscaling gambar ke resolusi 4K
upscaled_image = image.resize((upscaled_width, upscaled_height), Image.LANCZOS)

# Membuat canvas kosong dengan ukuran 4K
canvas = Image.new("RGB", (new_width, new_height))

# Menghitung posisi gambar yang di-upscale di tengah canvas
offset_x = (new_width - upscaled_width) // 2
offset_y = (new_height - upscaled_height) // 2

# Menempatkan gambar di tengah canvas
canvas.paste(upscaled_image, (offset_x, offset_y))

# Simpan gambar hasil upscaling ke file output
canvas.save(output_filename)

print("Gambar berhasil di-upscale ke resolusi 4K.")
