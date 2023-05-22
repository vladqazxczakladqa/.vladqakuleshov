def ask_riddles():
    riddles = [
        ("Висит груша, нельзя скушать. Что это?", "лампочка"),
        ("Что всегда перед нами, но мы его не видим?", "будущее"),
        ("Что может заполнить комнату, но не занимает места?", "свет")
    ]
 
    for i in range(len(riddles)):
        print("Загадка", i + 1, ":", riddles[i][0])
 
        while True:
            user_answer = input("Ваш ответ: ")
 
            if user_answer.lower() == riddles[i][1]:
                print("Правильно!")
                break
            else:
                print("Неправильно. Попробуйте ещё раз.")
 
ask_riddles()
 