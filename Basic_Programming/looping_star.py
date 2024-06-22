def cetak_segitiga(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print("", end=" ")
        for k in range(i):
            if k == i - 1:
                print("*")
            else:
                print("*", end=" ")

# Input jumlah baris segitiga
        
input_baris = int(5)

# Memanggil fungsi untuk mencetak segitiga
cetak_segitiga(input_baris)
