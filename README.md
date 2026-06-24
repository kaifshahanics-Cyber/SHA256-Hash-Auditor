# Simple SHA-256 Hash Cracker

Hello! I am a second year Computer Science student deeply passionate about cybersecurity and ethical hacking. This repository contains one of my first practical security projects. 

Instead of using automated tools, I built this simple dictionary attack simulator to understand how password auditing works under the hood. My main focus was to write clean, understandable logic and learn how to handle files safely in Python.

## 🛠️ What I Learned Building This

* **Safe File Handling:** I learned how to use `open()` and `close()` properly, and how to read a large text file line by line without crashing the computer's memory.
* **Error Prevention:** I added basic `try...except` blocks. If the user forgets to add the `wordlist.txt` file, the program gives a polite error message instead of throwing a massive system error.
* **Basic Cryptography:** I learned how to convert regular text into byte format (`.encode()`) and hash it using Python's native `hashlib` library.
* **Progress Tracking:** I used a simple mathematical modulo (`%`) logic to print a "still checking" message every 5,000 tries, so the user knows the program is not frozen.

## 🚀 How to Run It

1. Make sure you have Python installed on your computer.
2. Create a plain text file named `wordlist.txt` in the same folder as the script and put some guess words in it.
3. Open your terminal or command prompt and run:
```bash
   python hasher_cracker.py
