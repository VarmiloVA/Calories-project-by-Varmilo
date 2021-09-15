import json
from re import split

from text_format import *

#opening the json file
with open("calories.json", "r") as file:
    c = file.read()

dic = json.loads(c)

dic_user = dic["usuarios"]
dic_info = dic["info_usuarios"]

dicc = dic["alimentos"]

while True:

    print("For log in press 1")
    print("For sign in press 2")
    one_or_two_question = input("")

    if one_or_two_question == '1':

        log_user = input("Username: ")
        log_password = input("Password: ")

        if log_user not in dic_user:
            print('The username is incorrect')
            print(log_user)
            continue

        elif dic_user[log_user] == log_password:
            print('Perfect! You got completly acces to the program')
            first_part = 'But before, I have to tell you something, for the '
            second_part = 'moment this program is only aviable in spanish'
            print(first_part + second_part, '\n')

            break

        else:
            continue
        
    elif one_or_two_question == '2':
        while True:
            sign_in_name = input('Name: ')
            sign_in_last = input('Last: ')
            sign_in_age = input('Age:')
            sign_email = input('Email: ')
            sign_in_user = input('Username: ')
            sign_in_password = input('Password: ')
            

            sign_in_age = split('\D+', sign_in_age)
            sign_age = sign_in_age[0]
            
            #Las condicionales para comprobar que el usuario ha rellenado
            #correctamente todos los campos.
            if len(sign_in_password) < 6:
                print("La contraseña debe tener mínimo 6 caracteres")
                continue

            elif sign_in_user in dic_user:
                print('Ese username no está disponible')
                continue

            elif len(sign_in_name) == 0 or len(sign_in_last) == 0: 
                print('Alguno de los campos está incompleto')
                continue

            elif len(sign_in_user) == 0:
                print('alguno de los campos está incompleto')
                continue

            elif sign_age.isdigit() == False:
                print('La edad ha de ser un número')
                continue

            elif int(sign_age) > 110 or int(sign_age) <= 0:
                print('Perdone, pero con su edad sigue vivo??')
                continue

            elif '@' not in sign_email:
                print('Email incorrecto.')
                continue

            else:
                break
        
        #Si los datos itroducidos son correctos, se procede a añadirlos al 
        #diccionario
        sign__age = int(sign_age)

        with open("calories.json", "w") as file_sign:

            dic_user[sign_in_user] = sign_in_password

            dic_info[sign_in_user] = {
                "name": sign_in_name,
                "last": sign_in_last,
                "age": sign__age,
                "email": sign_email
            }

            json.dump(dic, file_sign, indent = 8)

        sign_completed = f'\nFelicidades {sign_in_name}!,'
        sign_completed_2 = ' ahora puedes iniciar sesión y tener acceso'
        sign_completed_3 = ' completo.'

        print(sign_completed + sign_completed_2 + sign_completed_3)
        print('\n')
            
    else:
        print("Entrada incorrecta")
        continue


while True:

    ent = input("- Introduzca un alimento: ")
    ent = format_low(ent)

    if ent not in dicc and len(ent) <= 0:
        print("Has de poner el nombre de un alimento :(")
        break

    elif ent in dicc:
        for alimento in dicc:
            if alimento == ent:
                food = format_tit(alimento)     
                print(f"{food}: {dicc[alimento]}")

    elif ent == "show all":
        print(dicc)

    elif ent not in dicc and ent!='add' and ent!='break' and ent!='delete':
        print("Ese alimento no está en la base de datos.")
        yes_no_question = input("¿Quiere añadirlo? (S/N)")
        yes_no_question = format_up(yes_no_question)

        if yes_no_question.capitalize() == "S":
            new_alimento = input("Nombre del alimento a añadir: ")
            new_alimento = format_low(new_alimento)

            new_calories = input("Calorías del alimento: ")
            new_calories = format_low(new_calories)
            
            number = split('\D+', new_calories)

            outfil3 = open("calories.json", "w")
            
            dicc[new_alimento] = number[0] + 'kcal'

            json.dump(dic, outfil3, indent = 8)
            outfil3.close()
            break

        elif yes_no_question.capitalize() == "N":
            print("El programa ha terminado.")
            break

        else:
            print("Entrada no válida")
            break

    elif ent not in dicc and ent == "add":
        new_alimento = input("Nombre del alimento a añadir: ")     
        new_alimento = format_low(new_alimento)

        new_calories = input("Calorias del alimento: ")
        new_calories = format_low(new_calories)

        if new_calories.isdigit() == False:
            dicc[new_alimento] = new_calories

            with open("calories.json", "w") as outfile:

                json.dump(dic, outfile, indent = 8)
            
                break

        elif new_calories.isdigit() == True:
            new_calories += "kcal"

            with open("calories.json", "w") as outf1le:

                dicc[new_alimento] = new_calories

                json.dump(dic, outf1le, indent = 8)
            
                break

    
    elif ent not in dicc and ent == "break":
        break

    elif ent not in dicc and ent == 'delete':
        while True:
            delete_question = input('Qué alimento desea eliminar? ')
            delete_question = format_low(delete_question)            
            
            if delete_question in dic['alimentos']:
                with open('calories.json', 'w') as outfile2:
                
                    del dicc[delete_question]
                    print("El alimento que ha introducido se ha eliminado")

                    json.dump(dic, outfile2, indent = 8)

                    break

            else:
                print('try again')
                continue        