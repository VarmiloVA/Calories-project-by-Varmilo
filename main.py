import pymysql
from pymysql.err import OperationalError
#from tkinter import Canvas, Lable, Button, Tk, Frame, Entry, StringVar, Scrollbar, Listbox, END, W, E, N, S

class NutritionalValues():
    def __init__(self, login_status): # Initialize the class
        self.login_status = login_status
        self.stop = False

    def connect(self): # Connect to the database
        self.conn = pymysql.connect(
            host='localhost', 
            user='root', 
            password='mondayl#tm#brok#n', 
            db='nutritional_values'
            )

        self.cursor = self.conn.cursor()

    def excecute(self, connection, request): # Execute a request
        self.cursor.execute(request)
        self.conn.commit()
    
    def run(self): # Module that runs the program
        while self.login != False:
            signedin = input('Are you signed in? (S/N): ')
            if signedin.strip().upper() == "S":
                self.login()
            elif signedin.strip().upper() == "N":
                self.register()
            elif signedin.strip().lower() == 'exit':
                self.stop = True
                break
            

        while self.login == True:
            print('\n')
            print('- 1. Search for a food')
            print('- 2. Show all foods')
            print('- 3. Add a food')
            print('- 4. Logout')
            print('- 5. Exit')
            choice = input('\nChoose an option: ')
            print('\n')
            if choice == '1':
                self.search()
            elif choice == '2':
                self.show_all()
            elif choice == '3':
                self.add()
            elif choice == '4':
                self.login = False
                print('\nLogged out')
            elif choice == '5':
                self.stop = True
                print('\nBye')
                break
            else:
                continue

    def login(self): # Login to the database
        while True:
            username = input('Username: ')
            password = input('Password: ')

            if username.lower() == 'exit' or password.lower() == 'exit':
                self.stop = True
            
            try:
                self.connect()
                request = f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'"
                self.excecute(self.conn, request)
                self.login = True
                print(f'\nWelcome {username}')
                self.conn.close()
            except OperationalError:
                print('\nWrong username or password\n')
                continue

    def register(self): # Register to the database
        while True:
            username = input('\n- Username: ')
            password = input('- Password: ')
            email = input('- Email: ')
            age = input('- Age: ')

            self.connect()
            request = f"INSERT INTO user (username, password, email, age) VALUES ('{username}', '{password}', '{email}', '{age}')"
            self.excecute(self.conn, request)
            request = f"INSERT INTO credentials (username, password) VALUES ('{username}', '{password}')"
            self.excecute(self.conn, request)
            print('\nUser created')
            self.conn.close()
            self.login = True
            break
    
    def show_all(self):
        self.connect()
        request = "SELECT * FROM calories"
        self.excecute(self.conn, request)
        result = self.cursor.fetchall()
        for row in result:
            print(row)
        self.conn.close()

    def add(self):pass

    def visual(self):pass

if __name__ == "__main__": # Run the program
    nv = NutritionalValues(True) # The instance is named as nv for short
    nv.stop = False
    while nv.stop != True:
        try:
            nv.run()
        except KeyboardInterrupt:
            nv.stop = True
            print('\nBye')