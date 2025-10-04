# "Hello World" python program with a twist

import random
import sys
import time
import string

GREEN = "\033[97;42m"
RED = "\033[97;41m"
RESET = "\033[0m"

# characters to try while "brute forcing"
choices = string.ascii_letters + string.digits + string.punctuation + " "

# targets
target_correct = "Hello, world!" # the correct result we'll print after Enter
target_wrong = "world hello"     # the 'wrong' outcome we simulate first


# Simulate brute-force reveal of `target` by random guesses per position.
def reveal(target, max_speed=0.01, color=None):
    current = ""
    for char in target:
        while True:
            time.sleep(0.001)
            guess = random.choice(choices)
            
            print()
            print("\r" + current + guess, end='', flush=True)
        
            time.sleep(max_speed)
            time.sleep(0.001)
            if guess == char:
                current += char
                break
    if color:
        print("\r" + color + current + RESET, flush=True)
    else:
        print("\r" + current, flush=True)

def type_out(text, delay=0.06):
    """Typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():

    print()
    type_out("Running a \"hello world\" fun Python program...", delay=0.09)
    print()
    time.sleep(0.35)

    # 1) Dramatic reveal of wrong output
    reveal(target_wrong, max_speed=0.005, color=RED)
    print()
    time.sleep(0.35)

    # 2) Oops message
    print("Oops! I wrote the wrong Hello World program 😂")
    print()
    time.sleep(0.25)
    
    # 3) Fixing it...
    type_out("Let me fix it...")
    print()
    input()
    time.sleep(0.25)
    
    # 4) Dramatic reveal of correct output
    reveal(target_correct, max_speed=0.005, color=GREEN)
    print()
    time.sleep(0.18)
    
    # 5) Success message
    type_out("Cracked the \"hello world\" Python program. Now, I am Certified Pythonic... 😎", delay=0.09)
    print()

if __name__ == "__main__":
    main()
