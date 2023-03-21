import math
math.pi
a = float(input('Введите радиус круга:'))

b = float(input('Введите сторону квадрат:'))

if a**2*math.pi > b**2: print('Площадь круга больше')

elif math.pi*a**2 == b**2: print('Площади круга и квадрата равны')
 
else: print('Площадь квадрата больше')