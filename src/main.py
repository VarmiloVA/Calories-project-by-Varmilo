from tkinter import ttk
from tkinter import *

import pymysql

class Calories:
    def __init__(self, window): #Here is the visual part
        #Initializing the window
        self.window = window
        self.window.title('Calories application')
        #Optionally, the window size can be set:
        #self.window.geometry('300x300')
        
        #Creating the adding Frame Container
        self.frame = LabelFrame(self.window, text='Register a food')
        self.frame.grid(row=0, column=0, columnspan=3, pady=20)

        #Adding-related
        Label(self.frame, text="Food's name: ").grid(row=1, column=0, sticky=W)
        add_food = Entry(self.frame)
        add_food.grid(row=1, column=1)
        add_food.focus_set()
        Label(self.frame, text="Its calories: ").grid(row=2, column=0, sticky=W)
        calories = Entry(self.frame)
        calories.grid(row=2, column=1)

        ttk.Button(self.frame, text='Add', command=lambda:self.add_food(add_food.get(), calories.get())).grid(row=3, column=0, sticky=W+E, columnspan=2)

        #Deleting-related
        Label(self.frame, text="Food's name:").grid(row=5, column=0, sticky=W)
        del_food = Entry(self.frame)
        del_food.grid(row=5, column=1)

        ttk.Button(self.frame, text='Delete', command=lambda:self.delete_food(del_food.get())).grid(row=6, column=0, sticky=W+E, columnspan=2)

        #Table-related
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=9, column=0, columnspan=2)
        self.tree.heading('#0', text='Food', anchor=CENTER)
        self.tree.heading('#1', text='Calories', anchor=CENTER)
        self.get_table()
        
    
    def add_food(self, food, calories): 
        food_test = food.replace(' ', '')
        calories.strip()

        invalid = Label(self.frame, text='Invalid input')
        invalid.grid(row=4, column=0, sticky=W+E, columnspan=2)
        invalid.config(fg="white")
        invalid.config(bg="white")

        if food_test.isalpha() == True and calories.isnumeric() == True:
            conn, cursor = self._connect()
            query = '''INSERT INTO food (name, calories) VALUES (%s, %s)'''
            parameters = (food.capitalize(), calories)
            self.run_query(conn, cursor, query, parameters)
            self.get_table()

            invalid.config(fg="black")
            invalid.config(bg="white")
            invalid.config(text="Succesfully registered")
            
        else:
            invalid.config(fg="red")
            invalid.config(bg="white")
            invalid.config(text="Invalid input")
            

    def delete_food(self, food):
        conn, cursor = self._connect()
        query = '''DELETE FROM food WHERE name = %s and id > 0'''
        parameters = (food)
        self.run_query(conn, cursor, query, parameters)
        self.get_table()
        
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

    #Modules related to the DB
    def _connect(self): #Module for connecting to the db
   
        conn = pymysql.connect(
            host='localhost',
            port=3306, 
            user='root', 
            password='mondayl#tm#brok#n', 
            db='calories'
            )
        cursor = conn.cursor()
        return conn, cursor
    
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

if __name__ == '__main__':
    try:
        window = Tk() 
        Calories(window)
        window.mainloop()

    except KeyboardInterrupt:
        print('\n\tCRUD App closed due to KeyboardInterrupt, see ya!\n') 
