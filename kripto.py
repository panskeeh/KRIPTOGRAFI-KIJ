def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(plain_text):
        shift = ord(key[i % key_length].lower()) - ord('a')
        encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        encrypted_text += encrypted_char
    
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(encrypted_text):
        shift = ord(key[i % key_length].lower()) - ord('a')
        decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
        decrypted_text += decrypted_char
    
    return decrypted_text

# Ambil input dari pengguna
key = input("Masukkan kunci (huruf saja): ").upper()
plain_text = input("Masukkan teks yang akan dienkripsi: ").lower()

encrypted_text = vigenere_encrypt(plain_text, key)
decrypted_text = vigenere_decrypt(encrypted_text, key)

print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
