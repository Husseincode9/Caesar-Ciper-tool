# I am using tkinter which is Python's built-in GUI framework
# This lets me create windows, buttons, labels, and text boxes
import tkinter as tk  

# I also need messagebox from tkinter so I can show error pop-ups
from tkinter import messagebox  

# ==================== Caesar Cipher Functions ====================

def caesar_encrypt(text, shift):
    """
    Encrypts text by shifting letters by the given shift value.
    """
    result = ""  # this will store the encrypted text
    for char in text:  # loop through each character
        if char.isalpha():  # only shift letters (ignore numbers, spaces, punctuation)
            base = ord('A') if char.isupper() else ord('a')  
            # work out the base code depending if it’s uppercase or lowercase
            result += chr((ord(char) - base + shift) % 26 + base)
            # shift the character and wrap around the alphabet using modulo
        else:
            result += char  # keep non-letters the same
    return result

def caesar_decrypt(cipher_text, shift):
    """
    Decrypts text by shifting letters in the opposite direction.
    """
    return caesar_encrypt(cipher_text, -shift)  
    # decryption is just encryption with a negative shift


# ==================== Button Functions ====================

def encrypt_text():
    """
    Runs when I press the Encrypt button.
    Gets the input text and shift, encrypts it, and shows the result.
    """
    try:
        shift = int(shift_entry.get())  # take the shift value from the entry box
        message = text_entry.get("1.0", tk.END).strip()  
        # get all the text I typed in the input box
        encrypted = caesar_encrypt(message, shift)  # call my encrypt function
        output_text.delete("1.0", tk.END)  # clear previous output
        output_text.insert(tk.END, encrypted)  # show the new encrypted text
    except ValueError:
        # if the user types something that isn’t an integer in shift box
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

def decrypt_text():
    """
    Runs when I press the Decrypt button.
    Gets the input text and shift, decrypts it, and shows the result.
    """
    try:
        shift = int(shift_entry.get())  # get the shift value
        cipher_text = text_entry.get("1.0", tk.END).strip()  # get the text from the box
        decrypted = caesar_decrypt(cipher_text, shift)  # call my decrypt function
        output_text.delete("1.0", tk.END)  # clear old result
        output_text.insert(tk.END, decrypted)  # show the decrypted text
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")


# ==================== GUI Layout ====================

root = tk.Tk()  # create the main window
root.title("Caesar Cipher Tool")  # set the title of the window

# label above the text box
tk.Label(root, text="Enter Text:").pack()

# text box where I type the message
text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

# label above the shift entry
tk.Label(root, text="Enter Shift Value:").pack()

# entry box where I type the shift number
shift_entry = tk.Entry(root)
shift_entry.pack()

# frame to hold the buttons next to each other
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# encrypt button
encrypt_button = tk.Button(button_frame, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=0, column=0, padx=5)

# decrypt button
decrypt_button = tk.Button(button_frame, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=0, column=1, padx=5)

# label above the output box
tk.Label(root, text="Result:").pack()

# text box where the result will be shown
output_text = tk.Text(root, height=5, width=50)
output_text.pack()

# keeps the window running until I close it
root.mainloop()
