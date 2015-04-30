def on_budget(books, budget):

    books = sorted(books)
    total_price = sum(books)

    result = {"books_on_budget": 0,
             "loan":0 }

    for book in books:
        if book <= budget:
            result["books_on_budget"] += 1
            budget = budget - book
            total_price -= book

        if result["loan"]  < 0:
            result["loan"] = 0
            

        
    result ["loan"] = total_price - budget

    print(budget)
    print(total_price)
    
    

    return result


books = [10, 20, 18]
budget = 10
print(on_budget(books,budget))
