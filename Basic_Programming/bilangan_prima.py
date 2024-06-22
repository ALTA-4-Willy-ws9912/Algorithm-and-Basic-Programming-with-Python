def is_prime(number):

    if number <= 1:
        return False
    
    if number <= 3:
        return True
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True

print(is_prime(7))  
print(is_prime(10)) 
