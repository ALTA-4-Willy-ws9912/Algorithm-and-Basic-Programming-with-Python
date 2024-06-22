def is_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    
    if input_string == input_string[::-1]:
        return True
    else:
        return False

print(is_palindrome("katak")) # output data adalah true
print(is_palindrome("kupu-kupu")) # Output data adalah false
print(is_palindrome("civic")) # Output data adalah true
print(is_palindrome("kasur rusak")) # Output data adalah true
print(is_palindrome("lion")) # Output data adalah false
