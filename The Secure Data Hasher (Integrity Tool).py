import hashlib
import time

# Generate the baseline SHA-256 target hash from user input
target_password = input("Enter a password to generate its target hash: ")
encoded_target = target_password.encode("utf-8")
target_hash = hashlib.sha256(encoded_target).hexdigest()

print(f"\n[*] Target SHA-256 Hash: {target_hash}")
print("[*] Initiating dictionary attack sequence...\n")

try:
    # Context manager for memory-efficient I/O; ignores malformed bytes in large datasets
    with open("wordlist.txt", "r", encoding="utf-8", errors="ignore") as file:
        print("[*] Dataset loaded into buffer. Commencing brute force...\n")
        
        attempt_counter = 0 
        
        for line in file:
            guess = line.strip() 
            attempt_counter += 1
            
            # Dynamic stream throttling: updates CLI every 10,000 iterations to prevent I/O bottlenecks
            if attempt_counter % 10000 == 0:
                print(f"\r[*] Iterations: {attempt_counter:,} | Evaluating: {guess[:12]:<12}", end="")
            
            # Cryptographic transformation and state evaluation
            encoded_guess = guess.encode("utf-8")
            guess_hash = hashlib.sha256(encoded_guess).hexdigest()

            if guess_hash == target_hash:
                print("\n\n[+] CRYPTOGRAPHIC MATCH FOUND")
                print(f"[+] Total attempts evaluated: {attempt_counter:,}")
                print(f"[+] Decrypted plaintext: {guess}\n")
                break
        else:
            print("\n\n[-] ATTACK COMPLETE")
            print("[-] Dataset exhausted. Target hash remains unbroken.")

except FileNotFoundError:
    print("\n[!] CRITICAL ERROR: 'wordlist.txt' missing from the execution directory.")