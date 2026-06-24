import hashlib

print("--- Simple SHA-256 Hash Cracker ---")
user_pass = input("Enter a password to make its hash: ")

# converting password to bytes and then hashing it
pass_bytes = user_pass.encode("utf-8")
target_hash = hashlib.sha256(pass_bytes).hexdigest()

print("Your target hash is:", target_hash)
print("Starting the dictionary attack now...")

try:
    file = open("wordlist.txt", "r") # basic file opening
    
    attempt_count = 0
    password_found = False
    
    for line in file:
        current_word = line.strip()
        attempt_count = attempt_count + 1
        
        # making hash of the current word from our file
        word_bytes = current_word.encode("utf-8")
        word_hash = hashlib.sha256(word_bytes).hexdigest()
        
        # showing progress after every 5000 tries so screen doesn't hang
        if attempt_count % 5000 == 0:
            print("Still checking... tried", attempt_count, "words")
        
        # checking if we found the match
        if word_hash == target_hash:
            print("\nSuccess! Password found in the list.")
            print("Total tries:", attempt_count)
            print("The cracked password is:", current_word)
            password_found = True
            break
            
    file.close()
    
    if password_found == False:
        print("\nAttack finished. Password was not in the wordlist.")
        
except FileNotFoundError:
    print("Error: Could not find the wordlist.txt file. Please check the folder.")
