def on_budget(books, budget):
    b = budget
    result = {
        "books_on_budget": 0,
        "loan": 0
        }

    books = sorted(books)

    sum_books = sum(books)

    for book in books:
        if budget > 0:
            if book > budget:
                break
            budget -= book
            result["books_on_budget"] += 1

    if sum_books > b:
        result["loan"] = sum_books - b

    return result


books = [15, 20, 18]
budget = 25
print(on_budget(books,budget))
