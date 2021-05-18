from tkinter import *
import database
import utilities


class Interface:
    # Common names used by the class
    def __init__(self):
        self.db = 'gasoline_and_diesel_prices.db'
        self.filename = 'data/Gasoline_and_Diesel_Prices.csv'
        self.db_name = self.scrub('Gasoline_and_Diesel_Prices')


    # Guarantee that the name passed is a valid name to the database
    def scrub(self, db_name):
        return ''.join(c for c in db_name if c.isalnum())


    # Insert/Update data to the database on click
    def insert_data_onClick(self):
        # Create the table to insert data (if it doesn't exist yet) 
        connect_db = database.create_connection(self.db)
        database.create_table(connect_db, self.db_name)
        database.close_connection(connect_db)

        # Insert the data from the csv file into the table created
        connect_db = database.create_connection(self.db)
        database.insert_data_on_database(connect_db, self.db_name, self.filename)
        database.close_connection(connect_db)

        ########### Test Query ###########
        connect_db = database.create_connection(self.db)
        database.search_data_test(connect_db, self.db_name)
        database.close_connection(connect_db)



    # Make query about the first price read
    def make_query1_onClick(self):
        connect_db = database.create_connection(self.db)
        result_query = database.query1(connect_db, self.db_name)
        database.close_connection(connect_db)

        print("\nResultado da Query:\n", result_query)
        print("Preços na data", result_query[0][0], ": Preço geral - U$", result_query[0][1], "Preço Regular - U$", result_query[0][2], "Preço MidGrade - U$", result_query[0][3], "Preço Premium - U$", result_query[0][4], "Preço Diesel - U$", result_query[0][5])
    

    # Make query about the last price read
    def make_query2_onClick(self):
        connect_db = database.create_connection(self.db)
        result_query = database.query2(connect_db, self.db_name)
        database.close_connection(connect_db)

        print("\nResultado da Query:\n", result_query)
        print("Preços na data", result_query[0][0], ": Preço geral - U$", result_query[0][1], "Preço Regular - U$", result_query[0][2], "Preço MidGrade - U$", result_query[0][3], "Preço Premium - U$", result_query[0][4], "Preço Diesel - U$", result_query[0][5])

    
    # Make query about the intermediate price read
    def make_query3_onClick(self):
        print("Placeholder")


    # Make query about the date when each fuel passed a determined value
    def make_query4_onClick(self):
        compared_value = float(self.entry_query4.get())

        connect_db = database.create_connection(self.db)
        regulargrade, midgrade, premiumgrade, diesel = database.query4(connect_db, self.db_name, compared_value)
        database.close_connection(connect_db)

        print("\nResultado da Query:\n", regulargrade, midgrade, premiumgrade, diesel)
        if regulargrade:
            print("Data em que o combustível Regular ultrapassou", compared_value, ":", regulargrade[0])
        else:
            print("Combustível Regular ainda não ultrapassou o valor", compared_value)
        if midgrade:
            print("Data em que o combustível MidGrade ultrapassou", compared_value, ":", midgrade[0])
        else:
            print("Combustível MidGrade ainda não ultrapassou o valor", compared_value)
        if premiumgrade:
            print("Data em que o combustível Premium ultrapassou", compared_value, ":", premiumgrade[0])
        else:
            print("Combustível Premium ainda não ultrapassou o valor", compared_value)
        if diesel:
            print("Data em que o Diesel ultrapassou", compared_value, ":", diesel[0])
        else:
            print("Diesel ainda não ultrapassou o valor", compared_value)

    # Make query about the the most expensive fuel on a given date
    def make_query10_onClick(self):
        connect_db = database.create_connection(self.db)
        result_query = database.query10(connect_db, self.db_name, self.entry_query10.get())
        database.close_connection(connect_db)

        fuel, price= utilities.get_most_expensive(result_query[0])
        print("\nResultado da Query:\n", result_query[0])
        print("Combustível mais caro na data", result_query[0][0], ":", fuel, "\nPreço: U$", price)

    def create_interface(self):
        # GUI
        menu = Tk()
        menu.title("U.S. Gasoline and Diesel Prices Database")
        menu.geometry("600x500")

        # Button to insert/update data to the sqlite database 
        self.button_data = Button(menu, text="Inserir dados ao Banco de Dados", command=self.insert_data_onClick,)
        self.button_data.pack(pady=5)

        # Button to make the query with the first price read
        self.button_query1 = Button(menu, text="Preço na data mais antiga", command=self.make_query1_onClick,)
        self.button_query1.pack(pady=5)

        # Button to take the most recent price read
        self.button_query2 = Button(menu, text="Preço na data mais recente",
                                          command=self.make_query2_onClick,)
        self.button_query2.pack(pady=5)

        # Button to take the intermediate price read
        self.button_query3 = Button(menu, text="Preço na data intermediária",
                                      command=self.make_query3_onClick, )
        self.button_query3.pack(pady=5)

        # Button to take the date when each fuel passed a determined value
        self.label_query4 = Label(menu, text="Valor a ser utilizado",)
        self.label_query4.pack(pady=8)
        self.entry_query4 = Entry(menu)
        self.entry_query4.pack()
        self.button_query4 = Button(menu, text="Data em que cada combustível ultrapassou o valor",
                                      command=self.make_query4_onClick, )
        self.button_query4.pack(pady=5)

        # Button to take the most pricey fuel on a given date
        self.label_query10 = Label(menu, text="Data a ser comparada",)
        self.label_query10.pack(pady=8)
        self.entry_query10 = Entry(menu)
        self.entry_query10.pack()
        self.button_query10 = Button(menu, text="Combustível mais caro na data",
                                 command=self.make_query10_onClick, )
        self.button_query10.pack(pady=5)

        menu.mainloop()