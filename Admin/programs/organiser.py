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
            user_input = input(colored('''      
                               
                    What operation you want to preceed with?''', 'cyan', attrs = ['bold']) +
                colored('''        
                   
                    1. CREATE
   
                    2. READ
                                   
                    3. DELETE
 
                    4. CHANGE PASSWORD
                   
                    5. Log Out
                     
                    Enter your preffered operation: ''', attrs =['bold']))
            if user_input == '1':
                self.create()
            elif user_input == '2':
                self.read()
            elif user_input == '3':
                self.delete()
            elif user_input == '4':
                self.change_pass()            
            elif user_input == '5':
                print(colored('''
                    Logged out successfully ''', 'green', attrs = ['bold']))
                break
            else:
                print(colored(''''
                    Invalid input''', 'red', attrs = ['bold']))
    def exit(self):
        print(colored('''
                    Exiting from Organiser operations... ''', 'green', attrs =['bold']))


    def change_pass(self):
        org_csv_path = "/home/narayanj/Practice/THAR2.0/Admin/csvs/organiser.csv"
        everyone_csv_path = "/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv"
       
        with open(org_csv_path, 'r') as file:
            reader = csv.DictReader(file)
            orgs_data = list(reader)
 
        for org in orgs_data:
            if org['Name'] == self.part_name:
                self.part_pass = org['Password']
                new_password = input(colored('Enter your new password: ', 'grey', attrs=['bold']))
                org['Password'] = new_password
 
                with open(org_csv_path, 'w', newline='') as file:
                    fieldnames = ['Name', 'Password', 'Role']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(orgs_data)
 
                print(colored('Password updated successfully!', 'green', attrs=['bold']))
 
                with open(everyone_csv_path, 'r') as file:
                    reader = csv.DictReader(file)
                    data = list(reader)
 
                for everyone in data:
                    if everyone['Name'] == self.part_name:
                        self.part_pass = everyone['Password']
                        everyone['Password'] = new_password
 
                with open(everyone_csv_path, 'w', newline='') as file:
                    fieldnames = ['Name', 'Password', 'Role']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(data)
 
                print(colored('Password updated successfully in everyone file', 'green', attrs=['bold']))
                return
 
        print(colored('Organiser not found!', 'red', attrs=['bold']))



 
    def create(self):
        user_input = input(colored('''
 
                    How would you like to proceed?''', 'cyan', attrs = ['bold']) + colored('''
           
                    1. Create Event
               
                    2. Create Exhibition  
               
                    3. Create Workshop
               
                    4. Create Pro-Nite
                               
                    5. Create Event Co-ordinator
               
                    6. Create Judge                    
 
                    7. Back to main
                   
                    Enter your preffered operation: ''', attrs =['bold']))
 
        if user_input == '1':
            self.create_event()
        elif user_input == '2':
            self.create_exhibition()
        elif user_input == '3':
            self.create_workshop()
        elif user_input == '4':
            self.create_pro_nite()
        elif user_input == '6':
            self.create_event_coordinator()
        elif user_input == '7':
            self.create_judge()
        elif user_input == '8':
            self.back()
            return False
        else:
            print(colored('''
                    No such operation available !!''', 'red', attrs = ['bold']))
    def back(self):
        print(colored('''
                    Going back to main crud... ''', 'green', attrs = ['bold']))
    def read(self):
        user_input = input(colored('''  
 
                    How would you like to proceed?''', 'cyan', attrs = ['bold']) +
          colored('''           
                   
                    1. Read Event
               
                    2. Read Exhibition  
               
                    3. Read Workshop
               
                    4. Read Pro-Nite'/home/narayanj/Practice/THAR2.0/Admin/csvs/event_results.csv', 'r'
               
                    5. Read Judges
 
                    6. Read Co-ordinators
 
                    7. Read All the Roles

                    8. Read Participation

                    9. Read Participants Details 
                  
                   10. Back to main
                   
                    Enter your preffered operation: ''', attrs =['bold']))
 
        if user_input == '1':
            self.read_event()
        elif user_input == '2':
            self.read_exhibition()
        elif user_input == '3':
            self.read_workshop()
        elif user_input == '4':
            self.read_pro_nite()
        elif user_input == '5':
            self.read_judges()
        elif user_input == '6':
            self.read_coordinators()
        elif user_input == '7':
            self.read_all_roles()
        elif user_input == '8':
            self.read_participants()
        elif user_input == '9':
            self.read_part_details()
        elif user_input == '10':
            self.back()
            return False
        else:
            print(colored('''
                    No such operation available !!''', 'red', attrs = ['bold']))
 
 
    def delete(self):
        user_input = input(colored('''  
 
                    How would you like to proceed?''', 'cyan', attrs = ['bold'])+ colored('''
                           
                    1. Delete Event
                   
                    2. Delete Exhibition  
                   
                    3. Delete Workshop
                   
                    4. Delete Pro-Nite
                   
                    5. Delete Event Co-ordinator
                   
                    6. Delete Judge    
 
                    7. Back to main
                   
                    Enter your preffered operation: ''', attrs = ['bold']))
 
        if user_input == '1':
            self.delete_event()
        elif user_input == '2':
            self.delete_exhibition()
        elif user_input == '3':
            self.delete_workshop()
        elif user_input == '4':
            self.delete_pro_nite()
        elif user_input == '5':
            self.delete_coordinator()
        elif user_input == '6':
            self.delete_judge()
        elif user_input == '7':
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
                print(colored('''
                    Sorry, The event you entered is already present. Please enter another event..''', 'red', attrs=['bold']))
            else:
                while True:
                    try:
                        self.event_time = input(colored('''
                    Event Time (e.g., 08:30 PM/AM): ''', 'grey', attrs = ['bold']))
                        datetime.strptime(self.event_time, "%I:%M %p")
                        break
                    except ValueError:
                        print(colored('''
                    Invalid time format. Please enter time again.''', 'red', attrs = ['bold']))
                self.event_venue = input(colored('''
                    Event place: ''', 'grey', attrs = ['bold']))
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
        with open('judge.csv', 'r') as file:
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
                    print(colored('''The list of all the Judges: ''', 'green', attrs = ['bold']))
 
                with open(self.path_1, 'r', newline='') as file:
                    x = from_csv(file)
                    x.hrules = ALL
                    print(x)
 
                with open(self.path, "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('All the roles active now: ', 'green', attrs = ['bold']))
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
                    Sorry, The Exhibition already exist, Enter another..''', 'red', attrs = ['bold']))
            else:
                self.ex_venue = input(colored('''
                    Exhibition place: ''', 'grey', attrs = ['bold']))
                while True:
                    try:
                        self.ex_time = input(colored('''
                    What will be time (e.g., 08:30 PM/AM): ''', 'grey', attrs = ['bold']))
                        datetime.strptime(self.ex_time, "%I:%M %p")
                        break
                    except ValueError:
                        print(colored('''
                    Invalid time format. Please enter time again.''', 'red', attrs = ['bold']))
 
                print(colored('''
                    Exhibition created succesfully''', 'green'))
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
                    print(colored('Exhibtion Created: ', 'green', attrs =['bold']))
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
            self.work_name = input(colored('''
                    Set workshop name: ''', 'grey', attrs =['bold']))
            if self.work_name.lower() in (name.lower() for name in self.workshop_list):
                print(colored('''
                    Sorry, The Exhibition already exist, Enter another.. ''', 'red', attrs =['bold']))
            else:
                self.work_venue = input(colored('''
                    Workshop place: ''', 'grey', attrs = ['bold']))
                while True:
                    try:
                        self.work_time = input(colored('''
                    What will be time (e.g., 08:30 PM/AM): ''', 'grey', attrs = ['bold']))
                        datetime.strptime(self.work_time, "%I:%M %p")
                        break
                    except ValueError:
                        print(colored('''
                    Invalid time format. Please enter time again.''', 'red', attrs = ['bold']))
 
                print(colored('''
                    Wrokshop created succesfully''', 'green', attrs =['bold']))
                print('\n')
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
                    print(colored('Workshop Created: ', 'green', attrs = ['bold']))
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
            self.name_pro_nite = input(colored('''
                    Set 'Pro Nite' name: ''', 'grey', attrs = ['bold']))
            if self.name_pro_nite.lower() in (name.lower() for name in self.pronites):
                print(colored('''
                    Pro Nite already exist, Enter another.. ''', 'red', attrs = ['bold']))
            else:    
                self.pro_venue = input(colored('''
                    Where it will be held: ''', 'grey', attrs = ['bold']))
                while True:
                    try:
                        self.pro_time = input(colored('''
                    What will be time (e.g., 08:30 PM/AM): ''', 'grey', attrs = ['bold']))
                        datetime.strptime(self.pro_time, "%I:%M %p")
                        break
                    except ValueError:
                        print(colored('''
                    Invalid time format. Please enter time again.''', 'red', attrs = ['bold']))
 
                self.pro_date = input(colored('''
                    Date of pro-nite being organised: ''', 'grey', attrs = ['bold']))
                print(colored('''
                    Pro-Nite created succesfully''', 'green', attrs = ['bold']))
                print('\n')
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
 
 
 
# -------------------------------------    CREATE COORDINATOR BY ADMIN    ------------------------------------- #
 
 
    def create_event_coordinator(self):
        self.cor_name = input(colored('''
                    Name of Coordinator: ''', 'grey', attrs = ['bold']))
        self.cor_event = input(colored('''
                    Coordinate which event: ''', 'grey', attrs = ['bold']))
        self.cor_pass = input(colored('''
                    Set password: ''', 'grey', attrs=['bold']))
        print('\n')
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv'
        self.path_1 = '/home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv'
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow([self.cor_name, self.cor_pass, 'Co-ordinator'])
 
        with open(self.path_1, 'a', newline='') as file:
            is_file_empty = os.stat(self.path_1).st_size == 0
            writer = csv.writer(file)
            if is_file_empty:
                writer.writerow(["Name", "Event", "Password"])
 
            writer.writerow([self.cor_name, self.cor_event, self.cor_pass])
            print(colored('''The list of all the Co-ordinators: ''', 'green', attrs=['bold']))
 
        with open(self.path_1, 'r', newline='') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(x)
            print('\n')
        with open(self.path, "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(colored('New Role added: ', 'green', attrs = ['bold']))
        print(x)





  ########################################################################################################
  #                                                                                                      #
  #                             <--------- READ STARTED HERE --------->                                  #
  #                                                                                                      #
  ########################################################################################################



# -------------------------------------    READ PARTS BY ORGANISER    ------------------------------------- #

    def read_participants(self):
        user_input = input(colored("""  

                How would you like to proceed?""", 'cyan', attrs =['bold'])+
        
        colored("""    
                           
                1. Event Participation
               
                2. Exhibition Participation   
               
                3. Workshop participation
               
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
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('''Participants in each Event is described as: ''', 'green', attrs = ['bold']))
            print(x)

    def read_exhibition_parts(self):
        print('\n')
        print(colored('Exhibitions being organised', 'green', attrs = ['bold']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv", 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(x)
            print('\n')

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('''Participants in Exhibitions: ''', 'green', attrs = ['bold']))
            print(x)

    def read_workshop_parts(self):
        print('\n')
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv", 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Workshops being organised: ', 'green', attrs = ['bold']))
            print(x)
            print('\n')

        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv", 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Participants in Workshops:', 'green', attrs = ['bold']))
            print(x)
            print('\n')




# -------------------------------------    READ EVENTS BY ORGANISER    ------------------------------------- #

    def read_event(self):
        print(colored('The Events we are organising are: \n',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ EXHIBITON BY ORGANISER    ------------------------------------- #

    def read_exhibition(self):
        print(colored('The Exhibitions are scheduled as: \n',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ WORKSHOPS BY ORGANISER    ------------------------------------- #

    def read_workshop(self):
        print(colored('The Workshops are scheduled as : \n',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ PRO-NITES BY ORGANISER    ------------------------------------- #

    def read_pro_nite(self):
        print(colored('The Pro-Nites are scheduled as: \n',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ ROLES BY ORGANISER    ------------------------------------- #

    def read_all_roles(self):
        print(colored('The role distribution is as follows: \n',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)


# -------------------------------------    READ ORGANISERS BY ORGANISER    --------------------------------- #
    
    def read_organisers(self):
        print(colored('The Organisers are: \n','magenta'))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/jorganiser.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)


# -------------------------------------    READ JUDGES BY ORGANISER    --------------------------------- #
    
    def read_judges(self):
        print(colored('The Judges are: \n','magenta'))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)


# -------------------------------------    READ COORDINATORS BY ORGANISER    --------------------------------- #
    
    def read_coordinators(self):
        print(colored('The Co-ordinators are: \n','magenta'))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)


    def read_part_details(self):
        print()
        print(colored('All participants details ','magenta'))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/partbasicdetails.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)






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


# -------------------------------------    DELETE CO-ORDINATOR BY ADMIN    ------------------------------------- #


    def delete_coordinator(self):
        filePath = '/home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv'
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
        
        with open(filePath, "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print('\n')
        print(colored('Co-ordinators before deletion: ', 'green'))
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