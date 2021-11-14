from re import split
from text_format import*

one_or_two_question = 1

dic_user = {
    'Varmilo': 'varmilova'
}

def log_in(dic_user, one_or_two_question):
    if one_or_two_question == '1':

        for key in dic_user:    
            log_user = key
            log_password = dic_user[key]

        if log_user not in dic_user:
            print(f'The {log_user} is incorrect')

        elif dic_user[log_user] != log_password:
            print('The password is incorrect')

        elif dic_user[log_user] == log_password:
            text = 'Perfect! You got completly acces to the program'
            return text

def sign_in(name, last, age, email, username, password, dicc_user):

    sign_in_name = name
    sign_in_last = last
    sign_in_age = age
    sign_email = email
    sign_in_user = username
    sign_in_password = password
            

    sign_in_age = split('\D+', sign_in_age)
    sign_age = sign_in_age[0]
            
    #Las condicionales para comprobar que el usuario ha rellenado
    #correctamente todos los campos.
    if len(sign_in_password) < 6:
        print("La contraseña debe tener mínimo 6 caracteres")

    elif sign_in_user in dicc_user:
        print('Ese username no está disponible')

    elif len(sign_in_name) == 0 or len(sign_in_last) == 0: 
        print('Alguno de los campos está incompleto')

    elif len(sign_in_user) == 0:
        print('alguno de los campos está incompleto')

    elif sign_age.isdigit() == False:
        print('La edad ha de ser un número')

    elif int(sign_age) > 110 or int(sign_age) <= 0:
        print('Perdone, pero con su edad sigue vivo??')

    elif '@' not in sign_email:
        print('Email incorrecto.')

    else:
        print('a')
