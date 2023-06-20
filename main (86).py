def next_number(n):
    # Функция, которая возвращает следующее число в последовательности
    s = str(n)
    return sum([int(c)**2 for c in s])

a0 = int(input("Введите первый элемент последовательности: "))
sequence = [a0]  # Список для хранения последовательности
length = 1  # Начальная длина последовательности - 1

while True:
    next_num = next_number(sequence[-1])  # Вычисляем следующее число в последовательности
    if next_num in sequence:  # Если это число уже встречалось ранее, то выходим из цикла
        break
    else:
        sequence.append(next_num)
        length += 1
        
print("Длина последовательности:", length)