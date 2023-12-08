import os
import csv
import re
from prettytable import PrettyTable, from_csv, ALL
from termcolor import colored
from datetime import datetime

# -------------------------------------    ADMIN    ------------------------------------- #


class Admin:
    def __init__(self):
        self.crud()

        # _____EVERYONE.CSV_____#

        file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv'
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            is_file_empty = os.stat(file_path).st_size == 0
            if is_file_empty:
                writer.writerow(["Name", "Password", "Role"])
                writer.writerow(['Narayan', 'admin123', 'Administrator'])

    def crud(self):
        while True:
            user_input = input(      
            colored(''' 
                    What operation you want to preceed with?''', 'cyan', attrs = ['bold'])+
                       
                   colored('''      
                    
                    1. CREATE
    
                    2. READ
    
                    3. UPDATE
                               
                    4. DELETE

                    5. SWITCH USER
                               
                    Enter your preffered operation: ''', 'grey', attrs =['bold']))
           
            if user_input == '1':
                self.create()
            elif user_input == '2':
                self.read()
            elif user_input == '3':
                self.update()
            elif user_input == '4':
                self.delete()
            elif user_input == '5':
                print(colored('''
                    Logged out successfully ''', 'green', attrs = ['bold']))
                break
            else:
                print(colored(''''
                    Invalid input''', 'red'))


    # def switch(self):
    #     while True:
    #         print('\n')
    #         user_input = input(colored('''      
    #             Login to which User?''', 'cyan', attrs = ['bold'])
    #             + colored('''    

    #             1. ADMIN 

    #             2. ORGANISER

    #             3. PARTICIPANT
                            
    #             4. JUDGE

    #             5. CO-ORDINATOR
                    
    #             6. EXIT
                          
    #             Enter your preffered operation: ''', 'grey', attrs= ['bold']))
    #       # if user_input == '1':
            #     self.authenticate_user()
            # elif user_input == '2':
            #     self.authenticate_user()
            # elif user_input == '3':
            #     self.authenticate_user()
            # elif user_input == '4':
            #     self.authenticate_user()
            # elif user_input == '5':
            #     self.authenticate_user()    
            # elif user_input == '6':
            #     self.exit()
            #     break 
            # else:
            #     print(colored(''''
            #     Invalid input''', 'red', attrs = ['bold']))

   
   
   
    
    def create(self):
        user_input = input(colored("""  

                    How would you like to proceed?""", 'cyan', attrs = ['bold']) +
               colored('''             
                    
                    1. Create Event
                
                    2. Create Exhibition   
                
                    3. Create Workshop
                
                    4. Create Pro-Nite
                
                    5. Create Organiser
                
                    6. Create Event Co-ordinator 
                
                    7. Create Judge                     

                    8. Back to main 
                    
                    Enter your preffered operation: ''', 'grey', attrs = ['bold']))

        if user_input == '1':
            self.create_event()
        elif user_input == '2':
            self.create_exhibition()
        elif user_input == '3':
            self.create_workshop()
        elif user_input == '4':
            self.create_pro_nite()
        elif user_input == '5':
            self.create_organiser()
        elif user_input == '6':
            self.create_event_coordinator()
        elif user_input == '7':
            self.create_judge()
        elif user_input == '8':
            self.back()
            return False
        else:
            print('No such operation available !!')
    def back(self):
        print(colored('''
                Going back to main crud... ''', 'cyan'))
    def read(self):
        user_input = input(colored("""  

                    How would you like to proceed?""" , 'cyan', attrs = ['bold']) +
                colored('''
                            
                    1. Read Event
                
                    2. Read Exhibition   
                
                    3. Read Workshop
                
                    4. Read Pro-Nite
                
                    5. Read Organisers

                    6. Read Judges

                    7. Read Co-ordinators

                    8. Read All the Roles
                            
                    9. Read Participants

                    10. Back to main
                    
                    Enter your preffered operation: ''', 'grey', attrs =['bold']))

        if user_input == '1':
            self.read_event()
        elif user_input == '2':
            self.read_exhibition()
        elif user_input == '3':
            self.read_workshop()
        elif user_input == '4':
            self.read_pro_nite()
        elif user_input == '5':
            self.read_organisers()
        elif user_input == '6':
            self.read_judges()
        elif user_input == '7':
            self.read_coordinators()
        elif user_input == '8':
            self.read_all_roles()
        elif user_input == '9':
            self.read_participants()
        elif user_input == '10':
            self.back()
            return False
        else:
            print(colored(
             '''No such operation available !!''', 'red', attrs = ['bold']))
    def back(self):
        print(colored('''
                Going back to main crud... ''', 'green', attrs =['bold']))
    def read_participants(self):
        user_input = input(colored("""  

                How would you like to proceed?""", 'cyan', attrs =['bold'])+
        
        colored("""               
                1. Read Event Participants
               
                2. Read Exhibition Participants   
               
                3. Read Workshop participants
               
                4. Back to main
                
                Enter your preffered operation: """, 'grey', attrs = ['bold']))

        if user_input == '1':
            self.read_event_parts()
        elif user_input == '2':
            self.read_exhibition_parts()
        elif user_input == '3':
            self.read_workshop_parts()
        elif user_input == '4':
            self.back()
            return False
        else:
            print(colored('''
                No such operation available !!''', 'red',attrs =['bold']))
    def back(self):
        print(colored('''
                Going back... ''', 'cyan'))
        
    def read_event_parts(self):
        print('\n')
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_details.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('''Participants in each Event is described as: ''', 'green', attrs = ['bold']))
            print(x)

    def read_exhibition_parts(self):
        print('\n')
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('''Participants in each Event is described as: ''', 'green', attrs = ['bold']))
            print(x)

    def read_workshop_parts(self):
        print('\n')
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('''Participants in each Event is described as: ''', 'green', attrs = ['bold']))
            print(x)

    def update(self):
        user_input = input(colored(""" 
                How would you like to proceed?""", 'cyan', attrs = ['bold'])+

            colored("""    
                1. Update Event
                
                2. Update Exhibition   
                
                3. Update Workshop
                
                4. Update Pro-Nite
                
                5. Update Organiser
                
                6. Update Event Co-ordinator 
                
                7. Update Judge                   

                8. Back to main
                
                Enter your preffered operation: """, 'grey', attrs = ['bold']))
        if user_input == '1':
            self.update_event()
        elif user_input == '2':
            self.update_exhibition()
        elif user_input == '3':
            self.update_workshop()
        elif user_input == '4':
            self.update_pro_nite()
        elif user_input == '5':
            self.update_organiser()
        elif user_input == '6':
            self.update_coordinator()
        elif user_input == '7':
            self.update_judge()
        elif user_input == '8':
            self.back()
            return False
        else:
            print(colored('''
                No such operation available !!''', 'red', attrs = ['bold']))

    def delete(self):
        user_input = input(colored("""  

                How would you like to proceed?""", 'cyan', attrs = ['bold'])+   
          colored("""              
                1. Delete Event
                
                2. Delete Exhibition   
                
                3. Delete Workshop
                
                4. Delete Pro-Nite
                
                5. Delete Organiser
                
                6. Delete Event Co-ordinator 
                
                7. Delete Judge     

                8. Back to main
                
                Enter your preffered operation: """, 'grey', attrs = ['bold']))

        if user_input == '1':
            self.delete_event()
        elif user_input == '2':
            self.delete_exhibition()
        elif user_input == '3':
            self.delete_workshop()
        elif user_input == '4':
            self.delete_pro_nite()
        elif user_input == '5':
            self.delete_organiser()
        elif user_input == '6':
            self.delete_coordinator()
        elif user_input == '7':
            self.delete_judge()
        elif user_input == '8':
            self.back()
            return False
        else:
            print(colored('''
                No such operation available !!''', 'red', attrs = ['bold']))

  ########################################################################################################
  #                                                                                                      #
  #                             <--------- CREATION STARTED HERE --------->                              #
  #                                                                                                      #
  ########################################################################################################

# -------------------------------------    CREATE EVENTS BY ADMIN    ------------------------------------- #

    def create_event(self):
        self.events_list = []

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.events_list.append(row['Event Name'])

        while True:
            self.event_name = input(colored('''
                Event name: ''', 'grey', attrs = ['bold']))

            if self.event_name.lower() in (name.lower() for name in self.events_list):
                print(colored('Sorry, The event you entered is already present. Please enter another event..', 'red'))
            else:
                while True:
                    try:
                        self.event_time = input(colored('''
                Event Time (e.g., 08:30 PM/AM): ''', 'grey', attrs =['bold']))
                        datetime.strptime(self.event_time, "%I:%M %p")
                        break 
                    except ValueError:
                        print(colored('''
                Invalid time format. Please enter time again.''', 'red', attrs = ['bold']))
                self.event_venue = input(colored('''
                Event place: ''', 'grey', attrs = ['bold']))
                # self.event_time = input('''
                # Event Time: ''')
                self.path = "/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv"
                self.is_file_empty = os.stat(self.path).st_size == 0

                with open(self.path, 'a', newline='') as file:
                    fieldnames = ["Event Name", "Venue", "Time"]
                    self.writer = csv.DictWriter(file, fieldnames=fieldnames)

                    if self.is_file_empty:
                        self.writer.writeheader()

                    self.writer.writerow({'Event Name': self.event_name, 'Venue': self.event_venue, 'Time': self.event_time})

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print("\n")
                    print(colored('''Event created successfully''', 'green', attrs = ['bold']))
                    print(x)
                    
                break
                
# -------------------------------------    CREATE JUDGES BY ADMIN    ------------------------------------- #

    def create_judge(self):
        self.judges_list = []
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/judge.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.judges_list.append(row['Name'])
        while True:
            self.judge_name = input(colored('''
                Judge name: ''', 'grey', attrs = ['bold']))
            if self.judge_name.lower() in (name.lower() for name in self.judges_list):
                print(colored('''
                Sorry, The Judge is already there, Enter another..''', 'red', attrs = ['bold']))
            else:
                self.judge_event_name = input(colored('''
                Event to be Judged: ''', 'grey', attrs = ['bold']))
                self.judge_pass = input(colored('''
                Set password: ''', 'grey', attrs = ['bold']))
                print(colored('''
                Judge created successfully''', 'green', attrs = ['bold']))

                self.path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv'
                self.path_1 = '/home/narayanj/Practice/THAR2.0/Admin/csvs/judge.csv'

                with open(self.path, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([self.judge_name, self.judge_pass, 'Judge'])

                with open(self.path_1, 'a', newline='') as file:
                    is_file_empty = os.stat(self.path_1).st_size == 0
                    writer = csv.writer(file)
                    if is_file_empty:
                        writer.writerow(["Name", "Event", "Password"])

                    writer.writerow([self.judge_name, self.judge_pass, 'Judge'])
                    print(colored('The list of all the Judges: ', 'green', attrs = ['bold']))

                with open(self.path_1, 'r', newline='') as file:
                    x = from_csv(file)
                    x.hrules = ALL
                    print(x)

                with open(self.path, "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('''All the roles active now: ''', 'green', attrs = ['bold']))
                    print(x)
                break
 # -------------------------------------    CREATE EXHIBITIONS BY ADMIN    ------------------------------------- #

    def create_exhibition(self):
        self.exhibitions_list = []
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.exhibitions_list.append(row['Exhibition'])
        while True:
            self.ex_name = input(colored('''
                    Set exhibition name: ''', 'grey', attrs = ['bold']))
            if self.ex_name.lower() in (name.lower() for name in self.exhibitions_list):
                print(colored('''
                    Sorry, The Exhibition already exist, Enter another..''', 'red', attrs =['bold']))
            else:
                self.ex_venue = input(colored('''
                Exhibition place: ''', 'grey', attrs = ['bold']))
                while True:
                    try:
                        self.ex_time = input(colored('''
                    What will be time (e.g., 08:30 PM/AM): ''', 'grey', attrs =['bold']))
                        datetime.strptime(self.event_time, "%I:%M %p")
                        break 
                    except ValueError:
                        print(colored('''
                    Invalid time format. Please enter time again.''', 'red', attrs =['bold']))

                # self.ex_time = input('''
                # What will be time: ''')
                print(colored('''
                    Exhibition created succesfully''', 'green', attrs =['bold']))
                self.path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv'
                self.is_file_empty = os.stat(self.path).st_size == 0
                if self.is_file_empty:
                    self.writer.writerow(["Exhibition", "Venue", "Time"])
                with open(self.path, 'a', newline='') as file:
                    self.writer = csv.writer(file)
                    self.writer.writerow([self.ex_name, self.ex_venue, self.ex_time])
                with open(self.path, "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('''Exhibtion Created: ''', 'green', attrs = ['bold']))
                    print(x)
                break


# -------------------------------------    CREATE WORKSHOPS BY ADMIN    ------------------------------------- #

    def create_workshop(self):
        self.workshop_list = []
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.workshop_list.append(row['Workshop'])
        while True:
            self.work_name = input('''
                Set workshop name: ''')
            if self.work_name.lower() in (name.lower() for name in self.workshop_list):
                print(colored('''
                Sorry, The Exhibition already exist, Enter another.. ''', 'red'))
            else:
                self.work_venue = input('''
                Workshop place: ''')
                while True:
                    try:
                        self.work_time = input('''
                  What will be time (e.g., 08:30 PM/AM): ''')
                        datetime.strptime(self.event_time, "%I:%M %p")
                        break 
                    except ValueError:
                        print(colored('Invalid time format. Please enter time again.', 'red'))

                # self.work_time = input('''
                # What will be time: ''')
                print(colored('''
                Wrokshop created succesfully''', 'green'))
                self.path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv'
                file_empty = os.stat(self.path).st_size == 0
                if file_empty:
                    self.writer.writerow(['Workshop', 'Venue', 'Time'])
                with open(self.path, 'a', newline='') as file:
                    self.writer = csv.writer(file)
                    self.writer.writerow(
                        [self.work_name, self.work_venue, self.work_time])
                with open(self.path, "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Workshop Created: ', 'green'))
                    print(x)
                break

# -------------------------------------    CREATE PRO-NITES BY ADMIN    ------------------------------------- #

    def create_pro_nite(self):
        self.pronites = []
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.pronites.append(row['Pro Nite'])
        while True:
            self.name_pro_nite = input('''
                Set 'Pro Nite' name: ''')
            if self.name_pro_nite.lower() in (name.lower() for name in self.pronites):
                print(colored('''
                Pro Nite already exist, Enter another.. ''', 'red'))
            else:    
                self.pro_venue = input('''
                Where it will be held: ''')
                while True:
                    try:
                        self.pro_time = input('''
                  What will be time (e.g., 08:30 PM/AM): ''')
                        datetime.strptime(self.pro_time, "%I:%M %p")
                        break 
                    except ValueError:
                        print(colored('Invalid time format. Please enter time again.', 'red'))
                
                while True:      
                    self.pro_date = input("Date of pro-nite being organised: (DD/MM/YYYY): ")         
                    date_pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')
                    if date_pattern.match(self.pro_date):         
                        print(f"Valid date: {self.pro_date}")        
                        break      
                    else:          
                        print("""
                  Invalid date format. Please enter the date in the format (DD/MM/YYYY).""")
                # self.pro_date = input('''
                # Date of pro-nite being organised: ''')
                print(colored('''
                Pro-Nite created succesfully''', 'green', attrs = ['bold']))
                self.path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv'
        
                with open(self.path, 'a', newline='') as file:
                    self.writer = csv.writer(file)
                    is_file_empty = os.stat(self.path).st_size == 0
                    if is_file_empty:
                        self.writer.writerow(['Pro Nite', 'Venue', 'Time', 'Date'])
                    self.writer.writerow(
                        [self.name_pro_nite, self.pro_venue, self.pro_time, self.pro_date])
                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Pro Nite Created: ', 'green', attrs = ['bold']))
                    print(x)
                break

# -------------------------------------    CREATE ORGANISER BY ADMIN    ------------------------------------- #

    def create_organiser(self):
        self.org_name = input('Name of Organiser: ')
        self.org_pass = input('Set Password: ')
        print('\n')
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv'
        self.path_1 = '/home/narayanj/Practice/THAR2.0/Admin/csvs/jorganiser.csv'
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow([self.org_name, self.org_pass, 'Organiser'])

        with open(self.path_1, 'a', newline='') as file:
            is_file_empty = os.stat(self.path_1).st_size == 0
            writer = csv.writer(file)
            if is_file_empty:
                writer.writerow(["Name", "Password", 'Role'])
            writer.writerow([self.org_name, self.org_pass, 'Organiser'])
            print(colored('The list of all the Organisers: ', 'green'))

        with open(self.path_1, 'r', newline='') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(x)
            print('\n')
        with open(self.path, "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(colored('New Role added: ', 'green'))
        print(x)

# -------------------------------------    CREATE CO-ORDINATOR BY ADMIN    ------------------------------------- #

    def create_event_coordinator(self):
        self.cor_name = input('Name of Coordinator: ')
        self.cor_event = input('Coordinate which event: ')
        self.cor_pass = input('Set password: ')
        print('\n')
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv'
        self.path_1 = '/home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv'
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(
                [self.cor_name, self.cor_pass, 'Co-ordinator'])

        with open(self.path_1, 'a', newline='') as file:
            is_file_empty = os.stat(self.path_1).st_size == 0
            writer = csv.writer(file)
            if is_file_empty:
                writer.writerow(["Name", "Event", "Password"])

            writer.writerow([self.cor_name, self.cor_event, self.cor_pass])
            print(colored('The list of all the Co-ordinators: ', 'green'))

        with open(self.path_1, 'r', newline='') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(x)
            print('\n')
        with open(self.path, "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(colored('New Role added: ', 'green'))
        print(x)

  ########################################################################################################
  #                                                                                                      #
  #                             <--------- READ STARTED HERE --------->                                  #
  #                                                                                                      #
  ########################################################################################################

# -------------------------------------    READ EVENTS BY ADMIN    ------------------------------------- #

    def read_event(self):
        print(colored('The Events we are organising are: ',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ EXHIBITON BY ADMIN    ------------------------------------- #

    def read_exhibition(self):
        print(colored('The Exhibitions are scheduled as: ',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ WORKSHOPS BY ADMIN    ------------------------------------- #

    def read_workshop(self):
        print(colored('The Workshops are scheduled as : ',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ PRO-NITES BY ADMIN    ------------------------------------- #

    def read_pro_nite(self):
        print(colored('The Pro-Nites are scheduled as: ',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ ROLES BY ADMIN    ------------------------------------- #

    def read_all_roles(self):
        print(colored('The role distribution is as follows: ',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)


# -------------------------------------    READ ORGANISERS BY ADMIN    --------------------------------- #
    
    def read_organisers(self):
        print(colored('The Organisers are: ','magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/jorganiser.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)


# -------------------------------------    READ JUDGES BY ADMIN    --------------------------------- #
    
    def read_judges(self):
        print(colored('The Judges are: ','magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)


# -------------------------------------    READ COORDINATORS BY ADMIN    --------------------------------- #
    
    def read_coordinators(self):
        print(colored('The Co-ordinators are: ','magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

  
  ########################################################################################################
  #                                                                                                      #
  #                             <--------- UPDATE STARTED HERE --------->                                #
  #                                                                                                      #
  ########################################################################################################


# -------------------------------------    UPDATE EVENTS BY ADMIN    ------------------------------------- #

    def update_event(self):
            self.event_attributes_list = ['Event Name', 'Venue', 'Time']
            print(colored('The attributes which are available to update are: \n', 'yellow'))
            for i, item in enumerate(self.event_attributes_list):
                print(f'{i+1}. {item}\n')
            self.user_input = input(
                colored('What do you want to update? \n', 'yellow'))

            if self.user_input == '1':

                file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv'
                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    event_name_list = []
                    for col in reader:
                        event_name_list.append(col['Event Name'])

                # for i, item in enumerate(event_name_list):
                #     print(f'{i+1}.{item}\n')
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'r') as file:
                    x = from_csv(file)
                    x.hrules= ALL
                    print(x)
                    print('\n')
                ch_event = input(
                    (colored('Which event name you want to change: ', 'yellow')))
                if ch_event in event_name_list:
                    chd_event = input(
                        colored('Enter the event name reaplace value: ', 'yellow'))

                    with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'r') as file:
                        reader = csv.DictReader(file)
                        rows = list(reader)
                    for row in rows:
                        if row['Event Name'] == ch_event:
                            row['Event Name'] = chd_event
                    fieldnames = reader.fieldnames
                    with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'w', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(rows)

                    with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv", "r") as fp:
                        x = from_csv(fp)
                        x.hrules = ALL
                        print(colored('Events after update are as follows: \n'))
                        print(x)
                else:
                    print(colored('The entered event not found ', 'red'))

            elif self.user_input == '2':

                file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv'
                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    venue_list = []
                    for col in reader:
                        venue_list.append(col['Venue'])

                # for i, item in enumerate(venue_list):
                #     print(f'{i+1}.{item}\n')
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'r') as file:
                    x = from_csv(file)
                    x.hrules= ALL
                    print(x)
                    print('\n')
                ch_venue = input(
                    (colored('Which venue you want to change: ', 'yellow')))
                if ch_venue in venue_list:
                    chd_venue = input(
                        colored('Enter the event name reaplace value: ', 'yellow'))

                    with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'r') as file:
                        reader = csv.DictReader(file)
                        rows = list(reader)
                    for row in rows:
                        if row['Venue'] == ch_venue:
                            row['Venue'] = chd_venue
                    fieldnames = reader.fieldnames
                    with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'w', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(rows)

                    with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv", "r") as fp:
                        x = from_csv(fp)
                        x.hrules = ALL
                        print(colored('Venue updated : \n'))
                        print(x)
                else:
                    print(colored('The entered venue not found ', 'red'))

            elif self.user_input == '3':
                file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv'
                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    time_list = []
                    for col in reader:
                        time_list.append(col['Time'])

                # for i, item in enumerate(time_list):
                #     print(f'{i+1}.{item}\n')
                with open('file_path', 'r') as file:
                    x = from_csv(file)
                    x.hrules= ALL
                    print(x)
                    print('\n')
                while True:
                    try:
                        ch_time = input('What time you want to change (e.g., 08:30 PM/AM): ')
                        datetime.strptime(self.event_time, "%I:%M %p")
                        break 
                    except ValueError:
                        print(colored('Invalid time format. Please enter time again.', 'red'))
                # ch_time = input(
                #     (colored('What time you want to change: ', 'yellow')))
                if ch_time in time_list:
                    while True:
                        try:
                            chd_time = input('What time you want to change (e.g., 08:30 PM/AM): ')
                            datetime.strptime(self.event_time, "%I:%M %p")
                            break 
                        except ValueError:
                            print(colored('Invalid time format. Please enter time again.', 'red'))
                    # chd_time = input(
                    #     colored('Enter the time reaplace value: ', 'yellow'))
                    with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'r') as file:
                        reader = csv.DictReader(file)
                        rows = list(reader)
                    for row in rows:
                        if row['Time'] == ch_time:
                            row['Time'] = chd_time
                    fieldnames = reader.fieldnames
                    with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'w', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(rows)

                    with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv", "r") as fp:
                        x = from_csv(fp)
                        x.hrules = ALL
                        print('\n')
                        print(colored('Time updated : \n'))

                        print(x)
                else:
                    print(colored('The entered time not found ', 'red'))

            else:
                print(colored('Sorry, The attribute you entered is not available !!', 'red'))
# -------------------------------------    UPDATE EXHIBTION BY ADMIN    ------------------------------------- #

    def update_exhibition(self):
        self.exhibition_attributes_list = ['Exhibition Name', 'Venue', 'Time']
        print(colored('The attributes which are available to update are: \n', 'yellow'))
        for i, item in enumerate(self.exhibition_attributes_list):
            print(f'{i+1}. {item}\n')
        self.user_input = input(
            colored('What do you want to update? \n', 'yellow'))

        if self.user_input == '1':

            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                exhibition_name_list = []
                for col in reader:
                    self.exhibition_attributes_list.append(col['Exhibition'])
            # for i, item in enumerate(event_name_list):
            #     print(f'{i+1}.{item}\n')
            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv', 'r') as file:
                x = from_csv(file)
                x.hrules= ALL
                print(x)
                print('\n')
            ch_exhibition = input(
                (colored('Which Exhibition name you want to change: ', 'yellow')))
            if ch_exhibition in exhibition_name_list:
                chd_exhibition = input(
                    colored('Enter the event name replace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Exhibition'] == ch_exhibition:
                        row['Exhibition'] = chd_exhibition
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Exhibitions after update are as follows: \n'))
                    print(x)
            else:
                print(colored('The entered exhibition not found ', 'red'))

        elif self.user_input == '2':

            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                venue_list = []
                for col in reader:
                    venue_list.append(col['Venue'])

            # for i, item in enumerate(venue_list):
            #     print(f'{i+1}.{item}\n')
            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv', 'r') as file:
                x = from_csv(file)
                x.hrules= ALL
                print(x)
                print('\n')
            ch_venue = input(
                (colored('Which venue you want to change: ', 'yellow')))
            if ch_venue in venue_list:
                chd_venue = input(
                    colored('Enter the venue reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Venue'] == ch_venue:
                        row['Venue'] = chd_venue
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Venue updated : \n'))
                    print(x)
            else:
                print(colored('The entered venue not found ', 'red'))

        elif self.user_input == '3':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                time_list = []
                for col in reader:
                    time_list.append(col['Time'])

            # for i, item in enumerate(time_list):participants
            #     print(f'{i+1}.{item}\n')
            with open('file_path', 'r') as file:
                x = from_csv(file)
                x.hrules= ALL
                print(x)
                print('\n')
            while True:
                try:
                    ch_time = input('What time you want to change (e.g., 08:30 PM/AM): ')
                    datetime.strptime(self.event_time, "%I:%M %p")
                    break 
                except:
                    print(colored('Invalid time format. Please enter time again.', 'red'))
            # ch_time = input(
            #     (colored('What time you want to change: ', 'yellow')))
            if ch_time in time_list:
                while True:
                    try:
                        chd_time = input('Enter the time replace value (e.g., 08:30 PM/AM): ')
                        datetime.strptime(self.event_time, "%I:%M %p")
                        break 
                    except ValueError:
                        print(colored('Invalid time format. Please enter time again.', 'red'))
                # chd_time = input(
                #     colored('Enter the time replace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Time'] == ch_time:
                        row['Time'] = chd_time
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Time updated : \n'))

                    print(x)
            else:
                print(colored('The entered time not found ', 'red'))

        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))


# -------------------------------------    UPDATE WORKSHOP BY ADMIN    ------------------------------------- #

    def update_workshop(self):
        self.workshop_attributes_list = ['Workshop Name', 'Venue', 'Time']
        print(colored('The attributes which are available to update are: \n', 'yellow'))
        for i, item in enumerate(self.workshop_attributes_list):
            print(f'{i+1}. {item}\n')
        self.user_input = input(
            colored('What do you want to update? \n', 'yellow'))

        if self.user_input == '1':

            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                workshop_name_list = []
                for col in reader:
                    workshop_name_list.append(col['Workshop'])

            # for i, item in enumerate(event_name_list):
            #     print(f'{i+1}.{item}\n')
            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv', 'r') as file:
                x = from_csv(file)
                x.hrules= ALL
                print(x)
                print('\n')
            ch_workshop = input(
                (colored('Which Workshop name you want to change: ', 'yellow')))
            if ch_workshop in workshop_name_list:
                chd_workshop = input(
                    colored('Enter the workshop name replace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Workshop'] == ch_workshop:
                        row['Workshop'] = chd_workshop
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Workshops after update are as follows: \n'))
                    print(x)
            else:
                print(colored('The entered workshop not found ', 'red'))

        elif self.user_input == '2':

            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                venue_list = []
                for col in reader:
                    venue_list.append(col['Venue'])

            # for i, item in enumerate(venue_list):
            #     print(f'{i+1}.{item}\n')
            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv', 'r') as file:
                x = from_csv(file)
                x.hrules= ALL
                print(x)
                print('\n')
            ch_venue = input(
                (colored('Which venue you want to change: ', 'yellow')))
            if ch_venue in venue_list:
                chd_venue = input(
                    colored('Enter the venue replace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Venue'] == ch_venue:
                        row['Venue'] = chd_venue
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Venue updated : \n'))
                    print(x)
            else:
                print(colored('The entered venue not found ', 'red'))

        elif self.user_input == '3':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                time_list = []
                for col in reader:
                    time_list.append(col['Time'])

            # for i, item in enumerate(time_list):
            #     print(f'{i+1}.{item}\n')
            with open('file_path', 'r') as file:
                x = from_csv(file)
                x.hrules= ALL
                print(x)
                print('\n')
            while True:
                 try:
                    ch_time = input('What time you want to change (e.g., 08:30 PM/AM): ')
                    datetime.strptime(self.event_time, "%I:%M %p")
                    break 
                 except:
                     print(colored('Invalid time format. Please enter time again.', 'red'))
            # ch_time = input(
            #     (colored('What time you want to change: ', 'yellow')))
            if ch_time in time_list:
                while True:
                    try:
                        chd_time = input('Enter the time replace value (e.g., 08:30 PM/AM): ')
                        datetime.strptime(self.event_time, "%I:%M %p")
                        break 
                    except:
                        print(colored('Invalid time format. Please enter time again.', 'red'))
                # chd_time = input(
                #     colored('Enter the time replace value: ', 'yellow'))

            # ch_time = input(
            #     (colored('What time you want to change: ', 'yellow')))
            # if ch_time in time_list:
            #     chd_time = input(
            #         colored('Enter the time reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Time'] == ch_time:
                        row['Time'] = chd_time
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Time updated : \n'))

                    print(x)
            else:
                print(colored('The entered time not found ', 'red'))

        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))


# -------------------------------------    UPDATE PRO-NITE BY ADMIN    ------------------------------------- #

    def update_pro_nite(self):
        self.pro_nite_attributes_list = ['Pro Nite', 'Venue', 'Time', 'Date']
        print(colored('The attributes which are available to update are: \n', 'yellow'))
        for i, item in enumerate(self.pro_nite_attributes_list):
            print(f'{i+1}. {item}\n')
        self.user_input = input(
            colored('What do you want to update? \n', 'yellow'))

        if self.user_input == '1':

            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                pronite_name_list = []
                for col in reader:
                    pronite_name_list.append(col['Pro Nite'])

            # for i, item in enumerate(event_name_list):
            #     print(f'{i+1}.{item}\n')
            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv', 'r') as file:
                x = from_csv(file)
                x.hrules= ALL
                print(x)
                print('\n')
            ch_pronite = input(
                (colored('Which Pro Nite you want to change: ', 'yellow')))
            if ch_pronite in pronite_name_list:
                chd_pronite = input(
                    colored('Enter the pro-nite name replace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Pro Nite'] == ch_pronite:
                        row['Pro Nite'] = chd_pronite
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Pro Nite after update are as follows: \n'))
                    print(x)
            else:
                print(colored('The entered pro-nite not found ', 'red'))

        elif self.user_input == '2':

            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                venue_list = []
                for col in reader:
                    venue_list.append(col['Venue'])

            # for i, item in enumerate(venue_list):
            #     print(f'{i+1}.{item}\n')
            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv', 'r') as file:
                x = from_csv(file)
                x.hrules= ALL
                print(x)
                print('\n')
            ch_venue = input(
                (colored('Which venue you want to change: ', 'yellow')))
            if ch_venue in venue_list:
                chd_venue = input(
                    colored('Enter the venue replace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Venue'] == ch_venue:
                        row['Venue'] = chd_venue
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Venue updated : \n'))
                    print(x)
            else:
                print(colored('The entered venue not found ', 'red'))

        elif self.user_input == '3':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                time_list = []
                for col in reader:
                    time_list.append(col['Time'])

            # for i, item in enumerate(time_list):
            #     print(f'{i+1}.{item}\n')
            with open('file_path', 'r') as file:
                x = from_csv(file)
                x.hrules= ALL
                print(x)
                print('\n')
            ch_time = input(
                (colored('What time you want to change: ', 'yellow')))
            if ch_time in time_list:
                chd_time = input(
                    colored('Enter the time replace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Time'] == ch_time:
                        row['Time'] = chd_time
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Time updated : \n'))

                    print(x)
            else:
                print(colored('The entered time not found ', 'red'))

        elif self.user_input == '4':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                date_list = []
                for col in reader:
                    date_list.append(col['Date'])

            # for i, item in enumerate(time_list):
            #     print(f'{i+1}.{item}\n')
            with open('file_path', 'r') as file:
                x = from_csv(file)
                x.hrules= ALL
                print(x)
                print('\n')
            while True:      
                ch_date = input(colored('''What Date you want to change: (DD/MM/YYYY): ''', 'yellow'))         
                date_pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')
                if date_pattern.match(ch_date):         
                    print(f"Entered date: {ch_date}")        
                    break      
                else:          
                    print(colored(""" 
                Invalid date format. Please enter the date in the format (DD/MM/YYYY).""", 'red', attrs = ['bold']))
            # ch_date = input(
            #     (colored('What Date you want to change: ', 'yellow')))
            if ch_date in date_list:
                while True:      
                    chd_date = input(colored('Enter the Date reaplace value (DD/MM/YYYY):  ', 'yellow'))         
                    date_pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')
                    if date_pattern.match(chd_date):         
                        print(f"Entered date: {chd_date}")        
                        break      
                    else:          
                        print("""
                    Invalid date format. Please enter the date in the format (DD/MM/YYYY).""")
                
                # chd_date = input(
                #     colored('Enter the Date reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Date'] == ch_date:
                        row['Date'] = chd_date
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Date updated : \n'))
                    print(x)
            else: 
                print(colored('The Date entered doesn\'t match any..', 'red'))
        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))


# -------------------------------------    UPDATE ORGANISER BY ADMIN    ------------------------------------- #

    def update_organiser(self):
        self.organiser_attributes_list = ['Name', 'Password']
        print('\n')
        print(colored('''
                The attributes which are available to update are: ''', 'green'))

        for i, item in enumerate(self.organiser_attributes_list):
            print(f"""
                 {i+1}.{item} """)
        self.user_input = input(colored('''
                What do you want to update: ''', 'green'))

        if self.user_input == '1':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/organiser.csv'
            file_path_1 = '/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                organisers = []
                for col in reader:
                    organisers.append(col['Name'])
            with open(file_path, 'r') as file:
              x = from_csv(file)
              x.hrules = ALL
              print(x)
              print('\n')
            # for i, item in enumerate(organisers):
            #     print(f'''
            #      {i+1}.{item}''')
            ch_name = input(
                (colored('''
                Which Organiser name you want to change: ''', 'green')))
            if ch_name in organisers:
                chd_name = input(
                    colored('''
                Enter the name reaplace value: ''', 'green'))

                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Name'] == ch_name:
                        row['Name'] = chd_name
                fieldnames = reader.fieldnames
                with open(file_path, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open(file_path, "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Organisers data updated: ', 'green'))
                    print(x)
                
                with open(file_path_1, 'r') as file:
                    reader = csv.reader(file)
                    data = list(reader)
                
                for row in data:
                    if ch_name in row:
                        data.remove(row)
                with open(file_path_1, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                print('\n')
                print(colored('The main file is also updated: ', 'green'))
                with open(file_path_1, 'r') as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(x)

            else:
                print(colored('The entered Organiser', {
                      ch_name}, 'not found ', 'red'))

        elif self.user_input == '2':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/organiser.csv'
            file_path_1 = '/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                passwords = []
                for col in reader:
                    passwords.append(col['Password'])
           
            with open(file_path, 'r') as file:
                x = from_csv(file)
                x.hrules = ALL
                print(x)
                print('\n')

            # for i, item in enumerate(passwords):
            #     print(f'{i+1}.{item}\n')

            ch_Password = input(
                (colored('Which Password you want to change: ', 'green')))
            if ch_Password in passwords:
                chd_Password = input(
                    colored('Enter the Password reaplace value: ', 'green'))
                print('\n')
                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Password'] == ch_Password:
                        row['Password'] = chd_Password
                fieldnames = reader.fieldnames
                with open(file_path, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open(file_path, "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Password has been updated in organisers file: ', 'green'))
                    print(x)

                with open(file_path_1, 'r') as file:
                    reader = csv.reader(file)
                    data_1 = list(reader)

                for row in data_1:
                    if ch_Password in row:
                        data_1.remove(row)
                with open(file_path_1, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data_1)
                
                with open(file_path_1, 'r') as file:
                    x = from_csv(file)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Password has been updated in main file: '))
                    print(x)

            else:
                print(colored('The entered Password not found ', 'red'))
        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))


# -------------------------------------   UPDATE EVENT COORDINATOR BY ADMIN    ------------------------------------- #

    def update_coordinator(self):
        self.coordinator_attributes_list = ['Name', 'Event Name', 'Password']
        print(colored('The attributes which are available to update are: \n'))

        for i, item in enumerate(self.coordinator_attributes_list):
            print(f"{i+1}.{item}")
        self.user_input = input('What do you want to update? ')

        if self.user_input == '1':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/coordinators.csv'
            file_path_1 = '/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                coordinators = []
                for col in reader:
                    coordinators.append(col['Name'])
            with open(file_path, 'r') as file:
                x = from_csv(file)
                x.hrules = ALL
                print(x)
                print('\n')
            # for i, item in enumerate(coordinators):
            #     print(f'''
            #      {i+1}.{item}''')
            ch_name = input(
                (colored('''
                Which Co-ordinators name you want to change: ''', 'green')))
            if ch_name in coordinators:
                chd_name = input(
                    colored('''
                Enter the name reaplace value: ''', 'green'))

                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Name'] == ch_name:
                        row['Name'] = chd_name
                fieldnames = reader.fieldnames
                with open(file_path, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open(file_path, "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Organisers data updated: ', 'green'))
                    print(x)
                
                with open(file_path_1, 'r') as file:
                    reader = csv.reader(file)
                    data = list(reader)
                
                for row in data:
                    if ch_name in row:
                        data.remove(row)
                with open(file_path_1, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                print('\n')
                print(colored('The main file is also updated: ', 'green'))
                with open(file_path_1, 'r') as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(x)

            else:
                print(colored('The entered Organiser', {
                      ch_name}, 'not found ', 'red'))

        elif self.user_input == '2':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                event_name_list = []
                for col in reader:
                    event_name_list.append(col['Event'])

            # for i, item in enumerate(event_name_list):
            #     print(f'{i+1}.{item}\n')
            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv', 'r') as file:
                x = from_csv(file)
                x.hrules= ALL
                print(x)
                print('\n')
            ch_event = input(
                (colored('Which event you want to change: ', 'yellow')))
            if ch_event in event_name_list:
                chd_event = input(
                    colored('Enter the event name reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Event'] == ch_event:
                        row['Event'] = chd_event
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Events after update are as follows: \n'))
                    print(x)
            else:
                print(colored('The entered event not found ', 'red'))

        elif self.user_input == '3':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv'
            file_path_1 = '/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                passwords = []
                for col in reader:
                    passwords.append(col['Password'])
           
            with open(file_path, 'r') as file:
                x = from_csv(file)
                x.hrules = ALL
                print(x)
                print('\n')

            # for i, item in enumerate(passwords):
            #     print(f'{i+1}.{item}\n')

            ch_Password = input(
                (colored('Which Password you want to change: ', 'green')))
            if ch_Password in passwords:
                chd_Password = input(
                    colored('Enter the Password reaplace value: ', 'green'))
                print('\n')
                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Password'] == ch_Password:
                        row['Password'] = chd_Password
                fieldnames = reader.fieldnames
                with open(file_path, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open(file_path, "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Password has been updated in organisers file: ', 'green'))
                    print(x)

                with open(file_path_1, 'r') as file:
                    reader = csv.reader(file)
                    data_1 = list(reader)

                for row in data_1:
                    if ch_Password in row:
                        data_1.remove(row)
                with open(file_path_1, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data_1)
                
                with open(file_path_1, 'r') as file:
                    x = from_csv(file)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Password has been updated in main file: '))
                    print(x)

            else:
                print(colored('The entered Password not found ', 'red'))
        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))


# -------------------------------------   UPDATE JUDGE BY ADMIN    ------------------------------------- #

    def update_judge(self):
        self.judge_attributes_list = ['Name', 'Event Name', 'Password']
        print(colored('The attributes which are available to update are: \n'))

        for i, item in enumerate(self.judge_attributes_list):
            print(f"{i+1}.{item}")
        self.user_input = input('What do you want to update? ')

        if self.user_input == '1':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv'
            file_path_1 = '/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                judges = []
                for col in reader:
                    judges.append(col['Name'])
            with open(file_path, 'r') as file:
                x = from_csv(file)
                x.hrules = ALL
                print(x)
                print('\n')
            # for i, item in enumerate(coordinators):
            #     print(f'''
            #      {i+1}.{item}''')
            ch_name = input(
                (colored('''
                Which Judge name you want to change: ''', 'green')))
            if ch_name in judges:
                chd_name = input(
                    colored('''
                Enter the name reaplace value: ''', 'green'))

                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Name'] == ch_name:
                        row['Name'] = chd_name
                fieldnames = reader.fieldnames
                with open(file_path, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open(file_path, "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Judge data updated: ', 'green'))
                    print(x)
                
                with open(file_path_1, 'r') as file:
                    reader = csv.reader(file)
                    data = list(reader)
                
                for row in data:
                    if ch_name in row:
                        data.remove(row)
                with open(file_path_1, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                print('\n')
                print(colored('The main file is also updated: ', 'green'))
                with open(file_path_1, 'r') as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(x)

            else:
                print(colored('The entered Judge not found ', 'red'))

        elif self.user_input == '2':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/judge.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                event_name_list = []
                for col in reader:
                    event_name_list.append(col['Event'])

            # for i, item in enumerate(event_name_list):
            #     print(f'{i+1}.{item}\n')
            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/judge.csv', 'r') as file:
                x = from_csv(file)
                x.hrules= ALL
                print(x)
                print('\n')
            ch_event = input(
                (colored('Which event you want to change: ', 'yellow')))
            if ch_event in event_name_list:
                chd_event = input(
                    colored('Enter the event name reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/judge.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Event'] == ch_event:
                        row['Event'] = chd_event
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/judge.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/judge.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Events after update are as follows: \n'))
                    print(x)
            else:
                print(colored('The entered event not found ', 'red'))

        elif self.user_input == '3':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv'
            file_path_1 = '/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                passwords = []
                for col in reader:
                    passwords.append(col['Password'])
           
            with open(file_path, 'r') as file:
                x = from_csv(file)
                x.hrules = ALL
                print(x)
                print('\n')

            # for i, item in enumerate(passwords):
            #     print(f'{i+1}.{item}\n')

            ch_Password = input(
                (colored('Which Password you want to change: ', 'green')))
            if ch_Password in passwords:
                chd_Password = input(
                    colored('Enter the Password reaplace value: ', 'green'))
                print('\n')
                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Password'] == ch_Password:
                        row['Password'] = chd_Password
                fieldnames = reader.fieldnames
                with open(file_path, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open(file_path, "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Password has been updated in organisers file: ', 'green'))
                    print(x)

                with open(file_path_1, 'r') as file:
                    reader = csv.reader(file)
                    data_1 = list(reader)

                for row in data_1:
                    if ch_Password in row:
                        data_1.remove(row)
                with open(file_path_1, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data_1)
                
                with open(file_path_1, 'r') as file:
                    x = from_csv(file)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Password has been updated in main file: '))
                    print(x)

            else:
                print(colored('The entered Password not found ', 'red'))
        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))

  ########################################################################################################
  #                                                                                                      #
  #                             <--------- DELETION STARTED HERE --------->                              #
  #                                                                                                      #
  ########################################################################################################

# -------------------------------------    DELETE EVENTS BY ADMIN    ------------------------------------- #

    def delete_event(self):
        filePath = '/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv'
        with open(filePath, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

        with open(filePath, 'r') as file:
            reader_1 = csv.DictReader(file)
            event_names = []
            for col in reader_1:
                event_names.append(col['Event Name'])

        print(colored('List of Events: \n', 'green'))
        for i, item in enumerate(event_names):
            print(f'{i+1}.{item}\n')

        rem_event = input(colored('Which event you want to remove: ', 'green'))
        print(colored('Events before deletion: ',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)
        for row in data:
            if rem_event in row:
                data.remove(row)

        with open(filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(colored('Events after deletion: ',
                  'magenta', attrs=['reverse', 'blink']))
            print(x)


# -------------------------------------    DELETE EXHIBITION BY ADMIN    ------------------------------------- #

    def delete_exhibition(self):

        filePath = '/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv'
        with open(filePath, 'r') as file:
            reader_1 = csv.DictReader(file)
            exhibitions = []
            for col in reader_1:
                exhibitions.append(col['Exhibition'])
            print(colored('List of exhibitions: \n', 'green'))
        for i, item in enumerate(exhibitions):
            print(f'{i+1}.{item}\n')

        with open(filePath, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        del_exhibition = input(
            colored('Which exhibtion you want to delete: ', 'green'))
        print('\n')
        print(colored('Exhibitions before deletion: ',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)

        for row in data:
            if del_exhibition in row:
                data.remove(row)
        with open(filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        with open(filePath, 'r') as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print('\n')
        print(colored('Exhibitions after deletion: ',
              'magenta', attrs=['reverse', 'blink']))
        print(x)


# -------------------------------------    DELETE WORKSHOP BY ADMIN    ------------------------------------- #

    def delete_workshop(self):

        filePath = '/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv'
        with open(filePath, 'r') as file:
            reader_1 = csv.DictReader(file)
            Workshop = []
            for col in reader_1:
                Workshop.append(col['Workshop'])
            print(colored('List of Workshops: \n', 'green'))
        for i, item in enumerate(Workshop):
            print(f'{i+1}.{item}\n')

        with open(filePath, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        del_workshop = input(
            colored('Which Workshop you want to delete: ', 'green'))
        print(colored('Workshop before deletion: ',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)

        for row in data:
            if del_workshop in row:
                data.remove(row)
        with open(filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        with open(filePath, 'r') as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print('\n')
        print(colored('Workshop after deletion: ',
              'magenta', attrs=['reverse', 'blink']))
        print(x)


# -------------------------------------    DELETE PRO-NITE BY ADMIN    ------------------------------------- #

    def delete_pro_nite(self):

        filePath = '/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv'
        with open(filePath, 'r') as file:
            reader_1 = csv.DictReader(file)
            pronites = []
            for col in reader_1:
                pronites.append(col['Pro Nite'])
            print(colored('List of Pro-Nites: \n', 'green'))
        for i, item in enumerate(pronites):
            print(f'{i+1}.{item}\n')

        with open(filePath, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        del_pronite = input(
            colored('Which Pro Nite you want to delete: ', 'green'))
        print(colored('Pro Nites before deletion: ',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)

        for row in data:
            if del_pronite in row:
                data.remove(row)
        with open(filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        with open(filePath, 'r') as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print('\n')
        print(colored('Pro Nites after deletion: ',
              'magenta', attrs=['reverse', 'blink']))
        print(x)


# -------------------------------------    DELETE ORGANISER BY ADMIN    ------------------------------------- #

    def delete_organiser(self):
        filePath = '/home/narayanj/Practice/THAR2.0/Admin/csvs/organiser.csv'
        with open(filePath, 'r') as file:
            reader_1 = csv.DictReader(file)
            organisers = []
            for col in reader_1:
                organisers.append(col['Name'])
            print(colored('List of Organisers: \n', 'green'))
        for i, item in enumerate(organisers):
            print(f'{i+1}.{item}\n')

        with open(filePath, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        del_org = input(
            colored('Which Organiser you want to delete: ', 'green'))
        print(colored('Organisers before deletion: ', 'green'))
        with open(filePath, "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)

        for row in data:
            if del_org in row:
                data.remove(row)
        with open(filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        with open(filePath, 'r') as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print('\n')
        print(colored('Organisers after deletion: ', 'green'))
        print(x)

        print('\n')

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'r') as file:
            read = csv.reader(file)
            DATA = list(read)

            for row in DATA:
                if del_org in row:
                    DATA.remove(row)
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(DATA)

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Roles active after deletion of Organiser: ', 'green'))
            print(x)


# -------------------------------------    DELETE CO-ORDINATOR BY ADMIN    ------------------------------------- #


    def delete_coordinator(self):
        filePath = '/home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs//home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv'
        with open(filePath, 'r') as file:
            reader_1 = csv.DictReader(file)
            coordinators = []
            for col in reader_1:
                coordinators.append(col['Name'])
            print(colored('List of Co-ordinators: \n', 'green'))
        for i, item in enumerate(coordinators):
            print(f'{i+1}.{item}\n')

        with open(filePath, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        del_coordinator = input(
            colored('Which Co-ordinator you want to delete: ', 'green'))
        print(colored('Co-ordinators before deletion: ', 'green'))
        with open(filePath, "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)

        for row in data:
            if del_coordinator in row:
                data.remove(row)
        with open(filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        with open(filePath, 'r') as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print('\n')
        print(colored('Co-ordinators after deletion: ', 'green'))
        print(x)

        print('\n')

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'r') as file:
            read = csv.reader(file)
            DATA = list(read)

            for row in DATA:
                if del_coordinator in row:
                    DATA.remove(row)
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(DATA)

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Roles active after deletion of Organiser: ', 'green'))
            print(x)


# -------------------------------------    DELETE JUDGE BY ADMIN    ------------------------------------- #


    def delete_judge(self):
        filePath = '/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv'
        with open(filePath, 'r') as file:
            reader_1 = csv.DictReader(file)
            judges = []
            for col in reader_1:
                judges.append(col['Name'])
            print(colored('List of Judges: \n', 'green'))
        for i, item in enumerate(judges):
            print(f'{i+1}.{item}\n')

        with open(filePath, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        del_judges = input(
            colored('Which Judge you want to delete: ', 'green'))
        print(colored('Judges before deletion: ', 'green'))
        with open(filePath, "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)

        for row in data:
            if del_judges in row:
                data.remove(row)
        with open(filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        with open(filePath, 'r') as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print('\n')
        print(colored('Judges after deletion: ', 'green'))
        print(x)

        print('\n')

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'r') as file:
            read = csv.reader(file)
            DATA = list(read)

            for row in DATA:
                if del_judges in row:
                    DATA.remove(row)
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(DATA)

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Roles active after deletion of Organiser: ', 'green'))
            print(x)