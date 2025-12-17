#вывод текста в терминал/консоль
#print ("мне", 18, "лет", sep="-", end="=")
#print ("приветик \\ \"Luci\"", end="\n") 
#print ("5 + 5", 5 // 5, sep=" = ") простая математика
#print ("result:" , min(5, 6, 2, 7, 8, 0, -12)) функция берет минимальное число
#print ("result:" , max(5, 6, 2, 7, 8, 0, -12)) функция берет максимально число
#print ("result:" , abs(-6)) противоположность
#print ("result:" , pow(2, 2)) возношение в квадрат
#print ("result:" , round(5 / 3)) округление вперед

#получение текста от человека
#input()

# переменные
#number = 5 #{int}
#word = "result:"#{string}
#yupi = True #False #{bool}
#str_num = '5'
#print(word, number)
#print(number + int(str_num)) #перевод данных в int

#del number #удаление переменной 

#number = 8.98 #{float}
#print(word, number)
#print (word + str(number)) #перевод данных в string

#примеры переменных и получений данных + интерпретация
#x = int (input("podaj pierwsza liczbe: "))
#b = int (input("podaj druga liczbe: "))
#c =  x + b
#print("trwa dodawanie")
#print(c)

#операторы условные
#ser_data = int(input("Write numer: "))

#isHappy = True
#question = input("are you happy yes/no: ")
#if isHappy and question == "yes": #and - or
#    print("User is happy")
#elif question == "no":
#    print("User is unhappy")
#else:
#    print("User is crazy")

#if user_data > 5:
#    print("woow, is soo big")

###############
#data = input()
#number = 5 if data == "Five" else 0
#####
#if data == "Five":
#    number = 5
#else:
#    number = 0
#####
#print(number)
################

#циклы
#for i in range(1, 6 ,2):
#    print(i)

#count = 0
#word = "hello"
#for i in word:
#    if i == "l":
#        count += 1
#
#print ("count:", count)

#isHasCar = True

#while isHasCar:
#    if input("Enter your text: ") == "stop":
#        isHasCar = False

#for i in range(1, 11):
#    if i ==5:
#        break#
#
#    if i % 2 == 0:
#        continue
#    print(i)

#found = None

#for i in "hello":
#    if i =="r":
#        found = True
#        break
#else:
#    found = False
#print(found)

#списки
#nums = [5, 7, 2, 4, 7, True, "hello", 6.7, [5, 7]]
#nums[0] = 50
#nums[5] = 1
#print(nums[-1][1])

#numbers = [5,2,7]
#numbers.append(100) #добавление в конец
#numbers.insert(1, True) #добавление в это место
#numbers.extend([5,6,8]) #добавление несколько элементов на конец
#numbers.sort() #сортировка от меньшего к большому
#numbers.reverse() #листа перевернута
#numbers.pop() #удаление последнего
#numbers.remove(2) #удаление выбраного
#numbers.clear() #полностью очищает список
#print(numbers.count(5)) #считает сколько 5 в списке
#print(len(numbers)) #считает сколько элемментов в списке

#nums = [5,2,7,"50", False]

#for element in nums:
#    element *= 2
#    print(element)

#n = int(input("Enter lenght: "))
#user_list = []
#i = 0
#while i < n:
#    string = "Enter element #" + str(i + 1) + ": "
#    user_list.append(input(string))
#    i += 1
#print(user_list)

#Функции строк
word = "artemida,hello,boss"
#print (len((word))) #считает длину строки
#print (word.count('a')) #считает сколько тех или инних букв\символов
#rint (word.islower()) #проверят маленькие ли буквы\isuper большие ли буквы
#print (word.capitalize()) #делает первую заглавную большой
#print(word.find('m')) #показывает в каком месте находиться символ\буква
task = word.split(',')
 
for i in range(len(task)):
    task[i] = task[i].capitalize()

print(task)