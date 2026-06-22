# SHA256 Hash Auditor

> A memory-efficient Python utility for evaluating SHA-256 cryptographic hashes via dynamic stream-processed dictionary attacks.

## Overview
SHA256 Hash Auditor is a lightweight, strictly terminal-based cryptographic utility developed in Python. It is designed to perform dictionary-based brute-force attacks against target SHA-256 hashes. The tool emphasizes memory efficiency and I/O optimization, making it capable of processing massive datasets (e.g., RockYou.txt) without causing system bottlenecking or memory overflow.

## Core Features
* **Memory-Safe Execution:** Utilizes dynamic stream processing (`for line in file:`) to read datasets line-by-line, ensuring the system RAM remains stable regardless of the wordlist size.
* **I/O Throttling:** Implements a custom modulus-based terminal refresh mechanism (updating stdout every 10,000 iterations). This prevents the CLI from bottlenecking CPU cycles, maintaining maximum cryptographic evaluation speed.
* **Fault Tolerance:** Includes bypass logic (`errors="ignore"`) to silently skip malformed bytes or non-UTF-8 characters commonly found in large, raw data dumps.
* **No Dependencies:** Built entirely using Python's standard libraries (`hashlib`, `time`). No external modules or packages are required.

## Prerequisites
* Python 3.x installed on your local machine.
* A target SHA-256 hash string.
* A wordlist/dictionary text file (e.g., `wordlist.txt`) placed in the root execution directory.

## Usage

1. Clone the repository to your local machine:
```bash
   git clone [https://github.com/YourUsername/SHA256-Hash-Auditor.git](https://github.com/YourUsername/SHA256-Hash-Auditor.git)
   ```

2. Navigate to the directory:
```bash
   cd SHA256-Hash-Auditor
   ```

3. Ensure your dictionary file is named `wordlist.txt` and is present in the same directory as the script.

4. Execute the script:
```bash
   python main.py
   ```

5. When prompted, enter the plaintext target to generate its hash, and the tool will automatically commence the dictionary evaluation against the dataset.

## Logic Blueprint
The script operates on the following workflow:
1. Captures target data and generates the baseline SHA-256 hash.
2. Opens the specified dataset using a secure context manager.
3. Iterates through the file sequentially, generating a fresh SHA-256 hash for each parsed line.
4. Evaluates the generated hash against the baseline target.
5. Halts execution immediately upon a successful cryptographic match or gracefully exits upon reaching EOF (End of File).

## Disclaimer
This script is developed strictly for educational purposes, cryptographic research, and authorized security auditing. The author is not responsible for any misuse or illegal activities conducted with this tool. Always ensure you have explicit permission before testing against infrastructure or data that you do not own.

## Author
**Muhammad Kaif Shahani**
