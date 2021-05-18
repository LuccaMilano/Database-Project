

# Get the most expensive fuel on a set date
def get_most_expensive(prices):
    dict_prices = {'Regular': float(prices[2]), 'MidGrade':float(prices[3]), 'Premium':float(prices[4]), 'Diesel': float(prices[5])}
    
    most_expensive_price = 0.0
    most_expensive_fuel = ''
    for fuel, price in dict_prices.items():
        if price >= most_expensive_price:
            most_expensive_price = price
            most_expensive_fuel = fuel

    return most_expensive_fuel, most_expensive_price
