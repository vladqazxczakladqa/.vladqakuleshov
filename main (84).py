def find_largest_power(n):
    # находим максимально возможное значение для a
    max_a = int(math.sqrt(n)) + 1
    
    # перебираем все возможные значения для a и b
    largest_power = 0
    for a in range(max_a):
        for b in range(2, n):
            current_power = a**b
            if current_power < n and current_power > largest_power:
                largest_power = current_power
                
    return largest_po
