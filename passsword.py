import time
attempts = 0
while True:
    password = input("CAN I HACK YOU PASSWORD? GET ME YOUR PASSWORD:")
    if len(password) != 7:
        print("use only 7 numbers")
        continue
    if not password.isdigit():
        print("Password must contain ONLY digits!")
        continue
    break
start_time = time.time()
for i in range (10_000_000):
    attempts += 1
    try_password = str(i).zfill(7)
    if password == try_password:
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Your Password ({try_password}) \n"
        f" I used {attempts} attempts \n"
        f"Time spent {elapsed:.4f} seconds")
        break