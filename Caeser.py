def caesar_encrypt(text, shift):  # Define a function to encrypt text using Caesar cipher with a given shift.
    result = ""  # Initialize an empty string to store the encrypted result.
    for char in text:  # Loop through each character in the input text.
        if char.isalpha():  # Check if the character is a letter.
            base = ord('A') if char.isupper() else ord('a')  # Determine the ASCII base depending on case.
            result += chr((ord(char) - base + shift) % 26 + base)  # Shift character and append to result.
        else:
            result += char  # If not a letter, leave it unchanged and append it as-is.
    return result  # Return the final encrypted string.

def caesar_decrypt(cipher_text, shift):  # Define a function to decrypt text using Caesar cipher.
    return caesar_encrypt(cipher_text, -shift)  # Decryption is just encryption with the negative shift.

def main():  # Define the main function to run the encryption/decryption tool.
    print("=== Caesar Cipher Tool ===")  # Display the tool's title.
    while True:  # Start an infinite loop to continually prompt the user.
        choice = input("\nChoose an option:\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter choice: ")  # Menu prompt.

        if choice == '1':  # If user chooses to encrypt
            message = input("Enter a message to encrypt: ")  # Prompt for the message.
            shift = int(input("Enter shift value: "))  # Prompt for the shift value and convert to integer.
            encrypted = caesar_encrypt(message, shift)  # Encrypt the message using the Caesar cipher.
            print("Encrypted message:", encrypted)  # Print the encrypted message.

        elif choice == '2':  # If user chooses to decrypt
            cipher_text = input("Enter a message to decrypt: ")  # Prompt for the encrypted message.
            shift = int(input("Enter shift value: "))  # Prompt for the shift used in encryption.
            decrypted = caesar_decrypt(cipher_text, shift)  # Decrypt the message.
            print("Decrypted message:", decrypted)  # Print the decrypted message.

        elif choice == '3':  # If user chooses to exit
            print("Exiting...")  # Print exit message.
            break  # Break the loop to exit the program.
        else:
            print("Invalid choice. Please select 1, 2, or 3.")  # Handle invalid input.

if __name__ == "__main__":  # Ensure the script runs only when executed directly.
    main()  # Call the main function to start the program.