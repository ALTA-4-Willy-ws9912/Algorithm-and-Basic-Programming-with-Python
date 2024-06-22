def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def is_full_prime(number):
    number_str = str(number)
    
    if not is_prime(number):
        return False
    
    for digit in number_str:
        if not is_prime(int(digit)):
            return False
    
    return True

inputs = [2, 3, 11, 13, 23, 29, 37, 41, 43, 53]
for num in inputs:
    if is_full_prime(num):
        print(f"Input: {num}, Output: True")
    else:
        print(f"Input: {num}, Output: False")
