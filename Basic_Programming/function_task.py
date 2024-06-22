def hitung_pangkat(x, n):
    # Base case
    if n == 0:
        return 1
    elif n == 1:
        return x
    
    # Recursive case
    if n % 2 == 0:
        half_power = hitung_pangkat(x, n // 2)
        return half_power * half_power
    else:
        half_power = hitung_pangkat(x, (n - 1) // 2)
        return x * half_power * half_power

# Contoh penggunaan
print(hitung_pangkat(2, 3)) # Output nya adalah 8
print(hitung_pangkat(7, 2)) # Output nya adalah 49
print(hitung_pangkat(5, 3)) # Output nya adalah125
print(hitung_pangkat(10, 2)) # Output nya adalah 100
print(hitung_pangkat(2, 5)) # Output nya adalah 32
print(hitung_pangkat(7, 3)) # Output nya adalah 343