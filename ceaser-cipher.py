def caesar_encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted = ord(char) + 3
            if is_upper:
                if shifted > ord('Z'):
                    shifted -= 26
            else:
                if shifted > ord('z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted = ord(char) - 3
            if is_upper:
                if shifted < ord('A'):
                    shifted += 26
            else:
                if shifted < ord('a'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if choice == 'e':
        text = input("Enter the text to encrypt: ")
        encrypted_text = caesar_encrypt(text)
        print("Encrypted text:", encrypted_text)
    elif choice == 'd':
        encrypted_text = input("Enter the text to decrypt: ")
        decrypted_text = caesar_decrypt(encrypted_text)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()
