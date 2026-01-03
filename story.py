game = True
name = input('Please Enter your name: ')
money = 0
print("Hello ",name," ,you have:",money,"$")
work = ["mine","curier","programer","trash","exit",[500, 200, 1000, 100, False]]
while game:
    nextw = input('Please Enter to be countiune')
    if nextw == "":
        print("Choose your work:", work[:-1])
        chose = input()
        print("your work is a ", chose)
        # ----- MINER -----
        if chose == work[0]:
            money += work[-1][0]
        # ----- CURIER -----
        elif chose == work[1]:
            money += work[-1][1]
        # ----- PROGRAMER -----
        elif chose == work[2]:
            money += work[-1][2]
        # ----- TRASH -----
        elif chose == work[3]:
            money += work[-1][3]
        # ----- EXIT -----
        elif chose == work[4]:
            game = work[-1][4]
    print("You have: ", money, "$")