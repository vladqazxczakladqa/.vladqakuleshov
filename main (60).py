def ask_riddles():
    riddles = [
        ("Висит груша, нельзя скушать. Что это?", "лампочка"),
        ("Что всегда перед нами, но мы его не видим?", "будущее"),
        ("Что может заполнить комнату, но не занимает места?", "свет")
    ]
 
    max_attempts = 5  
 
    for i in range(len(riddles)):
        print("Загадка", i + 1, ":", riddles[i][0])
        attempts = 0
 
        while attempts < max_attempts:
            user_answer = input("Ваш ответ: ")
 
            if user_answer.lower() == riddles[i][1]:
                print("Правильно!")
                break
            else:
                attempts += 1
                remaining_attempts = max_attempts - attempts
                print("Неправильно. У вас осталось", remaining_attempts, "попыток.")
 
        if attempts == max_attempts:
            print("У вас закончились попытки. Правильный ответ:", riddles[i][1])
 
ask_riddles()