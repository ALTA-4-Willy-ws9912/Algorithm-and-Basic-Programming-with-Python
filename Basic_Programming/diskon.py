harga_awal = float(370000.00)
diskon = float(15.0)

harga_diskon = diskon/100 * harga_awal

harga_akhir = harga_awal - harga_diskon

print(f"jadi harga yang harus dibayar oleh pembeli adalah {harga_akhir}")