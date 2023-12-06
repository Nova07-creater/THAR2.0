import os
import csv
import pandas as pd
from prettytable import PrettyTable, from_csv, ALL
from termcolor import colored
import re

# -------------------------------------    PARTICIPANT CLASS    ------------------------------------- #

# Participant can do :
# 1) Change his password
# 2) Participate in Events, Exhibitions, Workshops, Pro-Nites.
# 3) Cancel participation from any at any time 
# 4) Read all his data
# 5) Read Events, Exhibitions, Workshops, Pro-Nites being organised in the fest


class Participant:
    def __init__(self):
        self.part_name = None
        self.part_pass = None

        while True:
            self.user_input = input(colored('''
                    Are you a new user? ''', 'grey', attrs = ["bold"])+ colored("""
                
                    1. Log in
                
                    2. Sign Up
                
                    Enter (1/2)` accordingly:  """, 'grey', attrs= ['bold']))
            if self.user_input == '1':
                self.old_participant()
                break
            elif self.user_input == '2':
                self.new_participant()
                break
            else:
                print(colored('''
                    Incorrect input...''', 'red', attrs=['bold']))
                continue
  
    
    def participant_personal_info(self):
       
        print(colored('''
                    Please provide your basic information:  ''', 'cyan', attrs = ['bold']))
        while True:
            participant_name = input(colored('''
                    Your Name:  ''', 'grey', attrs = ['bold']))
            if participant_name == self.part_name:
                break
            else:
                print(colored('''
                              
                    The name you entered doesn't match you entered earlier, Please re-enter.. ''', 'red', attrs =['bold']))
        participant_city = input(colored('''
                    Your City:  ''', 'grey', attrs = ['bold']))
        while True:
            participant_gender = input(colored('''
                    Enter your Gender (Male/Female): ''', 'grey', attrs=['bold']))
            if participant_gender.lower() in ['male', 'female']:
                break
            else:
                print(colored('''
                    Invalid gender. Please enter "Male" or "Female".''', 'red', attrs = ['bold']))
        while True:
            participant_mobile = input(colored('''
                    Enter your Mobile Number: ''', 'grey', attrs=['bold']))
            if re.match(r'^\d{10}$', participant_mobile):
                break
            else:
                print(colored('''
                    Invalid mobile number format. Please enter a 10-digit number.''', 'red', attrs =['bold']))
 
        while True:
            participant_email = input(colored('''
                    Enter your Email: ''', 'grey', attrs=['bold']))
            if re.match(r'^\S+@\S+\.\S+$', participant_email):
                break
            else:
                print(colored('''
                    Invalid email format. Please enter a valid email address.''', 'red', attrs = ['bold']))
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/partbasicdetails.csv', 'a', newline ='') as file:
            writer = csv.writer(file)
            is_file_empty = os.stat('/home/narayanj/Practice/THAR2.0/Admin/csvs/partbasicdetails.csv').st_size == 0
            if is_file_empty:
                writer.writerow(["Name", "Mobile Number", "Email", "City", "Gender"])
            writer.writerow([participant_name, participant_mobile, participant_email, participant_city, participant_gender])
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/partbasicdetails.csv', 'r') as file:
            x= from_csv(file)
            x.hrules = ALL
            print(x)
        print(colored('''
                    Thank you for providing your information. Your details have been stored.
    ''', 'green', attrs=['bold'])) 
    
    
    def new_participant(self):
        print('\n')
        
        
        self.part_name = input(colored('''
                    Enter Name:  ''','grey' ,attrs = ['bold']))
        self.part_pass = input(colored('''
                    Enter Password:  ''','grey' ,attrs = ['bold']))
        
        
        self.participant_personal_info() 
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/participants.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            is_file_empty = os.stat('/home/narayanj/Practice/THAR2.0/Admin/csvs/participants.csv').st_size == 0
            if is_file_empty:
                writer.writerow(["Name", "Password"])
            writer.writerow([self.part_name, self.part_pass])

    
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/participants.csv', "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(colored('New Participant added: ', 'green', attrs = ['bold']))
        print(x)
        print(colored(f'''
                      
                    Hello {self.part_name}, You are now logged in to your account..''', 'cyan', attrs = ['bold']))
        self.participant_operations()


    def old_participant(self):
        while True:
            self.part_name = input(colored('''
                    Enter Name:  ''', 'grey', attrs=['bold']))

            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/participants.csv', 'r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row['Name'] == self.part_name:
                        while True: 
                            self.part_pass = input(colored('''
                    Enter Password:  ''', 'grey', attrs=['bold']))

                            if row['Password'] == self.part_pass:
                                print(colored(f'''
                    Heartiest Welcome {self.part_name.upper()}, In our National Level Techno-Management Fest.
                    Please proceed further with the operations accordingly \U0001F607''', 'cyan', attrs=['bold']))
                                self.participant_operations()
                                return 

                            print(colored('''
                    Password didn't match. Enter again...''', 'red', attrs=['bold']))
                        
                        
                else:
                    print(colored('''   
                    Name didn't match. Enter again...''', 'red', attrs=['bold']))


    def participant_operations(self):
        while True:
            print('\n')
            user_input = input(colored('''      
                    What operation you want to preceed with?''', 'cyan', attrs = ['bold'])
                + colored('''    

                    1. READ 

                    2. PARTICIPATE

                    3. UPDATE
                                
                    4. DELETE

                    5. CHANGE PASSWORD
                        
                    6. EXIT
                    
                    7. SWITCH USER
                            
                    Enter your preffered operation: ''', 'grey', attrs= ['bold']))
            if user_input == '1':
                self.part_read()
            elif user_input == '2':
                self.participate()
            elif user_input == '3':
                self.update()
            elif user_input == '4':
                self.delete()
            elif user_input == '5':
                self.change_pass()    
            elif user_input == '6':
                break
                # self.exit()
            elif user_input == '7':
                pass
                # self.switch()
            else:
                print(colored(''''
                    Invalid input''', 'red', attrs = ['bold']))


# ---------------------------   CHANAGE PASSWORD   ------------------------------ #
 
    def change_pass(self):
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/participants.csv', 'r') as file:
            reader = csv.DictReader(file)
            participants_data = list(reader)
 
        participant_found = False
        for participant in participants_data:
            if participant['Name'] == self.part_name:
                participant_found = True
                self.part_pass = participant['Password']
                new_password = input(colored('Enter your new password: ', 'grey', attrs=['bold']))
               
                participant['Password'] = new_password
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/participants.csv', 'w', newline='') as file:
                    fieldnames = ['Name', 'Password']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(participants_data)
 
                print(colored('Password updated successfully!', 'green', attrs=['bold']))
                break
 
        if not participant_found:
            print(colored('''
                    Participant not found. Password not updated.''', 'red', attrs=['bold']))
    # def exit(self):
    #     print(colored(''' 
    #             Exiting from Participant operarions... ''', 'cyan', attrs = ['bold']))




  ########################################################################################################
  #                                                                                                      #
  #                             <--------- READ STARTED HERE --------->                                  #
  #                                                                                                      #
  ########################################################################################################

# -------------------------------------    READ EVENTS      ------------------------------------- #
    def part_read(self):
        self.user_input = input(colored("""  

                    How would you like to proceed? """, 'cyan', attrs = ['bold'])
                    + colored("""        
                
                    1. Read Event
                    
                    2. Read Exhibiution   
                    
                    3. Read Workshop
                    
                    4. Read Pro-Nite
                    
                    5. Read all your data

                    6. Back to main

                    Enter your preffered operation: """, 'grey', attrs = ['bold']))
        print('\n')

        if self.user_input == '1':
            self.part_read_event()
        elif self.user_input == '2':
            self.part_read_exhibition()
        elif self.user_input == '3':
            self.part_read_workshop()
        elif self.user_input == '4':
            self.part_read_pro_nite()
        elif self.user_input == '5':
            self.part_fetch_data()
        elif self.user_input == '6':
            self.back()
            return False
        else:
            print(colored('''
                    No such operation available !!''', 'red', attrs = ['bold']))


# -------------------------------------    READ EVENTS    ------------------------------------- #

    def part_fetch_data(self):
        print(colored('''
                    Your data with us ''',
              'green', attrs=['bold']))
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == self.part_name:
                    events = row['Event Participated']
                    print(colored(f'''
                    1. Events Participated: {events}''', attrs=['bold']))
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == self.part_name:
                    exhibitions_ = row['Exhibition Participated']
                    print(colored(f'''
                    2. Exhibitions Participated: {exhibitions_}''', attrs=['bold']))
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == self.part_name:
                    workshops = row['Workshop Participated']
                    print(colored(f'''
                    3. Workshops Participated: {workshops}''', attrs=['bold']))
        with open('participate_pro_nite.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == self.part_name:
                    pronite = row['Participate Pro-Nite (Yes/No)']
                    print(colored(f'''
                    4. Attending in Pro-Nite: {pronite}''', attrs=['bold']))
        personal_details = {}
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/partbasicdetails.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == self.part_name:
                    personal_details = row
        print('\n')
        print(colored('''
                    Personal Details ''', 'green', attrs=['bold']))
        for key, value in personal_details.items():
            print(colored(f"""
                {key.ljust(20)}: {value}""", attrs =['bold']))
            
            
# -------------------------------------    READ EVENTS    ------------------------------------- #

    def part_read_event(self):
        print(colored('The Events we are organising are: ',
              'cyan', attrs=['bold']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ EXHIBITON    ------------------------------------- #

    def part_read_exhibition(self):
        print(colored('The Exhibitions are scheduled as: ',
              'cyan', attrs=['bold']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ WORKSHOPS     ------------------------------------- #

    def part_read_workshop(self):
        print(colored('The Workshops are scheduled as : ',
              'cyan', attrs=['bold']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ PRO-NITES     ------------------------------------- #

    def part_read_pro_nite(self):
        print(colored('The Pro-Nites are scheduled as: ',
              'cyan', attrs=['bold']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)



  ##################################################################################################
  #                                                                                                #
  #                       <--------- PARTICIPATION STARTED HERE --------->                         #
  #                                                                                                #
  ##################################################################################################

# -------------------------------------    PARTICIPATE    ---------------------------------------- #




    def participate(self):
        self.user_input = input(colored("""  

                    How would you like to proceed? """, 'cyan', attrs = ['bold'])
                    + colored("""        
                    1. Participate in Event
                    
                    2. Participate in Exhibition   
                    
                    3. Participate in Workshop
                    
                    4. Participate in Pro-Nite

                    5. Back to main

                    Enter your preffered operation: """, 'grey', attrs = ['bold']))

        if self.user_input == '1':
            self.participate_event()
        elif self.user_input == '2':
            self.participate_exhibition()
        elif self.user_input == '3':
            self.participate_workshop()
        elif self.user_input == '4':
            self.participate_pro_nite()
        elif self.user_input == '5':
            self.back()
            return False
        else:
            print(colored('''
                    No such operation available !!''', 'red', attrs = ['bold']))
    def back(self):
        print(colored('''
                    Going back to main crud... ''', 'cyan'))



# ---------------------------    PARTICIPATE IN EVENT    ------------------------------ #


    def participate_event(self):
        if not os.path.exists("/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv"):
            with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Event Participated"])

        try:
            with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv", "r", newline="") as file:
                reader = csv.reader(file)
                participate_data = list(reader)

        except FileNotFoundError:
            print("Error: /home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv not found.")
            return

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'r', newline="") as file:
            x = from_csv(file)
            x.hrules =ALL            
            print(colored('''
                    The Events you can participate in are:''', 'cyan', attrs=['bold']))
            print(x)

        num_events = int(input(colored("""
                    Enter the number of events you want to register for: """, 'grey', attrs = ['bold'])))

        participant_index = None
        current_events = []
        for i, row in enumerate(participate_data):
            if row[0] == self.part_name:
                participant_index = i
                current_events = row[1].split(", ")
                break

        for i in range(num_events):
            while True:
                event_name = input(colored(f"""
                    Enter the name of event {i + 1}: """, 'grey', attrs = ['bold']))

                if event_name in current_events:
                    print(colored("""
                    You have already registered in this event. Please enter a different event.""", 'red', attrs =['bold']))
                    continue

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv", "r", newline="") as file:
                    events_reader = csv.reader(file)
                    events_data = list(events_reader)

                if event_name not in [row[0] for row in events_data]:
                    print(colored("""
                    The event is not present. Please enter a correct event name.""", 'red', attrs = ['bold']))
                    continue

                break

            if participant_index is not None:
                participate_data[participant_index][1] += f", {event_name}"
            else:
                participate_data.append([self.part_name, event_name])

        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(participate_data)
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv", 'r') as file:
            x = from_csv(file)
            x.hrules =ALL
            print(colored("""Registration successful!""", 'green', attrs = ['bold']))
            print(x)



 
# ---------------------------    PARTICIPATE IN EXHIBITION    ------------------------------ #



    def participate_exhibition(self):

        if not os.path.exists("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv"):
            with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Exhibition Participated"])

        try:
            with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv", "r", newline="") as file:
                reader = csv.reader(file)
                participate_data = list(reader)

        except FileNotFoundError:
            print("Error: /home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv not found.")
            return

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv', 'r', newline="") as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('''
                The Exhibitions you can participate in are:''', 'cyan', attrs=['bold']))
            print(x)

        num_exhibitions = int(input(colored("""
                Enter the number of exhibitions you want to register for: """, 'grey', attrs = ['bold'])))

        participant_index = None
        current_exhibitions = []
        for i, row in enumerate(participate_data):
            if row[0] == self.part_name:
                participant_index = i
                current_exhibitions = row[1].split(", ")
                break

        for i in range(num_exhibitions):
            while True:
                ex_name = input(colored(f"""
                Enter the name of Exhibition {i + 1}: """))

                if ex_name in current_exhibitions:
                    print(colored("""
                You have already registered in this Exhibition. Please enter a different Exhibition.""", 'grey', attrs =['bold']))
                    continue

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibions.csv", "r", newline="") as file:
                    exhibitions_reader = csv.reader(file)
                    exhibiton_data = list(exhibitions_reader)

                if ex_name not in [row[0] for row in exhibiton_data]:
                    print(colored("""
                The exhibition is not present. Please enter a correct exhibition name.""", 'red', attrs =['bold']))
                    continue

                break

            if participant_index is not None:
                participate_data[participant_index][1] += f", {ex_name}"
            else:
                participate_data.append([self.part_name, ex_name])

        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(participate_data)
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv", "r") as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored("""Registration successful!""", 'green', attrs = ['bold']))
            print(x)

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('All Participants in Exhibitons:', 'green', attrs=['bold']))
            print(x)


   
# ---------------------------    PARTICIPATE IN WORKSHOP    ------------------------------ #
 
    def participate_workshop(self):

        if not os.path.exists("/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv"):
            with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Workshop Participated"])

        try:
            with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv", "r", newline="") as file:
                reader = csv.reader(file)
                participate_data = list(reader)

        except FileNotFoundError:
            print("Error: /home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv not found.")
            return

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv', 'r', newline="") as file:
            x = from_csv(file)
            x.hrules =ALL
            print(colored('''The Workshops you can participate in are:''', 'cyan', attrs=['bold']))
            print(x)

        num_workshops = int(input(colored("""
                Enter the number of workshops you want to register for: """, 'grey', attrs =['bold'])))
        participant_index = None
        current_workshops = []
        for i, row in enumerate(participate_data):
            if row[0] == self.part_name:
                participant_index = i
                current_workshops = row[1].split(", ")
                break

        for i in range(num_workshops):
            while True:

                workshop_name = input(colored(f"""
                Enter the name of workshop {i + 1}: """, 'grey', attrs = ['bold']))
                if workshop_name in current_workshops:
                    print(colored("""
                You have already registered in this workshop...""", 'red', attrs = ['bold']))
                    continue

                with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv", "r", newline="") as file:
                    exhibitions_reader = csv.reader(file)
                    workshops_data = list(exhibitions_reader)

                if workshop_name not in [row[0] for row in workshops_data]:
                    print(colored("""
                The workshop is not present...""", 'red', attrs = ["bold"]))
                    continue

                break

            if participant_index is not None:
                participate_data[participant_index][1] += f", {workshop_name}"
            else:
                participate_data.append([self.part_name, workshop_name])

        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(participate_data)
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv", "r") as file:
            x = from_csv(file)
            x.hrules = ALL
            print("Registration successful!")
            print(x)
 
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('All Participants in workshops:', 'green', attrs=['bold']))
            print(x)
 

  
# ---------------------------    PARTICIPATE IN PRO-NITE    ------------------------------ #
  
  
    def participate_pro_nite(self):
        print(colored('''The Pro-Nites you can participate in are: ''', 'cyan', attrs=['bold']))

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/pronite.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(x)
        if not os.path.exists("/home/narayanj/Practice/THAR2.0/Admin/csvs/participate_pro_nite.csv"):
            with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/participate_pro_nite.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Participate Pro-Nite (Yes/No)"])

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/participate_pro_nite.csv', 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == self.part_name:
                    print('You have already given your choice...')
                    return  

            yesORno = input(colored('''
                        Want to attend Pro-Nites (Yes/No)
                        
                        1) Yes
                        2) No
                        
                        Enter your preference: ''', 'grey', attrs=['bold']))

            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/participate_pro_nite.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                is_file_empty = os.stat('/home/narayanj/Practice/THAR2.0/Admin/csvs/participate_pro_nite.csv').st_size == 0
                if is_file_empty:
                    writer.writerow(["Name", "Participate Pro-Nite (Yes/No)"])
                writer.writerow([self.part_name, 'Yes' if yesORno == '1' else 'No'])

            with open('participate_pro_nite.csv', 'r') as file:
                x = from_csv(file)
                x.hrules = ALL
                print(colored('Participant details:', 'green', attrs=['bold']))
                print(x)

            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/participants.csv', 'r') as file:
                x = from_csv(file)
                x.hrules = ALL

                print(colored('All Participants:', 'green', attrs=['bold']))
                print(x)


 

  ##################################################################################################
  #                                                                                                #
  #                       <--------- DELETION STARTED HERE --------->                              #
  #                                                                                                #
  ##################################################################################################

# -------------------------------------    PARTICIPATE    ---------------------------------------- #




    def delete(self):
        self.user_input = input(colored("""  

                From which activity you want to remove your participation? """, 'cyan', attrs = ['bold'])
                + colored("""        
                
                1. From Event
                
                2. From Exhibition   
                
                3. From Workshop
                
                4. Back to main

                Enter your preffered operation: """, 'grey', attrs = ['bold']))

        if self.user_input == '1':
            self.from_event()
        elif self.user_input == '2':
            self.from_exhibition()
        elif self.user_input == '3':
            self.from_workshop()
        elif self.user_input == '4':
            self.back()
            return False
        else:
            print(colored('''
               No such operation available !!''', 'red', attrs = ['bold']))
    def back(self):
        print(colored('''
                Going back to main crud... ''', 'cyan'))




# -------------------------------------    REMOVE FROM EVENT    ------------------------------------- #

    def from_event(self):
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['Name'] == self.part_name:
                    events = row['Event Participated']

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Events participated: ', 'green', attrs=['bold']))
            print(x)

        print('\n')
        print(colored('The events you have registered are: ', 'green', attrs=['bold']))
        print(events)

        events_list = [event.strip() for event in events.split(',')]

        while True:
            rem_event = input('Which event you want to remove: ')
            if rem_event in events_list:
                events_list.remove(rem_event)
                events = ', '.join(events_list)
                break
            else:
                print('Event not found. Try again...')
                continue
        print(colored('Updated events after removal: ', 'green', attrs=['bold']))
        print(events)

        rows = []
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv', 'r') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames

            for row in reader:
                if row['Name'] == self.part_name:
                    row['Event Participated'] = events
                rows.append(row)

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
                

# -------------------------------------    REMOVE FROM EXHIBITIONS    ------------------------------------- #

    def from_exhibition(self):
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['Name'] == self.part_name:
                    exhibitions = row['Exhibition Participated']

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Exhibitions participated: ', 'green', attrs=['bold']))
            print(x)

        print('\n')
        print(colored('The exhibition you have registered are: ', 'green', attrs=['bold']))
        print(exhibitions)

        exhibitions_list = [exhibitions.strip() for event in exhibitions.split(',')]

        while True:
            rem_event = input('Which event you want to remove: ')
            if rem_event in exhibitions_list:
                exhibitions_list.remove(rem_event)
                events = ', '.join(exhibitions_list)
                break
            else:
                print('Exhibition not found. Try again...')
                continue
        print(colored('Updated exhibitions after removal: ', 'green', attrs=['bold']))
        print(exhibitions)

        rows = []
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv', 'r') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames

            for row in reader:
                if row['Name'] == self.part_name:
                    row['Exhibition Participated'] = exhibitions
                rows.append(row)

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/exhibition_participate.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)



# -------------------------------------    REMOVE FROM WORKSHOPS    ------------------------------------- #

    def from_workshop(self):
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['Name'] == self.part_name:
                    workshops = row['Workshop Participated']

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Workshops participated: ', 'green', attrs=['bold']))
            print(x)

        print('\n')
        print(colored('The workshops you have registered are: ', 'green', attrs=['bold']))
        print(workshops)

        workshops_list = [workshops.strip() for event in workshops.split(',')]

        while True:
            rem_workshop = input('Which workshop you want to remove: ')
            if rem_workshop in workshops_list:
                workshops = ', '.join(workshops_list)
                workshops_list.remove(rem_workshop)
                break
            
            else:
                print('Event not found. Try again...')
                continue
        print(colored('Updated workshops after removal: ', 'green', attrs=['bold']))
        print(workshops)

        rows = []
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv', 'r') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames

            for row in reader:
                if row['Name'] == self.part_name:
                    row['Workshop Participated'] = workshops
                rows.append(row)

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
