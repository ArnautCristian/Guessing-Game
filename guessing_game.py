def play_guess():
    import random
    
    print("Welcome to the Guessing Game")
    print("Choose the level by typing the numbers 1, 2 or 3 for:")
    print("1. Easy: 1-100 with 6 attempts")
    print("2. Medium: 1-500 with 11 attempts")
    print("3. Hard: 1-1000 with 15 attempts")
    
    while True:
        try:
            level = int(input("Level: "))
            if level in[1, 2, 3]:
                levels = {
                    1: (100,7),
                    2: (500,11),
                    3: (1000,15)
                }
                n,a = levels[level]
                break
            else:
                print('Please type either "1" or "2" or "3" to select the level')
        except ValueError:
            print('Please type either "1" or "2" or "3" to select the level')
    random_number = random.randint(1,n)
    attempts = 0
    print(f"I'm thinking of a number between 1 and {n}")
    
    while attempts < a:
        try:
             guess = int(input("Type your guess here: "))
        except ValueError:
            print("Please type only integer numbers")
            continue
        attempts += 1
        
        if guess > random_number:
            print("You've guessed too high! Try again.")
            
        elif guess < random_number:
            print("You've guessed too low! Try again.")
        else:
            print(f"You guessed correctly! It took you {attempts} attempts")
            break
        if attempts == a and guess != random_number:
            print(f"You've run out of attempts :( The number was {random_number}")
        
while True:            
    play_guess()
    
    while True:
        replay = input("Would you like to play again? (yes/no): ")    
        
        if replay == "yes":
            break #breaks this loop so the first loop can start again
        elif replay == "no":
            print("Thanks for playing!")
            exit() #ends the entire program(the first while loop would continue without it)
        else:
            print('Please type either "yes" or "no"')
            
