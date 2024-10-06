

---

# Caesar Cipher Tool

This is a simple Python-based tool for performing **Caesar Cipher** encryption and decryption. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted by a certain number of positions in the alphabet.

## Features
- Encrypts messages using a shift value.
- Decrypts messages using the reverse of the provided shift value.
- Handles both uppercase and lowercase letters, and retains non-alphabetic characters like spaces and punctuation unchanged.
- Input validation for shift values.

## How It Works
The tool asks for user input to either encrypt or decrypt a message using a Caesar Cipher. The shift value can be positive (shifts to the right) or negative (shifts to the left). The program supports looping functionality, allowing the user to perform multiple operations without restarting the program.

## Usage

### Prerequisites
Make sure you have **Python 3** installed. You can verify the installation by running:

```bash
python --version
```

### Running the Program
1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/caesar-cipher-tool.git
```

2. Navigate to the cloned directory:

```bash
cd caesar-cipher-tool
```

3. Run the Python script:

```bash
python caesar_cipher.py
```

### Example Usage
Once the program is running, you can choose to encrypt or decrypt a message by providing a shift value.

#### Encrypting
```bash
Do you want to encrypt or decrypt? encrypt
Enter your message: Hello World
Enter shift value (positive or negative): 3
Encrypted Message: Khoor Zruog
```

#### Decrypting
```bash
Do you want to encrypt or decrypt? decrypt
Enter your message: Khoor Zruog
Enter shift value (positive or negative): 3
Decrypted Message: Hello World
```

## Code Structure

- **`encrypt(message, shift_value)`**: Encrypts the given message using the specified shift value.
- **`decrypt(message, shift_value)`**: Decrypts the given message by shifting it in reverse.
- **`get_valid_shift()`**: Ensures that the user enters a valid integer shift value.
- **`main()`**: Main loop to handle user input for encryption or decryption.

## Contributing
Feel free to submit issues and pull requests if you'd like to contribute to the project!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

