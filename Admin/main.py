import csv
from termcolor import colored
from admin import Admin
from participant import Participant
from organiser import Organiser
# from coordinators import Coordinator
from judge import Judge


class UserAuthenticator:
    def __init__(self):
        self.authenticate_user()
    def authenticate_user(self):
        
        while True:
            self.part_name = input(colored("""
                    Please enter your Name:""", 'green', attrs=['bold']))

            with open('everyone.csv', 'r') as file:
                reader = csv.DictReader(file)
                name_found = any(row['Name'] == self.part_name for row in reader)

            if name_found:
                self.part_pass = input(colored("""
                    Please enter your Password:""", 'green', attrs=['bold']))

                with open('everyone.csv', 'r') as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        if row['Name'] == self.part_name and row['Password'] == self.part_pass:
                            role = row['Role']
                            if role.lower() == 'administrator':
                                print('\n')
                                print(colored('''
                                    >>>-- ADMIN DASHBOARD --<<<''', 'green', attrs=['bold']))
                                print(colored(f'''
                                    Welcome {self.part_name.upper()} ''', 'cyan', attrs=['bold']))
                                Admin()
                            elif role.lower() == 'co-ordinator':
                                print('\n')
                                print(colored('''
                                   >>>-- CO-ORDINATOR DASHBOARD --<<<''', 'green', attrs=['bold']))
                                print(colored(f'''
                                        Welcome {self.part_name.upper()} ''', 'cyan', attrs=['bold']))
                                # Coordinator()
                            elif role.lower() == 'organiser':
                                print('\n')
                                print(colored('''
                                   >>>-- ORGANISER DASHBOARD --<<<''', 'green', attrs=['bold']))
                                print(colored(f'''
                                        Welcome {self.part_name.upper()} ''', 'cyan', attrs=['bold']))
                                Organiser()
                            elif role.lower() == 'judge':
                                print('\n')
                                print(colored('''
                                   >>>-- JUDGE DASHBOARD --<<<''', 'green', attrs=['bold']))
                                print(colored(f'''
                                        Welcome {self.part_name.upper()} ''', 'cyan', attrs=['bold']))
                                Judge()
                            else:
                                print(colored("Invalid role detected.", 'red', attrs = ['bold']))
                            break
                    else:
                        print(colored("""
                    Incorrect password. Please enter again.""", 'red', attrs=['bold']))
            else:
                print(colored("""
                    Incorrect name. Please enter again.""", 'red', attrs=['bold']))


if __name__ == "__main__":

    while True:
        user_input =input("""\033[1;92m
                          
                   Login as a 'Participant' or 'Authority' ? \033[0m""" +
         
         
         ''' \033[1;96m
         
                    1. Authority
                    
                    2. Participant
                    
                    Enter your preffered login: \033[0m''')

        if user_input == '1':
            UserAuthenticator()
            break
        elif user_input == '2':
            Participant()
            break
        else:
            print('''\033[1;91m
                    Incorrect input, Choose either 1 or 2 \033[0m''')
            continue
  
