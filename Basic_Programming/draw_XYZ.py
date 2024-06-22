def drawXYZ(N):
    num = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1): 

            if num % 3 == 0:
                print("X", end=" ")
            elif num % 2 == 0:
                print("Z", end=" ")
            else:
                print("Y", end=" ")
            num += 1
        
        print()

# Contoh penggunaan
N = int(input("Masukkan nilai N: "))
drawXYZ(N)