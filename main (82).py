def get_total_cost(books):
    # определяем количество уникальных книг
    unique_books = set(books)
    num_unique_books = len(unique_books)
    
    # считаем количество копий каждой книги
    book_counts = {}
    for book in books:
        if book in book_counts:
            book_counts[book] += 1
        else:
            book_counts[book] = 1
    
    # считаем стоимость каждой книги без скидки
    base_price = 10
    
    # применяем скидки
    total_cost = 0
    if num_unique_books == 2:
        total_cost = base_price * num_unique_books * 0.95
    elif num_unique_books == 3:
        total_cost = base_price * num_unique_books * 0.9
    elif num_unique_books == 4:
        total_cost = base_price * num_unique_books * 0.8
    else:
        # если заказ только на одну книгу или все книги разные
        for book in book_counts:
            total_cost += base_price * book_counts[book]
    
    return int(total_cost)