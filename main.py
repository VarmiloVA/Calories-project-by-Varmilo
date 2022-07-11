from types import NoneType
import pymysql
from tkinter import *

from requests import request

class NutritionalValues():
    def __init__(self, window): 
        self.window = window
    
    def _connect(self): # Connect to the database
        try:
            conn = pymysql.connect(
                host='localhost', 
                user='root', 
                password='mondayl#tm#brok#n', 
                db='nutritional_values'
                )

            cursor = conn.cursor()
            return conn, cursor
        except pymysql.err.OperationalError:
            print('An error has ocurred while connecting to the db')

    def run_request(self, request): # Execute a request
        conn, cursor = self._connect()
        result = cursor.execute(request)
        conn.commit()

        if result:
            return result

    def show_all(self):
        self.connect()
        request = "SELECT * FROM calories"
        self.excecute(self.conn, request)
        result = self.cursor.fetchall()
        for row in result:
            print(row)
        self.conn.close()

    def visual(self):
        lbl_food = Label(self.window, text='Food').place(x=20, y=15)
        entry_food = Entry(self.window)
        entry_food.place(x=75, y=17)
        lbl_calories = Label(self.window, text='Calories').place(x=20, y=45)
        entry_calories = Entry(self.window)
        entry_calories.place(x=75, y=47)
        add_button = Button(self.window, text='Add', command=lambda:self._add(
            entry_food.get(), 
            entry_calories.get()
            ))
        add_button.config(width=24)
        add_button.place(x=21, y=87)
    
    def _add(self, food, calories):
        if food != NoneType and calories != NoneType:
            request = "INSERT INTO calories(name, calories) VALUES(%s, %s)"
            conn, cursor = self._connect()
            cursor.execute(request, (food, calories))
            print('Sexesfully added!')

root = Tk()
root.title('Nutritional Values')
root.geometry('900x500')

nv = NutritionalValues(root)
nv.visual()

root.mainloop()