# Secret Notes - Encrypted Note Taking Application

Secret Notes is a simple Python desktop application built with Tkinter that allows users to securely save and load encrypted text notes. It uses a password-based encoding scheme to protect your notes, storing each note as an encrypted file in a dedicated folder. This ensures your private information remains confidential and accessible only with the correct password.

## Features

- **User-friendly GUI:** A clean and simple interface to enter note titles, note text, and encryption passwords.
- **Password-based encryption:** Notes are encoded with a password you choose, using a custom encryption scheme combined with base64 encoding.
- **Separate storage per note:** Each note is saved as an individual encrypted file named after the note’s title (with special characters sanitized).
- **Encrypted notes folder:** All encrypted note files are saved in a dedicated `Encrypted_Notes` folder created automatically.
- **Load and decrypt:** Open any saved encrypted note by selecting the file and entering the correct password to decrypt and display the note content.
- **Input validation and error handling:** The app checks for empty inputs and handles decryption errors gracefully, displaying meaningful error messages.
- **Cross-platform:** Built with Python and Tkinter, it can run on Windows, macOS, and Linux with Python installed.

## How to Use

1. **Run the Application:**  
   Make sure you have Python 3 installed. Run the Python script to launch the GUI.

2. **Create and Save a Note:**  
   - Enter a title for your note in the "Enter Your Title" field.  
   - Write your note in the "Enter Your Text" area.  
   - Choose a password in the "Enter Your Key" field (this will be used to encrypt the note).  
   - Click **Save & Encrypt** to save the encrypted note. The note will be stored as a file inside the `Encrypted_Notes` folder.

3. **Load and Decrypt a Note:**  
   - Enter the password used to encrypt the note in the "Enter Your Key" field.  
   - Click **Load & Decrypt** and select the note file from the `Encrypted_Notes` folder.  
   - If the password is correct, the note’s decrypted content will appear along with the title.

## Important Notes

- The encryption method used is a custom simple scheme for educational and basic privacy purposes. It is **not recommended for securing highly sensitive data**. For stronger security, consider integrating cryptographic libraries such as `cryptography` and using standard encryption algorithms like AES.
- Keep your passwords secure and remember them! Without the correct password, notes cannot be decrypted.
- Filenames are sanitized to avoid invalid characters in file names. Titles with special characters are replaced by underscores `_`.

## Installation

No additional installation is required beyond having Python 3 and the standard libraries. Tkinter usually comes pre-installed with Python. If Tkinter is missing, install it via your system’s package manager.

## Dependencies

- Python 3.x
- Tkinter (usually included in Python)
- base64 (standard Python library)
- re, os (standard Python libraries)

## Project Structure

SecretNotes/
│
├── secret_notes.py # Main application script
├── Encrypted_Notes/ # Folder where encrypted notes are saved
│ ├── my_first_note.txt # Example encrypted note file
│ └── another_note.txt
└── README.md # This README file

## Future Improvements

- Replace the custom encryption with a secure, industry-standard encryption library such as `cryptography`.
- Add functionality to list all saved notes in the GUI with previews.
- Implement note editing and deletion capabilities.
- Support for exporting/importing encrypted notes.
- Password strength validation and password recovery options.
- Multi-user support with separate profiles.

## License

This project is open-source and free to use. Feel free to modify and distribute it as you wish.

---

If you want me to help you create this README as a file or add more sections like Contribution Guidelines or Installation Instructions, just ask!
