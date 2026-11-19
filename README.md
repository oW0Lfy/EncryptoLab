# EncryptoLab
This is a fun project made to explore Cryptography. It was originally made in 2024. It has a lot of room for improvement and actually make it a full application. It is currently on stand-by. No changes were made since then, and was made for fun. It has no automatic file creation. There are many things left undone. This project is presented as a demonstration of my knowledge and practical understanding of Python programming, cryptography, file handling, and basic authentication mechanisms. No AI was used for the creation of this program.

# 🔐 Python File Encryption & Decryption Tool

A command-line application developed in Python that allows users to securely encrypt and decrypt files using **Fernet symmetric encryption**. The program includes a password-based authentication mechanism, encryption key generation, and file validation.

## 📌 Project Overview

This project demonstrates the practical implementation of cryptography in Python. It provides users with the ability to protect files through encryption and restore them using the corresponding secret key.

The application uses the Fernet implementation provided by the Python `cryptography` library, which combines symmetric encryption with authentication to protect data against unauthorized modification.

## ✨ Features

- **File Encryption:** Encrypts files using Fernet symmetric encryption.
- **File Decryption:** Restores encrypted files using the correct encryption key.
- **Automatic Key Generation:** Generates a unique encryption key for each encryption operation.
- **Authentication:** Requires password verification before accessing the application.
- **Login Attempt Limitation:** Terminates the application after four unsuccessful authentication attempts.
- **File Validation:** Checks whether the specified file and encryption key paths exist.
- **Custom File Naming:** Allows users to specify output filenames and file extensions.
- **Command-Line Interface:** Provides a simple interactive menu for selecting operations.

## 🛠️ Technologies & Libraries

| Technology            | Purpose |
|---|---|
| Python 3              | Main programming language |
| Cryptography (Fernet) | Symmetric file encryption and decryption |
| Hashlib               | SHA-512 password hashing |
| OS                    | Operating system commands and file handling |
| Time                  | Application delays and interface control |
| Base64                | Imported for encoding-related operations |

## 📁 Project Structure

The application expects the following directory structure:

```text
Project/
│
├── main.py
│
├── Key/
│   └── Generated encryption keys
│
├── Encrypted/
│   └── Encrypted files
│
└── DecryptResult/
    └── Decrypted files
```

**Note:** The three directories must be created manually before running the application.

## 🔧 Future Improvements

Although the application provides basic file encryption and decryption functionality, several improvements could enhance its security, usability, and overall reliability.

Potential future improvements include:

- **Automatic Directory Creation:** Implement automatic creation of the required directories (`Key/`, `Encrypted/`, and `DecryptResult/`) to simplify the initial setup.
- **Improved Password Security:** Replace direct SHA-512 hashing with a dedicated password-hashing algorithm such as Argon2id or PBKDF2.
- **Secure Key Storage:** Introduce encrypted key storage to reduce the risk of unauthorized access to generated encryption keys.
- **Graphical User Interface (GUI):** Develop a graphical interface to make the application more user-friendly and accessible.
- **Multiple File Support:** Allow users to encrypt and decrypt multiple files in a single operation.
- **File Integrity Verification:** Introduce additional verification mechanisms to ensure that decrypted files match the original data.
- **Improved Error Handling:** Replace broad exception handling with specific exceptions to provide clearer error messages and prevent unexpected application termination.
- **Cross-Platform Compatibility:** Improve terminal handling to ensure consistent operation across Windows, Linux, and macOS.
- **Logging System:** Implement application logging to record important events, errors, and operations without exposing sensitive information.
- **Improved Authentication:** Introduce a more secure authentication mechanism with configurable credentials and better protection against unauthorized access.

These improvements could transform the current application into a more reliable, secure, and feature-rich file encryption tool.
