# Computer_Security_Assignment_1
Stream Cipher - Playfair Cypher Encryption and Decryption code. 
Overview

The Pentagon Cipher is a custom encryption algorithm inspired by the geometric structure of a pentagon — consisting of five sides — and the 5×5 matrix concept used in classical ciphers like Playfair.
This project demonstrates the core principles of stream and block cipher encryption in a simple, educational, and Python-implemented way.

🧠 Concept

The cipher uses a 25-letter alphabet (combining I and J) to form a 5×5 key matrix generated from a user-defined key. Each plaintext letter is encrypted based on its matrix position and dynamically shifted according to its order in the message, simulating the behavior of a stream cipher.

For the block cipher implementation, the plaintext is divided into equal-sized segments, and each block is encrypted independently using substitution or permutation rules derived from the key.

⚙️ Workflow
Stream Cipher – Pentagon Cipher

Encryption Process
 Convert plaintext to uppercase and replace J with I.
 Generate the 5×5 key matrix using the given key.
 For each character in plaintext:
  Find its position (row, col) in the key matrix.
  Shift both row and column by (index + 1) using modulo 5.
  Replace with the letter at the new position.
Output the ciphertext.

Decryption Process
 Repeat the process in reverse: shift each character backward by (index + 1).

Visualization

Plaintext  →  Convert/Replace  →  Find (row,col)  →  Shift by (i+1)  →  Ciphertext
Ciphertext →  Reverse Shift    →  Locate in Grid  →  Recover Letter  →  Plaintext

💡 Justification of Design

5×5 Pentagon Matrix: Symbolically represents the cipher’s name and simplifies the alphabet structure.
Dynamic Shifting: Each character shifts differently, adding variety similar to stream ciphers.
Simplicity: Lightweight and easily understandable, suitable for educational use or constrained environments (IoT).
Key Dependence: Different keys generate unique grids, enhancing variability.

🧩 Proposed Usage
Stream Cipher
Application: Secure short messages or lightweight IoT communication.

Strengths:
Fast, simple, and memory-efficient.
Dynamically changing shifts make patterns less predictable.

Weaknesses:
Limited cryptographic strength.
Vulnerable to known-plaintext and frequency attacks if algorithm exposed.
Block Cipher (Optional Extension)

Application: Encrypting stored data or files where fixed-size blocks are preferred.

Strengths: Provides structure and improved diffusion.

Weaknesses: Requires padding and more computational overhead.

🧾 Example Execution
Enter the key: MOUSE RUN FAST
Key Matrix:
M O U S E
R N F A T
B C D G H
I K L P Q
V W X Y Z

Enter the plain text: MEET ME OUTSIDE
Cipher Text: TVQC WW TQGZZGI
Decrypted Text: MEET ME OUTSIDE

🧰 Technologies Used

Language: Python 3
Concepts: Cryptography fundamentals, matrix manipulation, modular arithmetic, stream cipher logic

📘 How to Run

Clone the repository or copy the Python script.
Run the script in your terminal:
python pentagon_cipher.py
Enter your secret key and plaintext when prompted.
View the generated cipher text and decrypted result.

📚 Educational Purpose

This cipher is not intended for real-world security use.
It serves as a conceptual and educational demonstration of:

How custom ciphers can be designed.

The core differences between stream and block encryption methods.

The role of keys, shifts, and matrix-based transformations in classical cryptography
