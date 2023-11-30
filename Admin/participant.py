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
# 6) Update his/her details


class Participant:
    def __init__(self):
        self.user_input = input(colored('''
                Are you a new user? ''', 'grey', attrs = ["bold"])+ colored("""
            
                1. Log in
            
                2. Sign Up
            
                Enter (1/2) accordingly:  """, 'grey', attrs= ['bold']))
        if self.user_input == '1':
            self.part_name = input(colored('''
                Enter Name:  ''', 'grey',attrs = ['bold']))
            self.part_pass = input(colored('''
                Enter Password:  ''', 'grey' ,attrs = ['bold']))
            self.old_participant()
        elif self.user_input == '2':
            self.part_name = input(colored('''
                Enter Name:  ''','grey' ,attrs = ['bold']))
            self.part_pass = input(colored('''
                Enter Password:  ''','grey' ,attrs = ['bold']))
            self.new_participant()
        else:
            print('''Incorrect input...''', 'red', attrs=['bold'])
  
  
    
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
        with open('partbasicdetails.csv', 'a', newline ='') as file:
            writer = csv.writer(file)
            is_file_empty = os.stat('partbasicdetails.csv').st_size == 0
            if is_file_empty:
                writer.writerow(["Name", "Mobile Number", "Email", "City", "Gender"])
            writer.writerow([participant_name, participant_mobile, participant_email, participant_city, participant_gender])
        with open('partbasicdetails.csv', 'r') as file:
            x= from_csv(file)
            x.hrules = ALL
            print(x)
        print(colored('''
        Thank you for providing your information. Your details have been stored.
    ''', 'green', attrs=['bold'])) 
    
    
    def new_participant(self):
        print('\n')
        self.participant_personal_info() 
        with open('/home/narayanj/Practice/THAR2.0/Admin/participants.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            is_file_empty = os.stat('/home/narayanj/Practice/THAR2.0/Admin/participants.csv').st_size == 0
            if is_file_empty:
                writer.writerow(["Name", "Password"])
            writer.writerow([self.part_name, self.part_pass])

    
        with open('/home/narayanj/Practice/THAR2.0/Admin/participants.csv', "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
        print(colored('New Participant added: ', 'green', attrs = ['bold']))
        print(x)
        print(colored(f'''
                Hello {self.part_name}, You are now logged in to your account..''', 'cyan', attrs = ['bold']))
        self.participant_operations()


    def old_participant(self):
        with open('participants.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == self.part_name and row['Password'] == self.part_pass:
                    print(colored(f'''
                Hearttiest Welcome {self.part_name}, In our National Level Techno-Management Fest Please proceed further with the operations accordingly \U0001F607''', 'cyan', attrs = ['bold'])) 
                    self.participant_operations()
                elif row['Name'] == self.part_name and row['Password'] != self.part_pass:
                    user_input = input(colored('''
                Forgot Password... ''', 'cyan', attrs = ['bold']) + colored('''
                
                1. YES
                
                2. NO 
            
                If so we may let you proceed towards rest password''', 'grey', attrs = ['bold']))
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
                self.exit()
                break
            elif user_input == '7':
                pass
                # self.switch()
            else:
                print(colored(''''
                Invalid input''', 'red', attrs = ['bold']))

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
    #         if user_input == '1':
    #             self.authenticate_user()
    #         elif user_input == '2':
    #             self.authenticate_user()
    #         elif user_input == '3':
    #             self.authenticate_user()
    #         elif user_input == '4':
    #             self.authenticate_user()
    #         elif user_input == '5':
    #             self.authenticate_user()    
    #         elif user_input == '6':
    #             self.exit()
    #             break 
    #         else:
    #             print(colored(''''
    #             Invalid input''', 'red', attrs = ['bold']))





# ---------------------------   CHANAGE PASSWORD   ------------------------------ #
 
    def change_pass(self):
        with open('participants.csv', 'r') as file:
            reader = csv.DictReader(file)
            participants_data = list(reader)
 
        participant_found = False
        for participant in participants_data:
            if participant['Name'] == self.part_name:
                participant_found = True
                self.part_pass = participant['Password']
                new_password = input(colored('Enter your new password: ', 'grey', attrs=['bold']))
               
                participant['Password'] = new_password
                with open('participants.csv', 'w', newline='') as file:
                    fieldnames = ['Name', 'Password']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(participants_data)
 
                print(colored('Password updated successfully!', 'green', attrs=['bold']))
                break
 
        if not participant_found:
            print(colored('Participant not found. Password not updated.', 'red', attrs=['bold']))
    def exit(self):
        print(colored(''' 
                Exiting from Participant operarions... ''', 'cyan', attrs = ['bold']))



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
        print(colored('Your data with us: ',
              'cyan', attrs=['bold']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/events.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ EVENTS    ------------------------------------- #

    def part_read_event(self):
        print(colored('The Events we are organising are: ',
              'cyan', attrs=['bold']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/events.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ EXHIBITON    ------------------------------------- #

    def part_read_exhibition(self):
        print(colored('The Exhibitions are scheduled as: ',
              'cyan', attrs=['bold']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ WORKSHOPS     ------------------------------------- #

    def part_read_workshop(self):
        print(colored('The Workshops are scheduled as : ',
              'cyan', attrs=['bold']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/wrokshops.csv", "r") as fp:
            x = from_csv(fp)
            x.hrules = ALL
            print(x)

# -------------------------------------    READ PRO-NITES     ------------------------------------- #

    def part_read_pro_nite(self):
        print(colored('The Pro-Nites are scheduled as: ',
              'cyan', attrs=['bold']))
        with open("/home/narayanj/Practice/THAR2.0/Admin/pronite.csv", "r") as fp:
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

        print(colored('''The Events you can participate in are:''', 'cyan', attrs=['bold']))

        with open('/home/narayanj/Practice/THAR2.0/Admin/events.csv', 'r') as file:
           x = from_csv(file)
           print(x)
        num_events = int(input(colored('''
                Number of events you want to participate:  ''', 'grey', attrs=['bold'])))
        
        # with open('/home/narayanj/Practice/THAR2.0/Admin/participate_events.csv', 'r') as file:
        #     reader = csv.DictReader(file)
        #     data = list(reader)

        #     for row in data:
        #         if row['Name'] == self.part_name and  len(data[row]) !=2:
        #             pass
        events_list = []

        for _ in range(num_events):
            user_input_event = input(colored('''
            Enter event name you want to participate:  ''', 'grey', attrs=['bold']))
            events_list.append(user_input_event)


        is_participant_present = False
        with open('/home/narayanj/Practice/THAR2.0/Admin/participate_events.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # header row ko skip karne ke liye
            for row in reader:
                if row[0] == self.part_name:
                    is_participant_present = True
                    row[1] = eval(row[1]) + events_list
            print(row[1])
            # with open('/home/narayanj/Practice/THAR2.0/Admin/participate_events.csv', 'a') as file:
            #     writer = csv.writer(file)
            #     writer.writerow([self.part_name, row[1]])            

                
        if not is_participant_present:
            with open('/home/narayanj/Practice/THAR2.0/Admin/participate_events.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                if os.stat('/home/narayanj/Practice/THAR2.0/Admin/participate_events.csv').st_size == 0:
                    writer.writerow(["Name", "Event Participated"])
                writer.writerow([self.part_name, events_list])

        with open('/home/narayanj/Practice/THAR2.0/Admin/participate_events.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(x)


 
# ---------------------------    PARTICIPATE IN EXHIBITION    ------------------------------ #



    def participate_exhibition(self):
        print(colored('''The Exhibitions you can participate in are:''', 'cyan', attrs=['bold']))

        with open('/home/narayanj/Practice/THAR2.0/Admin/exhibions.csv', 'r') as file:
           x = from_csv(file)
           print(x)
        num_exhibitions = int(input(colored('''
                Number of exhibitions you want to participate:  ''', 'grey', attrs=['bold'])))
        exhibitions_list = []

        for _ in range(num_exhibitions):
            user_input_exhibition = input(colored('''
            Enter exhibition name you want to participate:  ''', 'grey', attrs=['bold']))
            exhibitions_list.append(user_input_exhibition)


        is_participant_present = False
        if os.path.exists('participate_exhibitions.csv'):
            with open('participate_exhibitions.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    if row[0] == self.part_name:
                        is_participant_present = True
                        # Update the existing row with new exhibitions
                        row[1] = eval(row[1]) + exhibitions_list
                

                
        if not is_participant_present:
            with open('participate_exhibitions.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                if os.stat('participate_exhibitions.csv').st_size == 0:
                    writer.writerow(["Name", "Exhibition Participated"])
                writer.writerow([self.part_name, exhibitions_list])

        with open('participate_exhibitions.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(x)

        with open('participants.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('All Participants:', 'green', attrs=['bold']))
            print(x)


   
# ---------------------------    PARTICIPATE IN WORKSHOP    ------------------------------ #
 
    def participate_workshop(self):
        print(colored('''The Workshops you can participate in are:''', 'cyan', attrs=['bold']))

        with open('/home/narayanj/Practice/THAR2.0/Admin/wrokshops.csv', 'r') as file:
           x = from_csv(file)
           print(x)
        num_workshop = int(input(colored('''
                Number of workshop you want to participate:  ''', 'grey', attrs=['bold'])))
        workshop_list = []

        for _ in range(num_workshop):
            user_input_workshop = input(colored('''
            Enter workshop name you want to participate:  ''', 'grey', attrs=['bold']))
            workshop_list.append(user_input_workshop)

       

        is_participant_present = False
        if os.path.exists('participate_workshop.csv'):
            with open('participate_workshop.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    if row[0] == self.part_name:
                        is_participant_present = True
                        row[1] = eval(row[1]) + workshop_list
                
        if not is_participant_present:
            with open('participate_workshop.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                if os.stat('participate_workshop.csv').st_size == 0:
                    writer.writerow(["Name", "Workshop Participated"])
                writer.writerow([self.part_name, workshop_list])

        with open('participate_workshop.csv', 'r') as file:
            x = PrettyTable()
            x = from_csv(file)
            x.hrules = ALL
            print(x)

        # with ('participants.csv', 'r') as file:
        #     x = from_csv(file)
        #     x.hrules = ALL
        #     print(colored('All Participants:', 'green', attrs=['bold']))
        #     print(x)
 
 
 
 
# ---------------------------    PARTICIPATE IN PRO-NITE    ------------------------------ #
  
  
    def participate_pro_nite(self):
 
        print(colored('''The Pro-Nite you can participate are: ''', 'cyan', attrs = ['bold']))
 
        with open('/home/narayanj/Practice/THAR2.0/Admin/pronite.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(x)
        yesORno = input(colored('''
                Want to attend Pro-Nites (Yes/No)
               
                1) Yes
               
                2) No
               
                Enter your preference: ''', 'grey', attrs = ['bold']))
        if yesORno == '1':
            with open('participate_pro_nite.csv', 'a', newline = '') as file:
                writer = csv.writer(file)
                is_file_empty = os.stat('participate_pro_nite.csv').st_size == 0
                if is_file_empty:
                    writer.writerow(["Name", "Participate Pro-Nite (Yes/No)"])
                writer.writerow([self.part_name, 'Yes'])
        else:
            with open('participate_pro_nite.csv', 'a', newline = '') as file:
                writer = csv.writer(file)
                is_file_empty = os.stat('participate_exhibitions.csv').st_size == 0
                if is_file_empty: 
                    writer.writerow(["Name", "Participate Pro-Nite (Yes/No)"])
                writer.writerow([self.part_name, 'No'])
           
        with open('participate_pro_nite.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Participant details:', 'green', attrs = ['bold']))
            print(x)
 
        with open('/home/narayanj/Practice/THAR2.0/Admin/participants.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
 
            print(colored('All Participants:', 'green', attrs = ['bold']))
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
                
                4. From Pro-Nite

                5. Back to main

                Enter your preffered operation: """, 'grey', attrs = ['bold']))

        if self.user_input == '1':
            self.from_event()
        elif self.user_input == '2':
            self.from_exhibition()
        elif self.user_input == '3':
            self.from_workshop()
        elif self.user_input == '4':
            self.from_pro_nite()
        elif self.user_input == '5':
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



