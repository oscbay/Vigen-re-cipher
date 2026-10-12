print("=== Message Encoder ===")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose 1 or 2: ")
sentence = input("Enter your message: ")
key = input("Enter your passphrase: ")

# Keep only letters in the key
key = "".join(char.lower() for char in key if char.isalpha())

result = ""

if not key:
    print("Error: Passphrase must contain at least one letter.")

elif choice not in ("1", "2"):
    print("Invalid choice.")

else:
    for i, char in enumerate(sentence):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('a')

            if choice == "2":
                shift = -shift

            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char

    if choice == "1":
        print("Encrypted:", result)
    else:
        print("Decrypted:", result)
