import pandas as pd


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


# Read a csv file and return its contents as a pandas dataframe
def read_csv_file(filename):
    csv_file = pd.read_csv(filename)
    return csv_file


# Guarantee that the name passed is a valid name to the database
def scrub(db_name):
    return ''.join(c for c in db_name if c.isalnum())
