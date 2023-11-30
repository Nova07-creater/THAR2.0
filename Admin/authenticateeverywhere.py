import csv
from admin import Admin
from participant import Participant
from organiser import Organiser
from coordinators import Coordinator
from judge import Judge
from termcolor import colored



class UserAuthenticator:
    def __init__(self):
        self.authenticate_user()
    def authenticate_user(self):
        name = input(colored("""
                        Please enter your Name:""", 'green', attrs = ['bold']) )
        password = input(colored("""
                        Please enter your Password:""", 'green', attrs = ['bold']) )

        with open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['Name'] == name and row['Password'] == password:
                    role = row['Role']
                    if role.lower() == 'administrator':
                        print('\n')
                        print(colored('''
                             ADMIN DASHBOARD''', 'green', attrs=['bold']))
                        print(colored(f'''
                   >>> Welcome {name} to your Dashboard...''', 'cyan', attrs=['bold']))
                        Admin()
                    elif role.lower() == 'co-ordinator':
                        print('\n')
                        print(colored('''
                             CO-ORDINATOR DASHBOARD''', 'green', attrs=['bold']))
                        print(colored(f'''
                   >>> Welcome {name} to your Dashboard...''', 'cyan', attrs=['bold']))
                        Coordinator()
                    elif role.lower() == 'organiser':
                        print('\n')
                        print(colored('''
                             ORGANISER DASHBOARD''', 'green', attrs=['bold']))
                        print(colored(f'''
                   >>> Welcome {name} to your Dashboard...''', 'cyan', attrs=['bold']))
                        Organiser()
                    elif role.lower() == 'judge':
                        print('\n')
                        print(colored('''
                             JUDGE DASHBOARD''', 'green', attrs=['bold']))
                        print(colored(f'''
                   >>> Welcome {name} to your Dashboard...''', 'cyan', attrs=['bold']))
                        Judge()
                    else:
                        print(colored(("""Invalid role detected.""", 'red')))
                    break
            else:
                print(colored("""
                       Incorrect name or password. Exiting...""", 'red', attrs=['bold']))










