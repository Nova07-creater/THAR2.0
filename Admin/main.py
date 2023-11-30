import csv
from termcolor import colored
from admin import Admin
from participant import Participant
from organiser import Organiser
from coordinators import Coordinator
from judge import Judge



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


if __name__ == "__main__":
    user_input = input(colored('''
                      
                      
                Login as a "Participant" or "Authority" ? ''', 'cyan', attrs = ['bold'])+ colored(
                ''' 

                1. Authority
                
                2. Participant
                
                Enter your preffered login: ''', 'grey', attrs = ['bold']))

    if user_input == '1':
        UserAuthenticator()
    elif user_input == '2':
        Participant()
    else:
        print(colored('''
                Welcome buddy, Come, Enjoy, Learn & Participate in our National Level Techno Management Festival...''', 'green', attrs = ['bold']))
