"""
Caesar Cipher Cryptography Demonstration Tool
Cybersecurity Mini Project

This module has the main crypto functions:
- Encryption
- Decryption
- Message Analysis
- Brute Force Attack demo

Author: Hamsini
"""

import time


def caesar_cipher(text, shift, mode, show_steps=False):
    """
    This function does Caesar Cipher encryption or decryption.

    Args:
        text (str): the message we input
        shift (int): key for shifting letters
        mode (str): encrypt or decrypt
        show_steps (bool): shows each letter change if True

    Returns:
        str: final converted message
    """

    shift = shift % 26  # keep shift within alphabet range
    result = ""

    if show_steps:
        print("\n[+] Character Transformations")
        print("-" * 35)

    for char in text:

        if char.isalpha():  # only change letters

            base = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 26 + base)

            if show_steps:
                print(f"{char}  -->  {new_char}")

            result += new_char

        else:
            # keep spaces, numbers, symbols same
            result += char

    return result


def message_statistics(text):
    """
    Just counts basic stuff in the message like letters, digits, etc.
    """

    return {
        "characters": len(text),
        "letters": sum(c.isalpha() for c in text),
        "digits": sum(c.isdigit() for c in text),
        "spaces": text.count(" ")
    }


def brute_force_attack(ciphertext):
    """
    Trying all possible shifts (1 to 25) to break the cipher.
    """

    print("\n[+] Brute Force Results")
    print("-" * 40)

    for shift in range(1, 26):

        plaintext = caesar_cipher(ciphertext, shift, "decrypt")

        print(f"Shift {shift:2}: {plaintext}")


def animated_output(text):
    """
    Prints output slowly so it looks cool/animated.
    """

    print("\n[+] Result: ", end="")

    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)

    print()


def save_log(mode, original, result):
    """
    Saves encryption/decryption history into a file
    so we can check it later.
    """

    with open("cipher_history.txt", "a") as file:
        file.write(f"{mode.upper()} | {original} -> {result}\n")
