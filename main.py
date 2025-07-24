from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import base64
import os
import re


# Creating Window
window = Tk()
window.title('Secret Notes')
window.minsize(400,700)

# Adding Image & Image Label
image = PhotoImage(file="secret2.png")
image_label = Label(image=image)
image_label.pack()

# Creating Title Label & Entry
title = Label(window, text="Enter Your Title")
title.pack()
title = Entry(window)
title.pack()

# Creating Text Label & Entry
text_label = Label(window,text="Enter Your Text")
text_label.pack()
text = Text(window,width=30, height=15)
text.pack()

# Creating Master Key Label & Entry
key_label = Label(window, text="Enter Your Key")
key_label.pack()
key_entry = Entry(window,show="*")
key_entry.pack()

# Creating Directory for Encrypted Notes
secret_folder = "Encrypted_Notes"
os.makedirs(secret_folder, exist_ok=True)

# Simple function to sanitize the title for use as a filename:
def safe_filename(title):
    # Keep only letters, numbers, dashes, and underscores; remove others
    return re.sub(r'[^a-zA-Z0-9_-]', '_', title) + ".txt"

# Creating Encode and Decode Functions
def Encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def Save_and_Encode_Note():
    title_text = title.get().strip()
    text_text = text.get("1.0", END).strip()
    key_text = key_entry.get()

    if not title_text or not text_text or not key_text:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    # Encryption process (using the example simple Encode function)
    message_encrypted = Encode(key_text, text_text)

    # Folder and filename
    filename = safe_filename(title_text)
    file_path = os.path.join(secret_folder, filename)

    try:
        with open(file_path, "w") as file:
            file.write(message_encrypted)
        messagebox.showinfo("Success", f"Note saved as:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save note:\n{e}")

    # Clear the input fields
    title.delete(0, END)
    text.delete("1.0", END)
    key_entry.delete(0, END)

def Load_and_Decode_Note():
    key_text = key_entry.get()
    if not key_text:
        messagebox.showerror("Error", "Please enter the password.")
        return

    file_path = filedialog.askopenfilename(initialdir=secret_folder, title="Select Note File",
                                           filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    try:
        with open(file_path, "r") as file:
            message_encrypted = file.read()
        decrypted_message = Decode(key_text, message_encrypted)
        # You can get the title from the filename or ask separately
        title_name = os.path.splitext(os.path.basename(file_path))[0]
        title.delete(0, END)
        title.insert(0, title_name)
        text.delete("1.0", END)
        text.insert(END, decrypted_message)
        messagebox.showinfo("Success", "Note decrypted and loaded.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not decrypt or load note:\n{e}")

# Creating Encrypt and Decrypt Buttons

encrypt_button = Button(window, text="Save & Encrypt", command=Save_and_Encode_Note)
encrypt_button.pack()
load_button = Button(window, text="Load & Decrypt", command=Load_and_Decode_Note)
load_button.pack()


# Keep Alive Window
window.mainloop()
