from tkinter import ttk
from tkinter import *

import pymysql

class Calories:
    def __init__(self, window):
        #db settings
        self.db_name = 'calories'
        self.db_password = 'mondayl#tm#brok#n'

        #Initializing the window
        self.window = window
        self.window.title('Calories application')
        #Optionally, the window size can be set:
        #self.window.geometry('300x300')
        
        #Creating a Frame Container
        frame = LabelFrame(self.window, text='Register a food')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        #Name Input
        Label(frame, text="Food's name: ").grid(row=1, column=0, sticky=W)
        food = Entry(frame)
        food.grid(row=1, column=1)
        food.focus_set()
        Label(frame, text="Its calories: ").grid(row=2, column=0, sticky=W)
        calories = Entry(frame)
        calories.grid(row=2, column=1)
        ttk.Button(frame, text='Add').grid(row=3, column=0, sticky=W+E, columnspan=2)

        #Table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Food', anchor=CENTER)
        self.tree.heading('#1', text='Calories', anchor=CENTER)

        self.get_table()

    def add_food(self, food, calories):
        conn, cursor = self._connect()
        query = '''INSERT INTO food (name, calories) VALUES (%s, %s)'''
        parameters = (food, calories)
        self.run_query(conn, cursor, query, parameters)

    def _connect(self): #Module for connecting to the db
        try:
            conn = pymysql.connect(
                host='localhost', 
                user='root', 
                password=self.db_password, 
                db=self.db_name
                )
            cursor = conn.cursor()
            return conn, cursor
        except pymysql.err.OperationalError: 
            print('An error has ocurred while connecting to the db')
    
    def run_query(self, conn, cursor, query, parameters=()): #Module for requesting data from the db
        try:
            result = cursor.execute(query, parameters)
            conn.commit()
            if result:
                try:
                    return cursor.fetchall()
                except:pass

            print('Succesfully runned the query')

        except:
            print('An error has ocurred while running the query')

        finally:
            conn.close()
    
    def get_table(self):
        #Cleaning tree
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #Getting data
        conn, cursor = self._connect()
        query = '''SELECT * FROM food ORDER BY id ASC'''
        rows = self.run_query(conn, cursor, query)
        #Filling tree
        for row in rows:
            self.tree.insert('', 0, text=row[1], values=f'{row[2]}kcal')

    def get_food(self, food):
        conn, cursor = self._connect()
        query = '''SELECT * FROM food WHERE name = %s'''
        parameter = (food)
        result = self.run_query(conn, cursor, query, parameters=parameter)
        return result

if __name__ == '__main__':
    try:
        window = Tk() 
        Calories(window)
        window.mainloop()

    except KeyboardInterrupt:
        print('\n\tCRUD App closed due to KeyboardInterrupt, see ya!\n')
         