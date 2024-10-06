def encrypt(message, shift_value):
    encrypted_message = ""
    for character in message:
        if character.isupper():
            new_char = chr((ord(character) - ord('A') + shift_value) % 26 + ord('A'))
            encrypted_message += new_char
        elif character.islower():
            new_char = chr((ord(character) - ord('a') + shift_value) % 26 + ord('a'))
            encrypted_message += new_char
        else:
            encrypted_message += character
    return encrypted_message


def decrypt(message, shift_value):
    return encrypt(message, -shift_value)


def get_valid_shift():
    while True:
        try:
            shift_value = int(input("Enter shift value (positive or negative): "))
            return shift_value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("Welcome to Caesar Cipher!")
    while True:
        operation = input("Do you want to encrypt or decrypt? ").lower()
        if operation not in ["encrypt", "decrypt"]:
            print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
            continue

        message = input("Enter your message: ")
        shift_value = get_valid_shift()

        if operation == "encrypt":
            print(f"Encrypted Message: {encrypt(message, shift_value)}")
        elif operation == "decrypt":
            print(f"Decrypted Message: {decrypt(message, shift_value)}")

        another_operation = input("Do you want to perform another operation? (yes/no): ").lower()
        if another_operation != 'yes':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
