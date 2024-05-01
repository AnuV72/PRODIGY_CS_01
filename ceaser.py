def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():  
            if encrypt:
                shifted = ord(char) + shift
            else:
                shifted = ord(char) - shift
            if char.islower():
                if encrypt:
                    if shifted > ord('z'):
                        shifted -= 26
                else:
                    if shifted < ord('a'):
                        shifted += 26
            elif char.isupper():
                if encrypt:
                    if shifted > ord('Z'):
                        shifted -= 26
                else:
                    if shifted < ord('A'):
                        shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (E/D): ").strip().upper()
        if choice == 'E':
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value for encryption: "))
            encrypted_text = caesar_cipher(text, shift)
            print("Encrypted text:", encrypted_text)
            break
        elif choice == 'D':
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value for decryption: "))
            decrypted_text = caesar_cipher(text, shift, encrypt=False)
            print("Decrypted text:", decrypted_text)
            break
        else:
            print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
