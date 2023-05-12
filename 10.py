import math

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
h = float(input("Введите значение шага h: "))
if a >= b or h <= 0:
    print("Вы ошиблись в вводе")
else:
    print(" x | y ")
    print("---|---")
    for x in range(int(a*100), int(b*100)+1, int(h*100)):
        x = x / 100
        y = math.sqrt(x)
        print("{:.1f}|{:.2f}".format(x, y)) 
