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
        if chose == work[0]:
            print("your work is a ", chose)
            money += work[-1][0]
            print("You have: ", money, "$")
        elif chose == work[1]:
            print("your work is a ", chose)
            money += work[-1][1]
            print("You have: ", money, "$")
        elif chose == work[2]:
            print("your work is a ", chose)
            money += work[-1][2]
            print("You have: ", money, "$")
        elif chose == work[3]:
            print("your work is a ", chose)
            money += work[-1][3]
            print("You have: ", money, "$")
        elif chose == work[4]:
            game = work[-1][4]
