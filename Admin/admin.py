import os
import csv
from prettytable import PrettyTable
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
            print('Choose correct option!!')


# -------------------------------------    CREATE EVENTS BY ADMIN    ------------------------------------- #

    def CreateEvent(self):
        self.event_name = input('Event name: ')
        self.event_venue = input('Event place: ')
        self.event_time = input('Event Time: ')
        print('Event created succesfully')
        self.path = "/home/narayanj/Practice/THAR2.0/Admin/events.csv"
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(
                [self.event_name, self.event_venue, self.event_time])


# -------------------------------------    CREATE JUDGES BY ADMIN    ------------------------------------- #

    def CreateJudge(self):
        self.judge_name = input('Judge name: ')
        self.judge_event_name = input('Event to be Judged: ')
        self.judge_pass = input('Set password: ')
        print('Judge created succesfully')
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow([self.judge_name, self.judge_pass, 'Judge'])


# -------------------------------------    CREATE EXHIBITIONS BY ADMIN    ------------------------------------- #

    def CreateExhibition(self):
        self.ex_name = input('Set exhibition name: ')
        self.ex_venue = input('Exhibition place: ')
        self.ex_time = input('What will be time: ')
        print('Exhibition created succesfully')
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
        print('Wrokshop created succesfully')
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/wrokshops.csv'
        file_empty = os.stat(self.path).st_size == 0
        if file_empty:
            self.writer.writerow(['Workshop', 'Venue', 'Time'])
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(
                [self.work_name, self.work_venue, self.work_time])
        self.z = PrettyTable()
        self.z.field_names = ['Workshop', 'Venue', 'Time']
        self.z.add_row([self.work_name, self.work_venue, self.work_time])
        print(self.z)


# -------------------------------------    CREATE PRO-NITES BY ADMIN    ------------------------------------- #

    def CreateProNite(self):
        self.name_pro_nite = input('Set "Pro Nite" name: ')
        self.pro_venue = input('Where it will be helo: ')
        self.pro_time = input('What time will it start: ')
        self.pro_date = input('Date of pro-nite being organised: ')
        print('Pro-Nite created succesfully')
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/pronite.csv'

        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            is_file_empty = os.stat(self.path).st_size == 0
            if is_file_empty:
                self.writer.writerow(['Pro Nite', 'Venue', 'Time', 'Date'])
            self.writer.writerow(
                [self.name_pro_nite, self.pro_venue, self.pro_time, self.pro_date])


# -------------------------------------    CREATE ORGANISER BY ADMIN    ------------------------------------- #

    def CreateOrganiser(self):
        self.org_name = input('Name of Organiser: ')
        self.org_pass = input('Set Password: ')
        print('Organiser created succesfully')
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow([self.org_name, self.org_pass, 'Organiser'])


# -------------------------------------    CREATE CO-ORDINATOR BY ADMIN    ------------------------------------- #

    def CreateCoordinator(self):
        self.cor_name = input('Name of Coordinator: ')
        self.cor_event = input('Coordinate which event: ')
        self.path = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(
                [self.cor_name, self.cor_event, 'Co-ordinator'])
        

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

    print(password_list)

    everyone_list = []
    file_path = open(
        '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r')
    file = csv.DictReader(file_path)
    for col in file:
        everyone_list.append(col['Name'])
    print(everyone_list)

    temp_1 = input('Please enter your Name: ')
    temp_2 = input('Please enter your password: ')
    if temp_1.lower() == 'narayan' and temp_2 == 'admin123':
        obj = Admin()
    elif temp_1 in everyone_list and temp_2 in password_list:
        obj1 = Organiser()
    else:
        print('Incorrect name or password. Exiting...')
