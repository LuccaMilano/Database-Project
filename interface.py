from tkinter import *
import database
import utilities


class Interface:
    # Common names used by the class
    def __init__(self):
        self.db = 'gasoline_and_diesel_prices.db'
        self.filename = 'data/Gasoline_and_Diesel_Prices.csv'
        self.db_name = utilities.scrub('Gasoline_and_Diesel_Prices')


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

    
    # Make query about the date when the average fuel was the most expensive
    def make_query3_onClick(self):
        connect_db = database.create_connection(self.db)
        result_query = database.query3(connect_db, self.db_name)
        database.close_connection(connect_db)

        print("\nResultado da Query:\n", result_query)
        print("Data em que o preço geral do combustível estava mais alto: ", result_query[0])
        print("Preço na data em questão: U$", result_query[1])
        

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

    
    # Make query about the date when each fuel went below a determined value
    def make_query5_onClick(self):
        compared_value = float(self.entry_query5.get())

        connect_db = database.create_connection(self.db)
        regulargrade, midgrade, premiumgrade, diesel = database.query5(connect_db, self.db_name, compared_value)
        database.close_connection(connect_db)

        print("\nResultado da Query:\n", regulargrade, midgrade, premiumgrade, diesel)
        if regulargrade:
            print("Data em que o combustível Regular estava abaixo de", compared_value, ":", regulargrade[0])
        else:
            print("Combustível Regular nunca esteve abaixo do valor", compared_value)
        if midgrade:
            print("Data em que o combustível MidGrade estava abaixo de", compared_value, ":", midgrade[0])
        else:
            print("Combustível MidGrade nunca esteve abaixo do valor", compared_value)
        if premiumgrade:
            print("Data em que o combustível Premium estava abaixo de", compared_value, ":", premiumgrade[0])
        else:
            print("Combustível Premium nunca esteve abaixo do valor", compared_value)
        if diesel:
            print("Data em que o Diesel estava abaixo de", compared_value, ":", diesel[0])
        else:
            print("Diesel nunca esteve abaixo do valor", compared_value)


    # Make query about the date when the regular fuel surpassed diesel
    def make_query6_onClick(self):
        connect_db = database.create_connection(self.db)
        result_query = database.query6(connect_db, self.db_name)
        database.close_connection(connect_db)

        print("\nResultado da Query:\n", result_query)
        print("Data em que o combustível Regular superou o Diesel: ", result_query[0])
        print("Preço do combustível Regular na data em questão: U$", result_query[2])
        print("Preço do Diesel na data em questão: U$", result_query[5])


    # Make query about the date when disel surpassed premium fuel
    def make_query7_onClick(self):
        connect_db = database.create_connection(self.db)
        result_query = database.query7(connect_db, self.db_name)
        database.close_connection(connect_db)

        print("\nResultado da Query:\n", result_query)
        print("Data em que o Diesel superou combustível premium: ", result_query[0])
        print("Preço do Diesel na data em questão: U$", result_query[5])
        print("Preço do combustível Premium na data em questão: U$", result_query[4])


    # Make query to know if regular fuel surpassed midgrade fuel one day
    def make_query8_onClick(self):
        connect_db = database.create_connection(self.db)
        result_query = database.query8(connect_db, self.db_name)
        database.close_connection(connect_db)

        print("\nResultado da Query:\n", result_query)
        if result_query:
            print("Data em que o combustível regular superou o midgrade: ", result_query[0])
            print("Preço do combustível regular na data em questão: U$", result_query[2])
            print("Preço do combustível midgrade na data em questão: U$", result_query[3])
        else:
            print("O preço do combustível regular não superou o do combustível midgrade até o prsente momento")


     # Make query to know if midgrade fuel surpassed premium fuel one day
    def make_query9_onClick(self):
        connect_db = database.create_connection(self.db)
        result_query = database.query9(connect_db, self.db_name)
        database.close_connection(connect_db)

        print("\nResultado da Query:\n", result_query)
        if result_query:
            print("Data em que o combustível midgrade superou o premium: ", result_query[0])
            print("Preço do combustível midgrade na data em questão: U$", result_query[3])
            print("Preço do combustível premium na data em questão: U$", result_query[4])
        else:
            print("O preço do combustível midgrade não superou o do combustível premium até o presente momento")


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
        menu.geometry("600x650")

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

        # Button to take the date when the average fuel was the most expensive
        self.button_query3 = Button(menu, text="Data em que o combustível, em geral, esteve mais caro",
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

         # Button to take the date when each fuel went below a determined value
        self.label_query5 = Label(menu, text="Valor a ser utilizado",)
        self.label_query5.pack(pady=8)
        self.entry_query5 = Entry(menu)
        self.entry_query5.pack()
        self.button_query5 = Button(menu, text="Data em que cada combustível ficou menor que o valor",
                                      command=self.make_query5_onClick, )
        self.button_query5.pack(pady=5)

        # Button to take the date when the regular fuel surpassed diesel
        self.button_query6 = Button(menu, text="Data em que o combustível regular superou o diesel",
                                      command=self.make_query6_onClick, )
        self.button_query6.pack(pady=5)

        # Button to take the date when disel surpassed premium fuel
        self.button_query7 = Button(menu, text="Data em que o diesel superou o combustível Premium",
                                      command=self.make_query7_onClick, )
        self.button_query7.pack(pady=5)

        # Button to know if regular fuel surpassed midgrade fuel one day
        self.button_query8 = Button(menu, text="Combustível Regular superou MidGrade em alguma data?",
                                      command=self.make_query8_onClick, )
        self.button_query8.pack(pady=5)

        # Button to know if midgrade fuel surpassed premium fuel one day
        self.button_query9 = Button(menu, text="Combustível MidGrade superou Premium em alguma data?",
                                      command=self.make_query9_onClick, )
        self.button_query9.pack(pady=5)

        # Button to take the most pricey fuel on a given date
        self.label_query10 = Label(menu, text="Data a ser comparada",)
        self.label_query10.pack(pady=8)
        self.entry_query10 = Entry(menu)
        self.entry_query10.pack()
        self.button_query10 = Button(menu, text="Combustível mais caro na data",
                                 command=self.make_query10_onClick, )
        self.button_query10.pack(pady=5)

        menu.mainloop()