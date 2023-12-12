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
       
        while True:
            self.part_name = input(colored("""
                    Please enter your Name:""", 'green', attrs=['bold']))
 
            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'r') as file:
                reader = csv.DictReader(file)
                name_found = any(row['Name'] == self.part_name for row in reader)
 
            if name_found:
                self.part_pass = input(colored("""
                    Please enter your Password:""", 'green', attrs=['bold']))
 
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'r') as file:
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
                                Coordinator(self.part_name)
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
                                Judge(self.part_name)
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

    for i in range(220):
        print('-', end='')

    print(colored(''' 
                  

                                                                      >>>-- RAJASTHAN TECHNICAL UNIVERSITY, KOTA --<<< ''', 'green', attrs = ['bold']) +
   
colored('''
        
            Rajasthan Technical University KOTA, is located on the banks of the Chambal River, spread over an area of more than 385 acres, it proudly holds the esteemed status of                     
            
            one of the premier universities in the state of Rajasthan. With affiliations extending to over 200 colleges throughout Rajasthan, this institution educates a substantial  
            
            student body of more than 150,000 individuals. Offering a wide range of courses, including engineering and MBA programs, the university is committed to achieving academic  
            
            excellence in engineering. This commitment is realized through the provision of comprehensive knowledge to students, fostering research activities, and aligning with the 
            
            evolving demands of industry, global trends, and societal needs.
''', attrs = ['bold']))
    print(colored(''' 
                             
                                                                                >>>-- THAR --<<<''', 'green', attrs = ['bold'])+

  colored( '''
        
            THAR, the flagship techno-management fest of Rajasthan Technical University, Kota, is a three-day event that provides a platform for students to showcase their technical
          
            and management skills, network  with industry experts, and learn from successful entrepreneurs.The fest's theme, "Navigating the Technical Dunes," reflects the ever-chang
          
            ing and challenging landscape of the tech industry and the need for students to be adaptable, skilled, and resourceful.Each day of the fest features a variety of events, 
          
            including competitions, workshops,Exhibitions and pronites.

''', attrs =['bold']))
    

    for i in range(len('Come, Participate, Lead the responsibilities and see the beauty of Technicle Dunes')+8):
        print('''-''', end= '')
    print(colored('''
    Come, Participate, Lead the responsibilities and see the beauty of Technicle Dunes ''', attrs=['bold']))
    for i in range(len('Come, Participate, Lead the responsibilities and see the beauty of Technicle Dunes')+8):
        print('''-''', end ='')
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

