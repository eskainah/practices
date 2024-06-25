import random

secret_num = random.randint(1,10) #generate random numbers
guess = int(input("Please enter your guess: "))

print(f"Secret number: {secret_num}")

match guess: 
    case _ if guess == secret_num:
        print('Congratulations, you guessed it!')
    case _ if guess > secret_num:
        print('Oops, your guess is a bit high. Try again!')
    case _ if guess < secret_num:
        print('Nope, your guess is a bit low. Give it another shot!')

