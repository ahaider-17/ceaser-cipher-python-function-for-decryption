def decrypt(text, shift):
    if shift < 1 or shift > 35:
        return "Shift must be between 1 and 35."

    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    shifted_chars = chars[-shift:] + chars[:-shift]

    table = str.maketrans(
        chars + chars.upper(),
        shifted_chars + shifted_chars.upper()
    )

    return text.translate(table)


encrypted_text = input("Enter encrypted text: ")
shift = int(input("Enter key (1-35): "))

decrypted_text = decrypt(encrypted_text, shift)

print("\nDecrypted Text:", decrypted_text)
