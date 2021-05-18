import sqlite3
import pandas as pd


# Read a csv file and return its contents as a pandas dataframe
def read_csv_file(filename):
    csv_file = pd.read_csv(filename)
    return csv_file


# Close a database connection
def close_connection(connect_db):
    connect_db.close()


# Open a database connection
def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except:
        print("Error opening the database")

    return connection


# Create the table for the database
def create_table(connect_db, db_name):
    try:
        cursor = connect_db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS """ + db_name + """ (
            Data text,
            PriceGeral text,
            PriceRegular text,
            PriceMidGrade text,
            PricePremium text,
            PriceDiesel text
            )""")
    except:
        print("Error creating Table")

    connect_db.commit()


# Insert the data obtained from the csv files to the database
def insert_data_on_database(connect_db, db_name, filename):
    cursor = connect_db.cursor()
    # Read the csv file and translate to a pandas dataframe, iterating over it's lines to insert them into the database
    df = read_csv_file(filename) 
    for _, row in df.iterrows():
        cursor.execute(
            'SELECT * FROM ' + db_name + ' WHERE Data=:Data AND PriceGeral=:PriceGeral AND PriceRegular=:PriceRegular AND PriceMidGrade=:PriceMidGrade AND PricePremium=:PricePremium AND PriceDiesel=:PriceDiesel',
            {'Data': row['Date'], 'PriceGeral': row['A1'], 'PriceRegular': row['R1'], 'PriceMidGrade': row['M1'], 'PricePremium': row['P1'], 'PriceDiesel': row['D1']})
        entry = cursor.fetchone()
        if entry is None:
            cursor.execute(
                "INSERT INTO " + db_name + " VALUES (:Data, :PriceGeral, :PriceRegular, :PriceMidGrade, :PricePremium, :PriceDiesel)",
                {'Data': row['Date'], 'PriceGeral': row['A1'], 'PriceRegular': row['R1'], 'PriceMidGrade': row['M1'], 'PricePremium': row['P1'], 'PriceDiesel': row['D1']})
        else:
            print("Key already in the table " + db_name)
    connect_db.commit()


# Insert the data obtained from the csv files to the database
def search_data_test(connect_db, db_name):
    cursor = connect_db.cursor()
    print("########### Test Query ###########")
    cursor.execute("SELECT * FROM " + db_name + " WHERE Data=:Data", {'Data': '02/13/1995'})
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceGeral=:PriceGeral", {'PriceGeral': '1.132'})
    print(cursor.fetchall())


# Make the query about the first data prices
def query1(connect_db, db_name):
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE Data=:Data", {'Data': '01/02/1995'})
    return cursor.fetchall()
