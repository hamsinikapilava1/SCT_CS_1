# Caesar Cipher Cryptography Demonstration Tool

## Overview

This project is a simple implementation of the Caesar Cipher,
which is one of the oldest and most basic techniques used in cryptography.

The tool supports both encryption and decryption of messages using a shift key.
It also includes a brute-force mode to demonstrate how weak classical ciphers
can be broken by trying all possible keys.

---

## Features

- Caesar Cipher Encryption
- Caesar Cipher Decryption
- Step-by-step character transformation visualization
- Brute Force Cryptanalysis (tries all 1–25 shifts)
- Message statistics (letters, digits, spaces, etc.)
- Activity logging to file
- Input validation for safe execution

---

## Cybersecurity Concepts Demonstrated

### Classical Cryptography

The Caesar Cipher works by shifting each letter in the message
by a fixed number of positions in the alphabet.

### Cryptanalysis

A brute-force attack is implemented to try all possible shift values
(1 to 25) to recover the original plaintext from ciphertext.

### Logging / Audit Trail

All encryption and decryption activities are saved in a log file
(`cipher_history.txt`) for tracking and analysis.

### Input Validation

User inputs are validated to ensure only correct numeric shift values
are accepted, preventing runtime errors.

---

## Project Structure
