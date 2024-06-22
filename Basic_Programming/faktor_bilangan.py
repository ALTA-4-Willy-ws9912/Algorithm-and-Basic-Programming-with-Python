# Input bilangan dari pengguna
bilangan = int(20)

# Menggunakan perulangan untuk mencetak faktor-faktor
print("Faktor dari", bilangan, "adalah:")
for i in range(1, bilangan + 1):
    if bilangan % i == 0:
        print(i)