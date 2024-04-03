import random #importing the random module

secret_num = random.randint(1, 10) #generate random number

max_attempt = 3 #attempts allowed

def welcome_message(): #to display a welcome message
    print("\nWelcome to the Number Guessing Game!")
    print(f"You have {max_attempt} attempts to guess the correct number.")

#functin for recursive guessing
def guess_recursive(attempts_left):
    guess = int(input("\nGuess the number(from 1-10): "))

    if guess == secret_num: # guess check
        print("Congratulations! You guessed the correct number.")
    else: 
        print(f"Wrong guess. Attempts left: {attempts_left-1}")
        if attempts_left > 1: 
            guess_recursive(attempts_left -1)# make recursive call for another guess
        else:
            print(f"\nSorry, better luck next time. The correct guess was: {secret_num}")
# calling the functions
welcome_message()
guess_recursive(max_attempt)

#Using id to get memory address
print(f"Memory adress of Secret Number {secret_num} is: {id(secret_num)}")