f = 0
l = 100
attempts = 0
print("Think of a number from 0 to 100")
print("Use these symbols to answer: < > or =")

while f <= l:
    attempts += 1
    computer_number = (f + l) // 2

    response = input(f"Your number: {computer_number}? - ")
    match response:
        case ">":
            f = computer_number + 1
        case "<":
            l = computer_number - 1
        case "=":
            print("I guessed!")
            print(f"Attempts were used: {attempts}")
            break
        case _:
            print("Use only < > or =")
            attempts -= 1
            continue
