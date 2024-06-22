def ubah_huruf(sentence):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = "KLMNOPQRSTUVWXYZABCDEFGHIJ"
    
    enkripsi_map = {alphabet[i]: shifted_alphabet[i] for i in range(len(alphabet))}
    

    hasil = ""
    
    for char in sentence:
        if char in enkripsi_map:
            hasil += enkripsi_map[char]
        else:
            hasil += char
    
    return hasil

print(ubah_huruf("SEPULSA OKE"))  # outnya adalah COZEVCK YUO
print(ubah_huruf("ALTERRA ACADEMY"))  # outnya adalah KVDOBBK KMKNOWI
print(ubah_huruf("INDONESIA"))  # outnya adalah SXNYXOCSK
print(ubah_huruf("GOLANG"))  # outnya adalah QYVKXQ
print(ubah_huruf("PROGRAMMER"))  # outnya adalah ZBYQBKWWOB
