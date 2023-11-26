import os
import csv
import pandas as pd
from prettytable import PrettyTable, from_csv, ALL
from termcolor import colored
from datetime import datetime

# -------------------------------------    ADMIN    ------------------------------------- #


class Admin:
    def __init__(self):
        print(colored('Welcome Narayan, Admin Detected!!', 'cyan'))
        self.crud()

        # _____EVERYONE.CSV_____#

        file_path = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            is_file_empty = os.stat(file_path).st_size == 0
            if is_file_empty:
                writer.writerow(["Name", "Password", "Role"])
                writer.writerow(['Narayan', 'admin123', 'Administrator'])

    def crud(self):
        while True:
            user_input = input('''
                    
                               
                    What operation you want to preceed with?
                        
                    1. CREATE
    
                    2. READ
    
                    3. UPDATE
                               
                    4. DELETE

                    5. EXIT
                     
                    Enter your preffered operation: ''')
            if user_input == '1':
                self.create()
            elif user_input == '2':
                self.read()
            elif user_input == '3':
                self.update()
            elif user_input == '4':
                self.delete()
            elif user_input == '5':
                self.exit()
                break
            else:
                print(colored(''''
                            Invalid input''', 'red'))
    def exit(self):
        print(colored(''' 
                    Exiting from Admin CRUD... ''', 'green'))
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
        else:
            print('No such operation available !!')

    def read(self):
        user_input = input("""  

                How would you like to proceed?
                        
                1. Read Event
               
                2. Read Exhibiution   
               
                3. Read Workshop
               
                4. Read Pro-Nite
               
                5. Read Roles
                                    
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
            self.read_roles()
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
            self.event_name = input('Event name: ')

            if self.event_name.lower() in (name.lower() for name in self.events_list):
                print(colored('Sorry, The event you entered is already present. Please enter another event..', 'red'))
            else:
                self.event_venue = input('Event place: ')
                self.event_time = input('Event Time: ')
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
                    print(colored('Event created successfully', 'green'))
                    print(x)
                    
                break
                
# -------------------------------------    CREATE JUDGES BY ADMIN    ------------------------------------- #

    def create_judge(self):
        self.judge_name = input('Judge name: ')
        self.judge_event_name = input('Event to be Judged: ')
        self.judge_pass = input('Set password: ')
        print(colored('Judge created successfully', 'green'))

        self.path = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
        self.path_1 = '/home/narayanj/Practice/THAR2.0/Admin/judge.csv'

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
            print(colored('All the roles active now: ', 'green'))
            print(x)
 # -------------------------------------    CREATE EXHIBITIONS BY ADMIN    ------------------------------------- #

    def create_exhibition(self):
        self.ex_name = input('Set exhibition name: ')
        self.ex_venue = input('Exhibition place: ')
        self.ex_time = input('What will be time: ')
        print(colored('Exhibition created succesfully', 'green'))
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv'
        self.is_file_empty = os.stat(self.path).st_size == 0
        if self.is_file_empty:
            self.writer.writerow(["Exhibition", "Venue", "Time"])
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow([self.ex_name, self.ex_venue, self.ex_time])
        self.y = PrettyTable()
        self.y.field_names = ["Exhibition", "Venue", "Time"]
        self.y.add_row([self.ex_name, self.ex_venue, self.ex_time])
        print(self.y)


# -------------------------------------    CREATE WORKSHOPS BY ADMIN    ------------------------------------- #

    def create_workshop(self):
        self.work_name = input('Set workshop name: ')
        self.work_venue = input('Workshop place: ')
        self.work_time = input('What will be time: ')
        print(colored('Wrokshop created succesfully', 'green'))
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/wrokshops.csv'
        file_empty = os.stat(self.path).st_size == 0
        if file_empty:
            self.writer.writerow(['Workshop', 'Venue', 'Time'])
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(
                [self.work_name, self.work_venue, self.work_time])
        with open("/home/narayanj/Practice/THAR2.0/Admin/wrokshops.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(colored(' <--- New Workshop added ---> !!!\n',
              'red', attrs=['reverse', 'blink']))
        print(x)


# -------------------------------------    CREATE PRO-NITES BY ADMIN    ------------------------------------- #

    def create_pro_nite(self):
        self.name_pro_nite = input('Set "Pro Nite" name: ')
        self.pro_venue = input('Where it will be held: ')
        self.pro_time = input('What time will it start: ')
        self.pro_date = input('Date of pro-nite being organised: ')
        print(colored('Pro-Nite created succesfully', 'green'))
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
        print(colored(' <--- New Pro-Nite added ---> !!!\n',
              'red', attrs=['reverse', 'blink']))
        print(x)


# -------------------------------------    CREATE ORGANISER BY ADMIN    ------------------------------------- #

    def create_organiser(self):
        self.org_name = input('Name of Organiser: ')
        self.org_pass = input('Set Password: ')
        print('\n')
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
        self.path_1 = '/home/narayanj/Practice/THAR2.0/Admin/organiser.csv'
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

  ########################################################################################################
  #                                                                                                      #
  #                             <--------- READ STARTED HERE --------->                                  #
  #                                                                                                      #
  ########################################################################################################

# -------------------------------------    READ EVENTS BY ADMIN    ------------------------------------- #

    def read_event(self):
        print(colored('The Events we are organising are: \n',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/events.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)

# -------------------------------------    READ EXHIBITON BY ADMIN    ------------------------------------- #

    def read_exhibition(self):
        print(colored('The Exhibitions are scheduled as: \n',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)

# -------------------------------------    READ WORKSHOPS BY ADMIN    ------------------------------------- #

    def read_workshop(self):
        print(colored('The Workshops are scheduled as : \n',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/wrokshops.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)

# -------------------------------------    READ PRO-NITES BY ADMIN    ------------------------------------- #

    def read_pro_nite(self):
        print(colored('The Pro-Nites are scheduled as: \n',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/pronite.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)

# -------------------------------------    READ ROLES BY ADMIN    ------------------------------------- #

    def read_roles(self):
        print(colored('The role distribution is as follows: \n',
              'magenta', attrs=['reverse', 'blink']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/everyone.csv", "r") as fp:
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

            file_path = '/home/narayanj/Practice/THAR2.0/Admin/events.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                event_name_list = []
                for col in reader:
                    event_name_list.append(col['Event Name'])

            for i, item in enumerate(event_name_list):
                print(f'{i+1}.{item}\n')

            ch_event = input(
                (colored('Which event name you want to change: ', 'yellow')))
            if ch_event in event_name_list:
                chd_event = input(
                    colored('Enter the event name reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/events.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Event Name'] == ch_event:
                        row['Event Name'] = chd_event
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/events.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/events.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Events after update are as follows: \n'))
                    print(x)
            else:
                print(colored('The entered event', {
                      ch_event}, 'not found ', 'red'))

        elif self.user_input == '2':

            file_path = '/home/narayanj/Practice/THAR2.0/Admin/events.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                venue_list = []
                for col in reader:
                    venue_list.append(col['Venue'])

            for i, item in enumerate(venue_list):
                print(f'{i+1}.{item}\n')

            ch_venue = input(
                (colored('Which venue you want to change: ', 'yellow')))
            if ch_venue in venue_list:
                chd_venue = input(
                    colored('Enter the event name reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/events.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Venue'] == ch_venue:
                        row['Venue'] = chd_venue
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/events.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/events.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Venue updated : \n'))
                    print(x)
            else:
                print(colored('The entered venue', {
                      ch_event}, 'not found ', 'red'))

        elif self.user_input == '3':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/events.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                time_list = []
                for col in reader:
                    time_list.append(col['Time'])

            for i, item in enumerate(time_list):
                print(f'{i+1}.{item}\n')

            ch_time = input(
                (colored('What time you want to change: ', 'yellow')))
            if ch_time in time_list:
                chd_time = input(
                    colored('Enter the time reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/events.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Time'] == ch_time:
                        row['Time'] = chd_time
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/events.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/events.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Time updated : \n'))

                    print(x)
            else:
                print(colored('The entered time', {
                      ch_time}, 'not found ', 'red'))

        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))

# -------------------------------------    UPDATE EXHIBTION BY ADMIN    ------------------------------------- #

    def update_exhibition(self):
        self.exhibition_attributes_list = ['Exhibition Name', 'Venue', 'Time']
        print(colored('The attributes which are available to update are: \n', 'green'))

        for i, item in enumerate(self.exhibition_attributes_list):
            print(f'{i+1}.{item}\n')

        self.user_input = input('What do you want to update? ')

        if self.user_input == '1':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                exhibition_name_list = []
                for col in reader:
                    exhibition_name_list.append(col['Exhibition Name'])

            for i, item in enumerate(exhibition_name_list):
                print(f'{i+1}.{item}\n')

            ch_exhibition = input(
                (colored('Which Exhibition you want to update: ', 'yellow')))
            if ch_exhibition in exhibition_name_list:
                chd_exhibition = input(
                    colored('Enter the Exhibition reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Exhibition Name'] == ch_exhibition:
                        row['Exhibition Name'] = chd_exhibition
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Exhibtions after update are as follows: \n'))
                    print(x)
            else:
                print(colored('The entered Exhibition', {
                      ch_exhibition}, 'not found ', 'red'))

        elif self.user_input == '2':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                venue_list = []
                for col in reader:
                    venue_list.append(col['Venue'])

            for i, item in enumerate(venue_list):
                print(f'{i+1}.{item}\n')

            ch_venue = input(
                (colored('Which Venue you want to change: ', 'yellow')))
            if ch_venue in venue_list:
                chd_venue = input(
                    colored('Enter the Venue reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Venue'] == ch_venue:
                        row['Venue'] = chd_venue
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Venue updated : \n'))
                    print(x)
            else:
                print(colored('The entered venue', {
                      ch_venue}, 'not found ', 'red'))

        elif self.user_input == '3':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                time_list = []
                for col in reader:
                    time_list.append(col['Time'])

            for i, item in enumerate(time_list):
                print(f'{i+1}.{item}\n')

            ch_time = input(
                (colored('What time you want to change: ', 'yellow')))
            if ch_time in time_list:
                chd_time = input(
                    colored('Enter the time reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Time'] == ch_time:
                        row['Time'] = chd_time
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Time updated : \n'))
                    print(x)
            else:
                print(colored('The entered time', {
                      ch_time}, 'not found ', 'red'))
        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))


# -------------------------------------    UPDATE WORKSHOP BY ADMIN    ------------------------------------- #

    def update_workshop(self):
        print(colored('The attributes which are available to update are: \n', 'green'))
        self.workshop_attributes_list = ['Workshop Name', 'Venue', 'Time']

        for i, item in enumerate(self.workshop_attributes_list):
            print(f"{i+1}.{item}\n")
        self.user_input = input('What do you want to update? ')

        if self.user_input == '1':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/wrokshop.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                workshop_name_list = []
                for col in reader:
                    workshop_name_list.append(col['Workshop Name'])

            for i, item in enumerate(workshop_name_list):
                print(f'{i+1}.{item}\n')

            ch_workshop = input(
                (colored('Which Workshop you want to update: ', 'yellow')))
            if ch_workshop in workshop_name_list:
                chd_workshop = input(
                    colored('Enter the Workshop reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/wrokshop.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Workshop Name'] == ch_workshop:
                        row['Workshop Name'] = chd_workshop
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/wrokshop.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/wrokshop.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Workshops after update are as follows: \n'))
                    print(x)
            else:
                print(colored('The entered Workshop', {
                      ch_workshop}, 'not found ', 'red'))

        elif self.user_input == '2':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/wrokshop.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                venue_list = []
                for col in reader:
                    venue_list.append(col['Venue'])
            for i, item in enumerate(venue_list):
                print(f'{i+1}.{item}\n')

            ch_venue = input(
                (colored('Which Venue you want to change: ', 'yellow')))
            if ch_venue in venue_list:
                chd_venue = input(
                    colored('Enter the Venue reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/wrokshop.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Venue'] == ch_venue:
                        row['Venue'] = chd_venue
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/wrokshop.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/wrokshop.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Venue updated : \n'))
                    print(x)
            else:
                print(colored('The entered venue', {
                      ch_venue}, 'not found ', 'red'))

        elif self.user_input == '3':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/wrokshop.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                time_list = []
                for col in reader:
                    time_list.append(col['Time'])

            for i, item in enumerate(time_list):
                print(f'{i+1}.{item}\n')

            ch_time = input(
                (colored('What time you want to change: ', 'yellow')))
            if ch_time in time_list:
                chd_time = input(
                    colored('Enter the time reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/wrokshop.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Time'] == ch_time:
                        row['Time'] = chd_time
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/wrokshop.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/wrokshop.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Time updated : \n'))
                    print(x)
            else:
                print(colored('The entered time', {
                      ch_time}, 'not found ', 'red'))
        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))


# -------------------------------------    UPDATE PRO-NITE BY ADMIN    ------------------------------------- #

    def update_pro_nite(self):
        self.pro_nite_attributes_list = ['Pro Nite', 'Venue', 'Time', 'Date']
        print(colored('The attributes which are available to update are: \n'))

        for i, item in enumerate(self.pro_nite_attributes_list):
            print(f"{i+1}.{item}")
        self.user_input = input('What do you want to update? ')

        if self.user_input == '1':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/pronite.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                pro_nite_list = []
                for col in reader:
                    pro_nite_list.append(col['Pro Nite'])

            for i, item in enumerate(pro_nite_list):
                print(f'{i+1}.{item}\n')

            ch_pronite = input(
                (colored('Which Pro Nite you want to change: ', 'yellow')))
            if ch_pronite in pro_nite_list:
                chd_pronite = input(
                    colored('Enter the Pro Nite reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/pronite.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Pro Nite'] == ch_pronite:
                        row['Pro Nite'] = chd_pronite
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/pronite.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/pronite.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Pro Nites after update are as follows: \n'))
                    print(x)
            else:
                print(colored('The entered Pro Nite', {
                      ch_pronite}, 'not found ', 'red'))

        elif self.user_input == '2':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/pronite.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                venue_list = []
                for col in reader:
                    venue_list.append(col['Venue'])
            for i, item in enumerate(venue_list):
                print(f'{i+1}.{item}\n')

            ch_venue = input(
                (colored('Which Venue you want to change: ', 'yellow')))
            if ch_venue in venue_list:
                chd_venue = input(
                    colored('Enter the Venue reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/pronite.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Venue'] == ch_venue:
                        row['Venue'] = chd_venue
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/pronite.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/pronite.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print(colored('Venue updated : \n'))
                    print(x)
            else:
                print(colored('The entered venue', {
                      ch_venue}, 'not found ', 'red'))

        elif self.user_input == '3':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/pronite.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                time_list = []
                for col in reader:
                    time_list.append(col['Time'])

            for i, item in enumerate(time_list):
                print(f'{i+1}.{item}\n')

            ch_time = input(
                (colored('What time you want to change: ', 'yellow')))
            if ch_time in time_list:
                chd_time = input(
                    colored('Enter the time reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/pronite.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Time'] == ch_time:
                        row['Time'] = chd_time
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/pronite.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/pronite.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Time updated : \n'))
                    print(x)
            else:
                print(colored('The entered time', {
                      ch_time}, 'not found ', 'red'))

        elif self.user_input == '4':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/pronite.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                date_list = []
                for col in reader:
                    date_list.append(col['Date'])

            for i, item in enumerate(date_list):
                print(f'{i+1}.{item}\n')

            ch_date = input(
                (colored('What Date you want to change: ', 'yellow')))
            if ch_date in date_list:
                chd_date = input(
                    colored('Enter the Data reaplace value: ', 'yellow'))

                with open('/home/narayanj/Practice/THAR2.0/Admin/pronite.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)
                for row in rows:
                    if row['Date'] == ch_date:
                        row['Date'] = chd_date
                fieldnames = reader.fieldnames
                with open('/home/narayanj/Practice/THAR2.0/Admin/pronite.csv', 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                with open("/home/narayanj/Practice/THAR2.0/Admin/pronite.csv", "r") as fp:
                    x = from_csv(fp)
                    x.hrules = ALL
                    print('\n')
                    print(colored('Date updated : \n'))
                    print(x)
            else:
                print(colored('The entered Date', {
                      ch_time}, 'not found ', 'red'))
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
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/organiser.csv'
            file_path_1 = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                organisers = []
                for col in reader:
                    organisers.append(col['Name'])

            for i, item in enumerate(organisers):
                print(f'''
                 {i+1}.{item}''')
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
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/organiser.csv'
            file_path_1 = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                passwords = []
                for col in reader:
                    passwords.append(col['Password'])

            for i, item in enumerate(passwords):
                print(f'{i+1}.{item}\n')

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
                print(colored('The entered Password', {
                      ch_Password}, 'not found ', 'red'))
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
            file_path_1 = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                coordinators = []
                for col in reader:
                    coordinators.append(col['Name'])

            for i, item in enumerate(coordinators):
                print(f'''
                 {i+1}.{item}''')
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
            pass
        elif self.user_input == '3':
            pass
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
            pass
        elif self.user_input == '2':
            pass
        elif self.user_input == '3':
            pass
        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))

  ########################################################################################################
  #                                                                                                      #
  #                             <--------- DELETION STARTED HERE --------->                              #
  #                                                                                                      #
  ########################################################################################################

# -------------------------------------    DELETE EVENTS BY ADMIN    ------------------------------------- #

    def delete_event(self):
        filePath = '/home/narayanj/Practice/THAR2.0/Admin/events.csv'
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
        with open("/home/narayanj/Practice/THAR2.0/Admin/events.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)
        for row in data:
            if rem_event in row:
                data.remove(row)

        with open(filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        with open("/home/narayanj/Practice/THAR2.0/Admin/events.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(colored('Events after deletion: ',
                  'magenta', attrs=['reverse', 'blink']))
            print(x)


# -------------------------------------    DELETE EXHIBITION BY ADMIN    ------------------------------------- #

    def delete_exhibition(self):

        filePath = '/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv'
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
        with open("/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv", "r") as fp:
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

        filePath = '/home/narayanj/Practice/THAR2.0/Admin/wrokshops.csv'
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
        with open("/home/narayanj/Practice/THAR2.0/Admin/wrokshops.csv", "r") as fp:
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

        filePath = '/home/narayanj/Practice/THAR2.0/Admin/pronite.csv'
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
        with open("/home/narayanj/Practice/THAR2.0/Admin/pronite.csv", "r") as fp:
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
        filePath = '/home/narayanj/Practice/THAR2.0/Admin/organiser.csv'
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

        with open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r') as file:
            read = csv.reader(file)
            DATA = list(read)

            for row in DATA:
                if del_org in row:
                    DATA.remove(row)
        with open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(DATA)

        with open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Roles active after deletion of Organiser: ', 'green'))
            print(x)


# -------------------------------------    DELETE CO-ORDINATOR BY ADMIN    ------------------------------------- #


    def delete_coordinator(self):
        filePath = '/home/narayanj/Practice/THAR2.0/Admin/coordinator.csv'
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

        with open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r') as file:
            read = csv.reader(file)
            DATA = list(read)

            for row in DATA:
                if del_coordinator in row:
                    DATA.remove(row)
        with open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(DATA)

        with open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Roles active after deletion of Organiser: ', 'green'))
            print(x)


# -------------------------------------    DELETE JUDGE BY ADMIN    ------------------------------------- #


    def delete_judge(self):
        filePath = '/home/narayanj/Practice/THAR2.0/Admin/judge.csv'
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

        with open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r') as file:
            read = csv.reader(file)
            DATA = list(read)

            for row in DATA:
                if del_judges in row:
                    DATA.remove(row)
        with open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(DATA)

        with open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Roles active after deletion of Organiser: ', 'green'))
            print(x)


# -------------------------------------    ORGANISER CLASS    ------------------------------------- #


class Organiser:
    def __init__(self):
        print(colored('Organiser class called', 'green'))


class Judge:
    def __init__(self):
        print(colored('Judge class called', 'green'))


class Coordinator:
    def __init__(self):
        print(colored('Co-ordinator class called', 'green'))


class UserAuthenticator:
    def __init__(self):
        self.authenticate_user()

    def authenticate_user(self):
        name = input("Please enter your Name: ") or 'Narayan'
        password = input("Please enter your password: ") or 'admin123'

        with open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['Name'] == name and row['Password'] == password:
                    role = row['Role']
                    if role.lower() == 'administrator':
                        Admin()
                    elif role.lower() == 'co-ordinator':
                        Coordinator()
                    elif role.lower() == 'organiser':
                        Organiser()
                    elif role.lower() == 'judge':
                        Judge()
                    else:
                        print("Invalid role detected.")
                    break
            else:
                print("Incorrect name or password. Exiting...")


if __name__ == "__main__":
    UserAuthenticator()
