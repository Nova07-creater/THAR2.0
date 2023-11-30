import os
import csv
from prettytable import PrettyTable, from_csv, ALL
from termcolor import colored
from datetime import datetime


# -------------------------------------    ORGANISER CLASS    ------------------------------------- #


class Organiser:
    def __init__(self):
        self.crud()
    def crud(self):
        while True:
            user_input = input('''      
                    What operation you want to preceed with?
                        
                    1. CREATE
    
                    2. READ
                                   
                    3. DELETE

                    4. CHANGE PASSWORD
                    
                    5. EXIT
                     
                    Enter your preffered operation: ''')
            if user_input == '1':
                self.create()
            elif user_input == '2':
                self.read()
            elif user_input == '3':
                self.delete()
            elif user_input == '4':
                self.change_pass()            
            elif user_input == '5':
                self.exit()
                break
            else:
                print(colored(''''
                    Invalid input''', 'red'))
    def exit(self):
        print(colored(''' 
                    Exiting from Organiser operations... ''', 'green'))
        

    def create(self):
        user_input = input("""  

                How would you like to proceed?
                        
                1. Create Event
               
                2. Create Exhibiution   
               
                3. Create Workshop
               
                4. Create Pro-Nite
               
                5. Create Organiser
               
                6. Create Event Co-ordinator 
               
                7. Create Judge                     

                8. Back to main 
                
                Enter your preffered operation: """)

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
        user_input = input("""  

                How would you like to proceed?
                        
                1. Read Event
               
                2. Read Exhibiution   
               
                3. Read Workshop
               
                4. Read Pro-Nite
               
                5. Read Organisers

                6. Read Judges

                7. Read Co-ordinators

                8. Read All the Roles

                9. Back to main
                
                Enter your preffered operation: """)

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
            self.back()
            return False
        else:
            print('No such operation available !!')

    def update(self):
        user_input = input(""" 
                How would you like to proceed?
                
                1. Update Event
                
                2. Update Exhibiution   
                
                3. Update Workshop
                
                4. Update Pro-Nite
                
                5. Update Organiser
                
                6. Update Event Co-ordinator 
                
                7. Update Judge                   

                8. Back to main
                
                Enter your preffered operation: """)
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
            print(colored('No such operation available !!', 'red'))

    def delete(self):
        user_input = input("""  

                How would you like to proceed?
                        
                1. Delete Event
                
                2. Delete Exhibiution   
                
                3. Delete Workshop
                
                4. Delete Pro-Nite
                
                5. Delete Organiser
                
                6. Delete Event Co-ordinator 
                
                7. Delete Judge     

                8. Back to main
                
                Enter your preffered operation: """)

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
            print('No such operation available !!')

  ########################################################################################################
  #                                                                                                      #
  #                             <--------- CREATION STARTED HERE --------->                              #
  #                                                                                                      #
  ########################################################################################################

# -------------------------------------    CREATE EVENTS BY ADMIN    ------------------------------------- #

    def create_event(self):
        self.events_list = []

        with open('/home/narayanj/Practice/THAR2.0/Admin/events.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.events_list.append(row['Event Name'])

        while True:
            self.event_name = input('''
            Event name: ''')

            if self.event_name.lower() in (name.lower() for name in self.events_list):
                print(colored('Sorry, The event you entered is already present. Please enter another event..', 'red'))
            else:
                while True:
                    try:
                        self.event_time = input('''
                  Event Time (e.g., 08:30 PM/AM): ''')
                        datetime.strptime(self.event_time, "%I:%M %p")
                        break 
                    except ValueError:
                        print(colored('Invalid time format. Please enter time again.', 'red'))
                self.event_venue = input('''
                # Event place: ''')
                # self.event_time = input('''
                # Event Time: ''')
                self.path = "/home/narayanj/Practice/THAR2.0/Admin/events.csv"
                self.is_file_empty = os.stat(self.path).st_size == 0

                with open(self.path, 'a', newline='') as file:
                    fieldnames = ["Event Name", "Venue", "Time"]
                    self.writer = csv.DictWriter(file, fieldnames=fieldnames)

                    if self.is_file_empty:
                        self.writer.writeheader()

                    self.writer.writerow({'Event Name': self.event_name, 'Venue': self.event_venue, 'Time': self.event_time})

                with open("/home/narayanj/Practice/THAR2.0/Admin/events.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print("\n")
                    print(colored('Event created successfully', 'green'))
                    print(x)
                    
                break
                
# -------------------------------------    CREATE JUDGES BY ADMIN    ------------------------------------- #

    def create_judge(self):
        self.judges_list = []
        with open('judge.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.judges_list.append(row['Name'])
        while True:
            self.judge_name = input('''
                Judge name: ''')
            if self.judge_name.lower() in (name.lower() for name in self.judges_list):
                print(colored('Sorry, The Judge is already there, Enter another..', 'red'))
            else:
                self.judge_event_name = input('''
                Event to be Judged: ''')
                self.judge_pass = input('''
                Set password: ''')
                print(colored('''
                Judge created successfully''', 'green'))

                self.path = 'everyone.csv'
                self.path_1 = 'judge.csv'

                with open(self.path, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([self.judge_name, self.judge_pass, 'Judge'])

                with open(self.path_1, 'a', newline='') as file:
                    is_file_empty = os.stat(self.path_1).st_size == 0
                    writer = csv.writer(file)
                    if is_file_empty:
                        writer.writerow(["Name", "Event", "Password"])

                    writer.writerow([self.judge_name, self.judge_pass, 'Judge'])
                    print(colored('The list of all the Judges: ', 'green'))

                with open(self.path_1, 'r', newline='') as file:
                    x = from_csv(file)
                    x.hrules = ALL
                    print(x)

                with open(self.path, "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('All the roles active now: ', 'green'))
                    print(x)
                break
 # -------------------------------------    CREATE EXHIBITIONS BY ADMIN    ------------------------------------- #

    def create_exhibition(self):
        self.exhibitions_list = []
        with open('exhibions.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.exhibitions_list.append(row['Exhibition'])
        while True:
            self.ex_name = input('''
                Set exhibition name: ''')
            if self.ex_name.lower() in (name.lower() for name in self.exhibitions_list):
                print(colored('''
                Sorry, The Exhibition already exist, Enter another..''', 'red'))
            else:
                self.ex_venue = input('''
                Exhibition place: ''')
                while True:
                    try:
                        self.ex_time = input('''
                  What will be time (e.g., 08:30 PM/AM): ''')
                        datetime.strptime(self.event_time, "%I:%M %p")
                        break 
                    except ValueError:
                        print(colored('Invalid time format. Please enter time again.', 'red'))

                # self.ex_time = input('''
                # What will be time: ''')
                print(colored('''
                Exhibition created succesfully''', 'green'))
                self.path = 'exhibions.csv'
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
                    print(colored('Exhibtion Created: ', 'green'))
                    print(x)
                break


# -------------------------------------    CREATE WORKSHOPS BY ADMIN    ------------------------------------- #

    def create_workshop(self):
        self.workshop_list = []
        with open('wrokshops.csv', 'r') as file:
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
                self.path = '/home/narayanj/Practice/THAR2.0/Admin/wrokshops.csv'
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
        with open('pronite.csv', 'r') as file:
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
                        datetime.strptime(self.event_time, "%I:%M %p")
                        break 
                    except ValueError:
                        print(colored('Invalid time format. Please enter time again.', 'red'))

                # self.pro_time = input('''
                # What time will it start: ''')
                self.pro_date = input('''
                Date of pro-nite being organised: ''')
                print(colored('''
                Pro-Nite created succesfully''', 'green'))
                self.path = '/home/narayanj/Practice/THAR2.0/Admin/pronite.csv'
        
                with open(self.path, 'a', newline='') as file:
                    self.writer = csv.writer(file)
                    is_file_empty = os.stat(self.path).st_size == 0
                    if is_file_empty:
                        self.writer.writerow(['Pro Nite', 'Venue', 'Time', 'Date'])
                    self.writer.writerow(
                        [self.name_pro_nite, self.pro_venue, self.pro_time, self.pro_date])
                with open("/home/narayanj/Practice/THAR2.0/Admin/pronite.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Pro Nite Created: ', 'green'))
                    print(x)
                break


    def create_event_coordinator(self):
        self.cor_name = input('Name of Coordinator: ')
        self.cor_event = input('Coordinate which event: ')
        self.cor_pass = input('Set password: ')
        print('\n')
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
        self.path_1 = '/home/narayanj/Practice/THAR2.0/Admin/coordinator.csv'
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
