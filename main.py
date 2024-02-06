U = int(input("Введите число:"))
if U % 2 == 0 or U % 3 == 0:
    print('Число А кратно 2 или 3')

hour = int(input("Введите число:"))
if hour >= 6 and hour < 12:
    print("Утро!!!")
if 6 <= hour < 12:  #а можно ещё проще
    print("Утро!!!")

a = int(input())
if a == 10:
    print('a равно 10')
elif a < 10:  #elif переводится как "а если"
    print('a меньше 10')
else:
    print('a больше 10')

month = int(input())
if month in [3, 4, 5]:
    print("Весна")
elif month in [6, 7, 8]:
    print("Лето")
elif month in [9, 10, 11]:
    print("Осень")
elif month in [12, 1, 2]:
    print("Зима")


def get_wind_class(speed): #объявление функции
    if 1 <= speed <= 4: #только аргумент
        return "weak [1]" #Тут вместо print("что-то там") пишем return"Чё-то там" Всё это из-за функции
    elif 5 <= speed <= 10:
        return "moderate [2]"
    elif 11 <= speed <= 18:
        return"strong [3]"
    elif speed >= 19:
        return "hurricane [4]"
print(get_wind_class(3)) #мы просим программу напечатать то, что в скобках


g = 42
h = 41
if g > h:
    result = g
else:
    result = h
result = g if g > h else h #Можно намного короче

#Задача чтоб только одно число было меньше 45
A = int(input('Введите первое число\n'))
B = int(input('Введите второе число\n'))
C = int(input('Введите третье число\n'))

if ((A < 45) and (B >= 45) and (C >=45)) or \
    ((A >= 45) and (B < 45) and (C >=45)) or \
    ((A >= 45) and (B >= 45) and (C < 45)):
    print('Есть число меньше 45 и только одно')
else:
    print('Числа меньше 45 нет или их несколько')

K = int(input('Введите число\n'))
if not (-10 <= K <= -1 or 2 <= K <= 15):
    print("Число не принадлежит интервалу")
else:
    print("Число принадлежит интервалу")

list_ = [-5, 2, 4, 8, 12, -7, 5]
print(len(list_) == len(set(list_))) #проверяем все ли элементы в списке уникальные

num = 12345678 #проверить читается ли число одинаково сначала до конца и с конца в начало
print(str(num) == str(num)[::-1])