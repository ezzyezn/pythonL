import random

def startrnd():
    first_number = 0
    last_number = 100
    attempts = 0
    while True:
        gamemode = input("Choose gamemode 'you' or 'computer' think of number : ")
        if gamemode not in ("you", "computer"):
            print("Please write 'you' or 'computer'")
            continue
        else:
            break
        
    # ---------- YOU THINK OF NUMBER ----------

    if gamemode == "you":
        print("Think of number from 0 to 100")
        print("Use these symbols to answer: < > or =")
        while first_number <= last_number:
            attempts += 1
            computer_number = (first_number + last_number) // 2

            response = input(f"Your number: {computer_number}? - ")
            match response:
                case ">":
                    first_number = computer_number + 1
                case "<":
                    last_number = computer_number - 1
                case "=":
                    print("I guessed!")
                    print(f"Attempts were used: {attempts}")
                    break
                case _:
                    print("Use only < > or =")
                    attempts -= 1

    # ---------- COMPUTER THINKS OF NUMBER ----------

    elif gamemode == "computer":
        computer_guess_number = random.randint(0, 100)
        print("Computer thinks of number from 0 to 100")
        while True:
            attempts += 1
            guess = input("Your number: ")
            if not guess.isdigit():
                print("Please write a number")
                continue
            guess = int(guess)

            if guess < first_number or guess > last_number:
                print(f"Please write a number from {first_number} to {last_number}")
                continue

            if guess < computer_guess_number:
                print("Computer number is higher")
                first_number = guess + 1
            elif guess > computer_guess_number:
                print("Computer number is lower")
                last_number = guess - 1
            else:
                print("You guessed computer number")
                print(f"Attempts were used: {attempts}")
                break

#------------ MAIN ------------
while True:
    startrnd()
    again = input("Play again? (yes/no) : ")
    if again.lower() != "yes":
        break