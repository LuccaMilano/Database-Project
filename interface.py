from tkinter import *
import database


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
        result_query1 = database.query1(connect_db, self.db_name)
        database.close_connection(connect_db)

        print("Preços na data mais antiga: ", result_query1)
    

    # Make query about the last price read
    def make_query2_onClick(self):
        print("Placeholder")

    
    # Make query about the intermediate price read
    def make_query3_onClick(self):
        print("Placeholder")


    # Make query about the the most expensive fuel on a given date
    def make_query10_onClick(self):
        print("Placeholder")

    def create_interface(self):
        # GUI
        menu = Tk()
        menu.title("U.S. Gasoline and Diesel Prices Database")
        menu.geometry("450x350")

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

        # Button to take the most pricey fuel on a given date
        self.label_query10 = Label(menu, text="Data a ser comparada",)
        self.label_query10.pack(pady=8)
        self.entry_query10 = Entry(menu)
        self.entry_query10.pack()
        self.button_query10 = Button(menu, text="Combustível mais caro na data",
                                 command=self.make_query10_onClick, )
        self.button_query10.pack(pady=5)

        menu.mainloop()