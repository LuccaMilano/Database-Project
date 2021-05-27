import sqlite3
import pandas as pd
import utilities


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
            PriceGeral real,
            PriceRegular real,
            PriceMidGrade real,
            PricePremium real,
            PriceDiesel real
            )""")
    except:
        print("Error creating Table")

    connect_db.commit()


# Insert the data obtained from the csv files to the database
def insert_data_on_database(connect_db, db_name, filename):
    cursor = connect_db.cursor()
    # Read the csv file and translate to a pandas dataframe, iterating over it's lines to insert them into the database
    df = utilities.read_csv_file(filename) 
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
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceGeral=:PriceGeral", {'PriceGeral': 1.132})
    print(cursor.fetchall())


# Make the query about the first data prices
def query1(connect_db, db_name):
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE Data=:Data", {'Data': '01/02/1995'})
    return cursor.fetchall()


# Make the query about the first data prices
def query2(connect_db, db_name):
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE Data=:Data", {'Data': '01/25/2021'})
    return cursor.fetchall()


# Make the query about the date when the average fuel was the most expensive
def query3(connect_db, db_name):
    cursor = connect_db.cursor()
    cursor.execute("SELECT max(PriceGeral) FROM " + db_name)
    last = cursor.fetchone()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceGeral =" + str(last[0]))
    last_date = cursor.fetchone()
    return last_date


# Make the query about the date when each fuel passed a determined value
def query4(connect_db, db_name, compared_value):
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceRegular >" + str(compared_value))
    regulargrade = cursor.fetchone()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceMidGrade >" + str(compared_value))
    midgrade = cursor.fetchone()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PricePremium >" + str(compared_value))
    premiumgrade = cursor.fetchone()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceDiesel >" + str(compared_value))
    diesel = cursor.fetchone()
    return regulargrade, midgrade, premiumgrade, diesel


# Make the query about the last date when each fuel went below a determined value
def query5(connect_db, db_name, compared_value):
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceRegular <" + str(compared_value))
    regulargrade = cursor.fetchall()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceMidGrade <" + str(compared_value))
    midgrade = cursor.fetchall()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PricePremium <" + str(compared_value))
    premiumgrade = cursor.fetchall()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceDiesel <" + str(compared_value))
    diesel = cursor.fetchall()
    return regulargrade[-1], midgrade[-1], premiumgrade[-1], diesel[-1]


# Make the query about the date when the regular fuel surpassed diesel
def query6(connect_db, db_name):
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceRegular > PriceDiesel")
    result = cursor.fetchone()
    return result


# Make the query about the date when disel surpassed premium fuel
def query7(connect_db, db_name):
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceDiesel > PricePremium")
    result = cursor.fetchone()
    return result


# Make the query to know if regular fuel surpassed midgrade fuel one day
def query8(connect_db, db_name):
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceRegular > PriceMidGrade")
    result = cursor.fetchone()
    return result


# Make the query to know if midgrade fuel surpassed premium fuel one day
def query9(connect_db, db_name):
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceMidGrade > PricePremium")
    result = cursor.fetchone()
    return result


# Make the query about the the most expensive fuel on a given date
def query10(connect_db, db_name, date):
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE Data=:Data", {'Data': date})
    return cursor.fetchall()


# Make the query about plot of all fuel prices
def adv_query1(connect_db, db_name):
    x_value = []
    y_value = [[] for _ in range(5)]

    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name)
    all_values = cursor.fetchall()

    for value in all_values:
        x_value.append(value[0])
        y_value[0].append(value[1])
        y_value[1].append(value[2])
        y_value[2].append(value[3])
        y_value[3].append(value[4])
        y_value[4].append(value[5])

    return x_value, y_value


# Make the query about the prices of all grades fuel that are below a certain value
def adv_query2(connect_db, db_name, compared_value):
    x_value = []
    y_value = []
    
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceGeral <" + str(compared_value))
    allgrades = cursor.fetchall()

    for value in allgrades:
        x_value.append(value[0])
        y_value.append(value[1])

    return x_value, y_value


# Make the query about plotting the highest value achieved by each fuels
def adv_query3(connect_db, db_name):
    axis_value = [[] for _ in range(6)]
    max_values_axis = [[] for _ in range(6)]
    date_values = [[] for _ in range(5)]
    
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name)
    all_values = cursor.fetchall()

    for value in all_values:
        axis_value[0].append(value[0])
        axis_value[1].append(value[1])
        axis_value[2].append(value[2])
        axis_value[3].append(value[3])
        axis_value[4].append(value[4])
        axis_value[5].append(value[5])

    # Find the max value and its surroundings
    # Max of All Grades
    max_value = max(axis_value[1])
    max_index = axis_value[1].index(max_value)

    for i in range(max_index - 5, max_index + 6):
        max_values_axis[1].append(axis_value[1][i])
        date_values[0].append(axis_value[0][i])

    # Max of Regular Grade
    max_value = max(axis_value[2])
    max_index = axis_value[2].index(max_value)

    for i in range(max_index - 5, max_index + 6):
        max_values_axis[2].append(axis_value[2][i])
        date_values[1].append(axis_value[0][i])

    # Max of Mid Grade
    max_value = max(axis_value[3])
    max_index = axis_value[3].index(max_value)

    for i in range(max_index - 5, max_index + 6):
        max_values_axis[3].append(axis_value[3][i])
        date_values[2].append(axis_value[0][i])

    # Max of Premium Grade
    max_value = max(axis_value[4])
    max_index = axis_value[4].index(max_value)

    for i in range(max_index - 5, max_index + 6):
        max_values_axis[4].append(axis_value[4][i])
        date_values[3].append(axis_value[0][i])

    # Max of Diesel
    max_value = max(axis_value[5])
    max_index = axis_value[5].index(max_value)

    for i in range(max_index - 5, max_index + 6):
        max_values_axis[5].append(axis_value[5][i])
        date_values[4].append(axis_value[0][i])

    return date_values, max_values_axis


# Make the query about plotting the lowest value achieved by each fuels
def adv_query4(connect_db, db_name):
    axis_value = [[] for _ in range(6)]
    min_values_axis = [[] for _ in range(6)]
    date_values = [[] for _ in range(5)]
    
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name)
    all_values = cursor.fetchall()

    for value in all_values:
        axis_value[0].append(value[0])
        axis_value[1].append(value[1])
        axis_value[2].append(value[2])
        axis_value[3].append(value[3])
        axis_value[4].append(value[4])
        axis_value[5].append(value[5])

    # Find the minimum value and its surroundings
    # Min of All Grades
    min_value = min(axis_value[1])
    min_index = axis_value[1].index(min_value)

    for i in range(min_index - 5, min_index + 6):
        min_values_axis[1].append(axis_value[1][i])
        date_values[0].append(axis_value[0][i])

    # Min of Regular Grade
    min_value = min(axis_value[2])
    min_index = axis_value[2].index(min_value)

    for i in range(min_index - 5, min_index + 6):
        min_values_axis[2].append(axis_value[2][i])
        date_values[1].append(axis_value[0][i])

    # Min of Mid Grade
    min_value = min(axis_value[3])
    min_index = axis_value[3].index(min_value)

    for i in range(min_index - 5, min_index + 6):
        min_values_axis[3].append(axis_value[3][i])
        date_values[2].append(axis_value[0][i])

    # Min of Premium Grade
    min_value = min(axis_value[4])
    min_index = axis_value[4].index(min_value)

    for i in range(min_index - 5, min_index + 6):
        min_values_axis[4].append(axis_value[4][i])
        date_values[3].append(axis_value[0][i])

    # Min of Diesel
    min_value = min(axis_value[5])
    min_index = axis_value[5].index(min_value)

    for i in range(min_index - 5, min_index + 6):
        min_values_axis[5].append(axis_value[5][i])
        date_values[4].append(axis_value[0][i])

    return date_values, min_values_axis


# Make the query about all the times when Diesel was cheaper than Regular fuel
def adv_query5(connect_db, db_name):
    x_value = []
    y_value = [[] for _ in range(2)]
    
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceDiesel < PriceRegular")
    all_values = cursor.fetchall()

    for value in all_values:
        x_value.append(value[0])
        y_value[0].append(value[2])
        y_value[1].append(value[5])

    return x_value, y_value


# Make the query about all the times when Premium fuel was cheaper than Diesel
def adv_query6(connect_db, db_name):
    x_value = []
    y_value = [[] for _ in range(2)]
    
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM " + db_name + " WHERE PriceDiesel > PricePremium")
    all_values = cursor.fetchall()

    for value in all_values:
        x_value.append(value[0])
        y_value[0].append(value[4])
        y_value[1].append(value[5])

    return x_value, y_value