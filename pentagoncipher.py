# Pentagon Cipher - Stream Cipher that 
import string

# Generate Key
def generate_key(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = "".join(sorted(set(key.upper()), key=lambda x: key.index(x)))  
    key = key.replace("J","I")
    key_pentagon = []
    for char in key:
        if char not in key_pentagon and char in alphabet:
            key_pentagon.append(char)
    for char in alphabet:
        if char not in key_pentagon:
            key_pentagon.append(char)
    return [key_pentagon[i:i+5] for i in range(0, 25, 5)]

def encrypt(plain_text, key_pentagon):
    plain_text = plain_text.upper().replace("J", "I")
    cipher_text = ""
    for i, char in enumerate(plain_text):
        if char == " ":
            cipher_text += " "
            continue
        # Find position of char in key_pentagon
        found = False
        for row in range(5):
            for col in range(5):
                if key_pentagon[row][col] == char:
                    # Shift by (i + 1) for both row and col, modulo 5
                    shift_amount = i + 1
                    new_row = (row + shift_amount) % 5
                    new_col = (col + shift_amount) % 5
                    cipher_text += key_pentagon[new_row][new_col]
                    found = True
                    break
            if found:
                break
        if not found:
            # If char not in grid (shouldn't happen), just add as is
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key_pentagon):
    plain_text = ""
    for i, char in enumerate(cipher_text):
        if char == " ":
            plain_text += " "
            continue
        # Find position of char in key_pentagon
        found = False
        for row in range(5):
            for col in range(5):
                if key_pentagon[row][col] == char:
                    # Reverse shift: subtract (i + 1) for both row and col, modulo 5
                    shift_amount = i + 1
                    orig_row = (row - shift_amount) % 5
                    orig_col = (col - shift_amount) % 5
                    plain_text += key_pentagon[orig_row][orig_col]
                    found = True
                    break
            if found:
                break
        if not found:
            # If char not in grid (shouldn't happen), just add as is
            plain_text += char
    return plain_text

def main():
    key = input("Enter the key: ").upper()
    key_pentagon = generate_key(key)
    print("Key:", key)
    print("Key Pentagon:")
    for row in key_pentagon:
        print(' '.join(row))
    
    plain_text = input("Enter the plain text: ").upper()
    cipher = encrypt(plain_text, key_pentagon)
    print("Cipher text:", cipher)
    
    # Decrypt to verify
    decrypted = decrypt(cipher, key_pentagon)
    print("Decrypted text:", decrypted)

if __name__ == '__main__':
    main()
