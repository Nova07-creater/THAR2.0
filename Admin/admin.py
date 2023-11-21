import os
import csv
from prettytable import PrettyTable, from_csv, ALL
from termcolor import colored


# -------------------------------------    CREATED CSV FILE FOR STORING ROLES    ------------------------------------- #


file_path = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
with open(file_path, 'a', newline='') as file:
    writer = csv.writer(file)
    is_file_empty = os.stat(file_path).st_size == 0
    if is_file_empty:
        writer.writerow(["Name", "Password", "Role"])
        writer.writerow(['Narayan', 'admin123', 'Administrator'])


# -------------------------------------    ADMIN    ------------------------------------- #


class Admin:
    def __init__(self):
        pass
        self.temp_1 = input('Admin, Please enter your Name: ')
        if self.temp_1.lower() == 'narayan':
            self.temp_2 = input('Please Enter your password: ')
            if self.temp_2 == 'admin123':
                self.crud()
            else:
                print('Password incorrect')
        else:
            print('Incorrect username')

    def crud(self):
        user_input = input('''
                What operation you want to preceed with?
                    
                1. Creation
                2. Updation
                3. Deletion
                
                ''')
        if user_input == '1':
            self.creation()

        elif user_input == '2':
            self.Updation()
        elif user_input == '3':
            self.Deletion()
        else:
            print(colored('Invalid input', 'red'))


    def creation(self):
        user_input = input("""  

                How would you like to proceed?
                        
                1. Create Event
                2. Create Exhibiution   
                3. Create Workshop
                4. Create Pro-Nite
                5. Create Organiser
                6. Create Event Co-ordinator 
                7. Create Judge                     
                """)

        if user_input == '1':
            self.CreateEvent()
        elif user_input == '2':
            self.CreateExhibition()
        elif user_input == '3':
            self.CreateWorkshop()
        elif user_input == '4':
            self.CreateProNite()
        elif user_input == '5':
            self.CreateOrganiser()
        elif user_input == '6':
            self.CreateCoordinator()
        else:
            print('No such operation available !!')
   
   
    def Updation(self):
        user_input = input("""
                How would you like to proceed?
                
                1. Update Event
                2. Update Exhibiution   
                3. Update Workshop
                4. Update Pro-Nite
                5. Update Organiser
                6. Update Event Co-ordinator 
                7. Update Judge                   
                           
                """)
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
        else:
            print(colored('No such operation available !!', 'red'))


# -------------------------------------    UPDATE EVENTS BY ADMIN    ------------------------------------- #

    def update_event(self):
        self.event_attributes_list = ['Event Name', 'Venue', 'Time']
        print(colored('The attributes which are available to update are: \n', 'green'))
        for i, item in enumerate(self.event_attributes_list):
            print(f'{i+1}. {item}\n')
        self.user_input = input('What do you want to update? ')

        if self.user_input.lower() == 'event name':
            pass
        elif self.user_input.lower() == 'venue':
            pass
        elif self.user_input.lower() == 'Time':
            pass
        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))

# -------------------------------------    UPDATE EXHIBTION BY ADMIN    ------------------------------------- #

    def update_exhibition(self):
        self.exhibition_attributes_list = ['Exhibition Name', 'Venue', 'Time']
        print(colored('The attributes which are available to update are: \n', 'green'))

        for i, item in enumerate(self.exhibition_attributes_list):
            print(f'{i+1}.{item}\n')
        
        self.user_input = input('What do you want to update? ')

        if self.user_input.lower() == 'exhibition name':
            pass
        elif self.user_input.lower() == 'venue':
            pass
        elif self.user_input.lower() == 'time':
            pass
        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))


# -------------------------------------    UPDATE WORKSHOP BY ADMIN    ------------------------------------- #

    def update_workshop(self):
        self.workshop_attributes_list = ['Workshop Name', 'Venue', 'Time']
        print(colored('The attributes which are available to update are: \n', 'green'))

        for i, item in enumerate(self.workshop_attributes_list):
            print(f"{i+1}.{item}\n")
        self.user_input = input('What do you want to update? ')

        if self.user_input == '1':
            pass
        elif self.user_input == '2':
            pass
        elif self.user_input == '3':
            pass
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
            pass
        elif self.user_input == '2':
            pass
        elif self.user_input == '3':
            pass
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
            pass
        elif self.user_input == '2':
            pass
        elif self.user_input == '3':
            pass
        else:
            print(colored('Sorry, The attribute you entered is not available !!', 'red'))

# -------------------------------------    CREATE EVENTS BY ADMIN    ------------------------------------- #

    def CreateEvent(self):
        self.event_name = input('Event name: ')
        self.event_venue = input('Event place: ')
        self.event_time = input('Event Time: ')
        print(colored('Event created succesfully', 'green'))
        self.path = "/home/narayanj/Practice/THAR2.0/Admin/events.csv"
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(
                [self.event_name, self.event_venue, self.event_time])

        with open("/home/narayanj/Practice/THAR2.0/Admin/events.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)

# -------------------------------------    CREATE JUDGES BY ADMIN    ------------------------------------- #

    def CreateJudge(self):
        self.judge_name = input('Judge name: ')
        self.judge_event_name = input('Event to be Judged: ')
        self.judge_pass = input('Set password: ')
        print(colored('Judge created succesfully', 'green'))
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow([self.judge_name, self.judge_pass, 'Judge'])

        with open("/home/narayanj/Practice/THAR2.0/Admin/everyone.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules=ALL
        print(x)

# -------------------------------------    CREATE EXHIBITIONS BY ADMIN    ------------------------------------- #

    def CreateExhibition(self):
        self.ex_name = input('Set exhibition name: ')
        self.ex_venue = input('Exhibition place: ')
        self.ex_time = input('What will be time: ')
        print(colored('Exhibition created succesfully', 'green'))
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv'
        self.is_file_empty = os.stat(file_path).st_size == 0
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

    def CreateWorkshop(self):
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

    def CreateProNite(self):
        self.name_pro_nite = input('Set "Pro Nite" name: ')
        self.pro_venue = input('Where it will be helo: ')
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

    def CreateOrganiser(self):
        self.org_name = input('Name of Organiser: ')
        self.org_pass = input('Set Password: ')
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow([self.org_name, self.org_pass, 'Organiser'])
        with open("/home/narayanj/Practice/THAR2.0/Admin/everyone.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(colored(' <--- New Organiser added ---> !!!\n',
              'red', attrs=['reverse', 'blink']))
        print(x)

# -------------------------------------    CREATE CO-ORDINATOR BY ADMIN    ------------------------------------- #

    def CreateCoordinator(self):
        self.cor_name = input('Name of Coordinator: ')
        self.cor_event = input('Coordinate which event: ')
        self.cor_pass = input('Set password: ')
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(
                [self.cor_name, self.cor_pass, 'Co-ordinator'])
        with open("/home/narayanj/Practice/THAR2.0/Admin/everyone.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(colored(' <--- New Coordinator added ---> !!!\n',
              'red', attrs=['reverse', 'blink']))
        print(x)

# -------------------------------------    ORGANISER CLASS    ------------------------------------- #


class Organiser:
    def __init__(self):

        self.temp_1 = input('Please enter your Name: ')

        for i in self.everyone_list:
            if i == self.temp_1:
                self.temp_2 = input('Please enter your password: ')
                for Pass in self.password_list:
                    if Pass == self.temp_2:
                        print('Role verified!!')
                    else:
                        print('Password incorrect')
            else:
                print('No role found with this name!')


if __name__ == "__main__":
    # Made a list of all the passwords saved in the csv to cross check the password at login time of login.
    password_list = []
    file_path = open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r')
    file = csv.DictReader(file_path)
    for col in file:
        password_list.append(col['Password'])

    # print(password_list)

    everyone_list = []
    file_path = open(
        '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r')
    file = csv.DictReader(file_path)
    for col in file:
        everyone_list.append(col['Name'])
    # print(everyone_list)

    temp_1 = input('Please enter your Name: ')
    temp_2 = input('Please enter your password: ')
    if temp_1.lower() == 'narayan' and temp_2 == 'admin123':
        obj = Admin()
    elif temp_1 in everyone_list and temp_2 in password_list:
        obj1 = Organiser()
    else:
        print('Incorrect name or password. Exiting...')