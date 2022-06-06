import pymysql

class Main():
    def __init__(self):
        self.login = False

    def connect(self):
        self.conn = pymysql.connect(
            host='localhost', 
            user='root', 
            password='mondayl#tm#brok#n', 
            db='nutritional_values'
            )

        self.cursor = self.conn.cursor()

    def excecute(self, connection, request):
        self.cursor.execute(request)
        self.conn.commit()
    
    def main(self):
        while True:
            if self.login != True:
                signedin = input('Are you signed in? (S/N): ')
                if signedin.upper == "S":
                    self.login()
                elif signedin.upper == "N":
                    self.register()
                else:
                    continue
            else:
                print('\n')
                print('1. Search for a food')
                print('2. Show all foods')
                print('3. Add a food')
                print('4. Delete a food')
                print('5. Edit a food')
                print('6. Delete a user')
                print('7. Edit a user')
                print('8. Logout')
                print('9. Exit')
                print('\n')
                choice = input('Choose an option: ')
                if choice == '1':
                    self.search()
                elif choice == '2':
                    self.show_all()
                elif choice == '3':
                    self.add()
                elif choice == '4':
                    self.delete()
                elif choice == '5':
                    self.edit()
                elif choice == '6':
                    self.delete_user()
                elif choice == '7':
                    self.edit_user()
                elif choice == '8':
                    self.login = False
                    print('Logged out')
                elif choice == '9':
                    print('Bye')
                    break
                else:
                    continue
        

    def login(self):
        while True:
            username = input('Username: ')
            password = input('Password: ')
            self.connect()
            request = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
            self.excecute(self.conn, request)
            if self.cursor.fetchone() == None:
                print('Wrong username or password')
                continue
            else:
                self.login = True
                print(f'Welcome {self.cursor.fetchone()}')
                self.conn.close()
                break

    def register(self):
        while True:
            username = input('Username: ')
            password = input('Password: ')
            email = input('Email: ')
            age = input('Age: ')
            self.connect()
            request = f"INSERT INTO users (username, password, email, age) VALUES ('{username}', '{password}', '{email}', '{age}')"
            self.excecute(self.conn, request)
            print('User created')
            self.conn.close()
            self.login = True
            break    

if __name__ == "__main__":pass
