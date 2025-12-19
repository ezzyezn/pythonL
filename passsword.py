import random
guessed = False
attempts = 0
while True:
    password = input("CAN I HACK YOU PASSWORD? GET ME YOUR PASSWORD:")
    if len(password) != 4:
        print("use only 4 numbers")
        continue
    if not password.isdigit():
        print("Password must contain ONLY digits!")
        continue
    break
while not guessed:
    attempts += 1

    try_password = "".join(str(random.randint(0, 9)) for _ in range(4))
    print(try_password)
    if password == try_password:
        print(f"Your Password ({try_password}) \n I used {attempts} attempts")
        guessed = True