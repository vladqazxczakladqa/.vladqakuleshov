a = int(input("Введите четырехзначное число "))

digit1 = a // 1000
digit2 = (a // 100) % 10
digit3 = (a // 10) % 10
digit4 = a % 10

digit_sum = digit1 + digit2 + digit3 + digit4
digit_product = digit1 * digit2 * digit3 * digit4

print("Сумма цифр: ", digit_sum)
print("Произведение цифр: ", digit_product)