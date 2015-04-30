def calculate_coins(sum):
    result = {}
    coins = [100, 50, 20, 10, 5, 2,1]
             
    sum = round(sum * 100)
    
    
    for coin in coins:
        times_to_pay = sum // coin

        result[coin] = times_to_pay

        sum -= times_to_pay * coin

    return result

print(calculate_coins(8.94) == { 1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2 })
print(calculate_coins(0.53) == { 1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0 })
