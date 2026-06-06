from cipher_engine import *

# ======================================================
# Caesar Cipher Cryptography Demonstration Tool
#
# Features:
# - Encryption
# - Decryption
# - Brute Force Attack (cryptanalysis)
# - Logging activity
# - Basic message statistics
# ======================================================


def banner():

    # just prints the project title in ASCII art form
    print(r"""
   _____                            _____ _       _
  / ____|                          / ____(_)     | |
 | |     __ _  ___  ___  __ _ _ __| |     _ _ __ | |__   ___ _ __
 | |    / _` |/ _ \/ __|/ _` | '__| |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |  | |____| | |_) | | | |  __/ |
  \_____\__,_|\___||___/\__,_|_|   \_____|_| .__/|_| |_|\___|_|
                                           | |
                                           |_|

        Cybersecurity Mini Project
    """)

    print("=" * 60)


def menu():

    # simple menu shown every time in the loop
    print("\nChoose an Operation")
    print("-" * 30)

    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Brute Force Attack")
    print("4. Exit")


def get_shift():
    """
    Takes shift value from user and makes sure it's valid.
    Keeps asking until correct input is given.
    """

    while True:

        try:
            shift = int(input("\nEnter shift value (1-25): "))
            return shift

        except ValueError:
            print("[!] Invalid input. Please enter numbers only.")


def display_statistics(message):

    # shows simple stats about the message
    stats = message_statistics(message)

    print("\n[+] Message Analysis")
    print("-" * 30)

    print(f"Characters : {stats['characters']}")
    print(f"Letters    : {stats['letters']}")
    print(f"Digits     : {stats['digits']}")
    print(f"Spaces     : {stats['spaces']}")


# start of program
banner()

while True:

    menu()

    choice = input("\nEnter choice: ")

    if choice == "1":

        print("\n[Encryption Mode]")

        message = input("Enter plaintext message: ")

        shift = get_shift()

        result = caesar_cipher(
            message,
            shift,
            "encrypt",
            show_steps=True
        )

        animated_output(result)

        display_statistics(message)

        save_log("encrypt", message, result)

        print("\n[+] Saved to cipher_history.txt")


    elif choice == "2":

        print("\n[Decryption Mode]")

        message = input("Enter ciphertext message: ")

        shift = get_shift()

        result = caesar_cipher(
            message,
            shift,
            "decrypt",
            show_steps=True
        )

        animated_output(result)

        display_statistics(message)

        save_log("decrypt", message, result)

        print("\n[+] Saved to cipher_history.txt")


    elif choice == "3":

        print("\n[Cryptanalysis Mode]")

        ciphertext = input("Enter encrypted text: ")

        # tries all shifts from 1 to 25
        brute_force_attack(ciphertext)


    elif choice == "4":

        print("\nExiting Caesar Cipher Tool...")
        print("Goodbye.")
        break


    else:

        print("\n[!] Invalid option, try again.")
