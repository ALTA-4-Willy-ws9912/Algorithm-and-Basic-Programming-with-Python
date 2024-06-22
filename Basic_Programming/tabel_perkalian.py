def tabel_perkalian(n):
    
    if n < 1 or n > 30:
        print("Masukkan bilangan antara 1 hingga 30.")
        return
    
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            
            print(f"{i * j:4}", end=" ")
        
        print()

n = int(9)
tabel_perkalian(n)