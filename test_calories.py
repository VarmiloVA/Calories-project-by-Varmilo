import unittest
from calories_functions import*

class Test_log_in(unittest.TestCase):
    """Prueba si log_in funciona correctamente"""
    def setUp(self):
        self.dic_user = {
            'Varmilo': '123456'
        }
        self.question = '1'
        self.correct_case = 'Perfect! You got completly acces to the program'
    
    def test_correct_data(self):
        datos_correctos = log_in(self.dic_user, self.question)
        self.assertEqual(datos_correctos, self.correct_case)

if __name__ == '__main__':
    unittest.main()


#Investingar sobre como correr varios del mismo archivo a la vez.
class Test_sign_in(unittest.TestCase):
    """Prueba si sign_in funciona correctamente"""
    def setUp(self):
        self.dic_user = {
            'Varmilo': '123456'
        }
        self.name = 'name'
        self.last = 'last'
        self.age = '18'
        self.email = 'example@gmail.com'
        self.username = 'name-last'
        self.password = '123456'
    
    def test_correct_case(self):
        sign_in_correct_case = sign_in(self.name, self.last, self.age, self.email, self.username, self.password, self.dic_user)
        self.assertEqual(sign_in_correct_case, 'a')

if __name__ == '__main__':
    unittest.main()

