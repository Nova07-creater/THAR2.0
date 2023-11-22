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
        print(colored('Welcome Narayan, Admin Detected!!', 'cyan'))
        self.crud()
    def crud(self):
        user_input = input('''
                What operation you want to preceed with?
                    
                1. Creation

                2. Updation

                3. Removal
                
                ''')
        if user_input == '1':
            self.creation()

        elif user_input == '2':
            self.Updation()
        elif user_input == '3':
            self.Removal()
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
        elif user_input == '7':
            self.update_judge()
        else:
            print(colored('No such operation available !!', 'red'))


    def Removal(self):
        user_input = input("""  

                How would you like to proceed?
                        
                1. Remove Event
                
                2. Remove Exhibiution   
                
                3. Remove Workshop
                
                4. Remove Pro-Nite
                
                5. Remove Organiser
                
                6. Remove Event Co-ordinator 
                
                7. Remove Judge                     
                """)

        if user_input == '1':
            self.remove_event()
        elif user_input == '2':
            pass
            # self.remove_exhibition()
        elif user_input == '3':
            pass
            # self.remove_workshop()
        elif user_input == '4':
            pass
            # self.remove_pro_nite()
        elif user_input == '5':
            pass
            # self.remove_organiser()
        elif user_input == '6':
            pass
            # self.remove_event_coordinator()
        elif user_input == '7':
            pass
            # self.remove_remove_judge()
        else:
            print('No such operation available !!')

# -------------------------------------    REMOVE EVENTS BY ADMIN    ------------------------------------- #
    def remove_event(self):
        file_path = '/home/narayanj/Practice/THAR2.0/Admin/events.csv'
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            event_name_list = []
            for col in reader:
                event_name_list.append(col['Event Name'])
        
        
        for i,item in enumerate(event_name_list):
            print(f'{i+1}.{item}\n')        
        ch_event = input((colored('Which event you want to remove: \n', 'yellow') ))     
        if ch_event in event_name_list:     
            index_to_remove = event_name_list.index(ch_event)
            event_name_list.pop(index_to_remove)

            with open(file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames = reader.fieldnames)
                writer.writeheader()
                writer.writerows(event_name_list)
            print(colored('Events has been removed', 'green'))
            with open("/home/narayanj/Practice/THAR2.0/Admin/events.csv", "r") as fp:
                x = from_csv(fp)
                x.hrules = ALL
                print(colored('Events after update are as follows: \n'))
                print(x)              

        else:
            print(colored('The entered event not found ', 'red'))

# -------------------------------------    UPDATE EVENTS BY ADMIN    ------------------------------------- #

    def update_event(self):
        self.event_attributes_list = ['Event Name', 'Venue', 'Time']
        print(colored('The attributes which are available to update are: \n', 'yellow'))
        for i, item in enumerate(self.event_attributes_list):
            print(f'{i+1}. {item}\n')
        self.user_input = input(colored('What do you want to update? \n', 'yellow'))

        if self.user_input == '1':
            
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/events.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                event_name_list = []
                for col in reader:
                    event_name_list.append(col['Event Name'])
           
           
            for i,item in enumerate(event_name_list):
                print(f'{i+1}.{item}\n')
           
           
            ch_event = input((colored('Which event name you want to change: ', 'yellow') ))     
            if ch_event in event_name_list:
                chd_event = input(colored('Enter the event name reaplace value: ', 'yellow'))
                
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
                print(colored('The entered event', {ch_event},'not found ', 'red'))



        elif self.user_input == '2':

            file_path = '/home/narayanj/Practice/THAR2.0/Admin/events.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                venue_list = []
                for col in reader:
                    venue_list.append(col['Venue'])
           
           
            for i,item in enumerate(venue_list):
                print(f'{i+1}.{item}\n')
           
           
            ch_venue = input((colored('Which venue you want to change: ', 'yellow') ))     
            if ch_venue in venue_list:
                chd_venue = input(colored('Enter the event name reaplace value: ', 'yellow'))
                
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
                print(colored('The entered venue', {ch_event},'not found ', 'red'))




        elif self.user_input == '3':
            file_path = '/home/narayanj/Practice/THAR2.0/Admin/events.csv'
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                time_list = []
                for col in reader:
                    time_list.append(col['Time'])
           
           
            for i,item in enumerate(time_list):
                print(f'{i+1}.{item}\n')
           
           
            ch_time = input((colored('What time you want to change: ', 'yellow') ))     
            if ch_time in time_list:
                chd_time = input(colored('Enter the time reaplace value: ', 'yellow'))
                
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
                print(colored('The entered venue', {ch_event},'not found ', 'red'))

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
            pass
        elif self.user_input == '2':
            pass
        elif self.user_input == '3':
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


# -------------------------------------    UPDATE ORGANISER BY ADMIN    ------------------------------------- #

    def update_organiser(self):
        self.organiser_attributes_list = ['Organiser Name', 'Password']
        print(colored('The attributes which are available to update are: \n'))

        for i, item in enumerate(self.organiser_attributes_list):
            print(f"{i+1}.{item}")
        self.user_input = input('What do you want to update? ')

        if self.user_input == '1':
            pass
        elif self.user_input == '2':
            pass
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
            pass
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


# -------------------------------------    CREATE EVENTS BY ADMIN    ------------------------------------- #

    def create_event(self):
        self.event_name = input('Event name: ')
        self.event_venue = input('Event place: ')
        self.event_time = input('Event Time: ')
        print(colored('Event created succesfully', 'green'))
        self.path = "/home/narayanj/Practice/THAR2.0/Admin/events.csv"
        self.is_file_empty = os.stat(file_path).st_size == 0
        if self.is_file_empty:
            self.writer.writerow(["Event Name", "Venue", "Time"])
        with open(self.path, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(
                [self.event_name, self.event_venue, self.event_time])

        with open("/home/narayanj/Practice/THAR2.0/Admin/events.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(x)

# -------------------------------------    CREATE JUDGES BY ADMIN    ------------------------------------- #

    def create_judge(self):
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
            x.hrules = ALL
        print(x)

# -------------------------------------    CREATE EXHIBITIONS BY ADMIN    ------------------------------------- #

    def create_exhibition(self):
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

    def create_event_coordinator(self):
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
        name = input("Please enter your Name: ")
        password = input("Please enter your password: ")

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

# if __name__ == "__main__":
#     # Made a list of all the passwords saved in the csv to cross check the password at login time of login.
#     password_list = []
#     file_path = open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r')
#     file = csv.DictReader(file_path)
#     for col in file:
#         password_list.append(col['Password'])

#     # print(password_list)

#     everyone_list = []
#     file_path = open(
#         '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r')
#     file = csv.DictReader(file_path)
#     for col in file:
#         everyone_list.append(col['Name'])
#     # print(everyone_list)

#     temp_1 = input('Please enter your Name: ')
#     temp_2 = input('Please enter your password: ')
#     if temp_1.lower() == 'narayan' and temp_2 == 'admin123':
#         obj = Admin()
#     elif temp_1 in everyone_list and temp_2 in password_list:
#         obj1 = Organiser()
#     else:
#         print('Incorrect name or password. Exiting...')