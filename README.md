# Caesar Cipher Cryptography Demonstration Tool

## Overview

This project is a simple implementation of the Caesar Cipher,
which is one of the oldest and most basic techniques used in cryptography.

The tool can encrypt and decrypt messages using a shift key.
It also includes a brute-force mode to show how easily this cipher
can be broken by trying all possible keys.

---

## Features

- Caesar Cipher Encryption
- Caesar Cipher Decryption
- Step-by-step character transformation view
- Brute Force Attack (Cryptanalysis)
- Basic message statistics (letters, digits, spaces)
- Activity logging into a file
- Input validation for user safety

---

## Cybersecurity Concepts Demonstrated

### Classical Cryptography

The Caesar Cipher works by shifting each letter in the message
by a fixed number of positions in the alphabet.

### Cryptanalysis

A brute-force attack is used here to try all possible shift values
(1 to 25) to recover the original message.

### Logging / Audit Trail

All encryption and decryption activities are saved in a log file
so that the actions can be reviewed later.

### Input Validation

The program checks user inputs to make sure only valid numeric
shift values are accepted.

---

## Project Structure
