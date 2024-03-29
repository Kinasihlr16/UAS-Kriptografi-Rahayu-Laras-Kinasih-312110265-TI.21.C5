def otp_encrypt(plain_text, key):
    encrypted_text = ""

    for i in range(len(plain_text)):
        # Konversi karakter plaint text dan kunci ke nilai ASCII
        plain_char = ord(plain_text[i])
        key_char = ord(key[i % len(key)])

        # Enkripsi dengan XOR
        encrypted_char = plain_char ^ key_char

        # Konversi nilai ASCII kembali ke karakter
        encrypted_text += chr(encrypted_char)

    return encrypted_text

# Plaint text dan kunci
plain_text = "RUSDI"
key = "CRASH"

# Enkripsi menggunakan OTP
encrypted_text = otp_encrypt(plain_text, key)

# Tampilkan hasil enkripsi
print(f"Plaint text: {plain_text}")
print(f"Kunci: {key}")
print(f"Hasil Enkripsi: {encrypted_text}")

def otp_decrypt(encrypted_text, key):
    decrypted_text = ""

    for i in range(len(encrypted_text)):
        # Konversi karakter terenkripsi dan kunci ke nilai ASCII
        encrypted_char = ord(encrypted_text[i])
        key_char = ord(key[i % len(key)])

        # Deskripsi dengan XOR
        decrypted_char = encrypted_char ^ key_char

        # Konversi nilai ASCII kembali ke karakter
        decrypted_text += chr(decrypted_char)

    return decrypted_text

# Teks terenkripsi (gunakan hasil enkripsi sebelumnya)
# encrypted_text = "..."
# Kunci yang sama dengan saat enkripsi
# key = "CRASH"

# Deskripsi menggunakan OTP
decrypted_text = otp_decrypt(encrypted_text, key)

# Tampilkan hasil deskripsi
print(f"Hasil Deskripsi: {decrypted_text}")

#RAHAYU LARAS KINASIH 312110265