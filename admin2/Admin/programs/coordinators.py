import os
import csv
from prettytable import from_csv, ALL
from termcolor import colored
 
class Coordinator:
    def __init__(self, part_name):
        self.part_name = part_name
        self.coordinator_operations()
 
    def coordinator_operations(self):
        while True:
            user_input = input(colored('''
                Coordinator Operations ''', 'cyan', attrs=['bold'])
                + colored('''
               
                1. Budget & Volunteers for Event
               
                2. Change Password
               
                3. Read Participant Details of Event
                              
                4. Remove Participant
               
                5. Logout
               
                Enter your preferred choice:  ''', 'grey', attrs=['bold']))
 
            if user_input == '1':
                self.give_req()
            elif user_input == '2':
                self.change_password()
            elif user_input == '3':
                self.read_participant_details()
            elif user_input == '4':
                self.remove_participant()
            elif user_input == '5':
                print(colored('''
                Logout successful.''', 'green', attrs=['bold']))
                break
            else:
                print(colored('Invalid choice. Please enter a valid number.', 'red', attrs=['bold']))
 

 

# -------------------------------------    Give Budget for Event    ---------------------------------------- #

    def give_req(self):

        
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv", 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('The Events being organised are: ', 'green', attrs = ['bold']))
            print(x)
   
        budget_csv_path = "/home/narayanj/Practice/THAR2.0/Admin/csvs/budget.csv"
        detailed_event_csv = "/home/narayanj/Practice/THAR2.0/Admin/csvs/event_details.csv"
        if not os.path.exists(budget_csv_path):
            with open(budget_csv_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Coordinator", "Event Name", "Budget"])
        event = []
       
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == self.part_name:
                    event = row[1]
        print(colored(f'''
                {self.part_name} you have already been alloted an Event i.e. :  {event} ''', 'green', attrs = ['bold']))

        budget = int(input(colored('''
                What is the budget for your event:  ''', 'grey', attrs=['bold'])))
        num_vol = int(input(colored('''
                Number of Volunteers required:  ''', 'grey', attrs=['bold'])))
        with open(budget_csv_path, 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print('\n')
            print(colored(f'{event}\'s budget before any change', 'green', attrs =['bold']))
            print(x)
            print('\n')
        
        rows = [] 
        with open(budget_csv_path, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        coordinator_found = False
        for row in rows:
            if row and row[0] == self.part_name:
                row[2] = budget
                coordinator_found = True
                break

        if not coordinator_found:
            rows.append([self.part_name, event, budget])

        with open(budget_csv_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        with open(budget_csv_path, 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored(f'{event}\'s budget has been updated', 'green', attrs =['bold']))
            print(x)

        
        if not os.path.exists(budget_csv_path):
            with open(budget_csv_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Coordinator", "Event Name", "Budget"])
        
        
        partis_list = []             
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if event in row[1]:
                    partis_list.append(row[0])
        partis = partis_list

        detailed_event_csv = "/home/narayanj/Practice/THAR2.0/Admin/csvs/event_details.csv"
        with open(detailed_event_csv, "w", newline="") as file:
            writer = csv.writer(file)
            is_file_empty = os.stat(detailed_event_csv).st_size ==0
            if is_file_empty:
                writer.writerow(["Coordinator", "Event Name", "Budget", "Participants", "Volunteers Req."])

        with open(detailed_event_csv, 'a', newline= '') as file:
            writer = csv.writer(file)
            writer.writerow([self.part_name, event, budget, partis, num_vol])

        with open(detailed_event_csv, 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('Details of each event: ', 'green', attrs = ['bold']))
            print(x)







# -------------------------------------    Give Budget for Event    ---------------------------------------- #


    def change_password(self):
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv', 'r') as file:
            reader = csv.DictReader(file)
            coordinators_data = list(reader)
            for coordinator in coordinators_data:
                if coordinator['Name'] == self.part_name:
                    self.part_pass = coordinator['Password']
                    new_password = input(colored('Enter your new password: ', 'grey', attrs=['bold']))
    
                    coordinator['Password'] = new_password
                    with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/participants.csv', 'w', newline='') as file:
                        fieldnames = ['Name', 'Event', 'Password']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(coordinators_data)
    
                    print(colored('Password updated successfully!', 'green', attrs=['bold']))

 
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    data = list(reader)
                
                for coordinator in data:
                    if coordinator['Name'] == self.part_name: 
                        self.part_pass = coordinator['Password']
                        coordinator['Password'] = new_password
                        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv', 'w', newline='') as file:
                            fieldnames = ['Name', 'Password', 'Role']
                            writer = csv.DictWriter(file, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerows(data)
        
                        print(colored('Password updated successfully in mail file', 'green', attrs=['bold']))

            
    
# -------------------------------------    Read Participant Details    ---------------------------------------- #


    
    def read_participant_details(self):
        event =[]
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/coordinator.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.part_name:
                    event = row[1]
        participants_in_specific_event =[]
        with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if event in row[1]:
                    participants_in_specific_event.append(row[0])
        print('\n')
        print(colored(f'The participants in your Event {event} are: ', 'green', attrs = ['bold']))  
        print('\n')  
        for i,name in enumerate(participants_in_specific_event, start=1):
            print(colored(f"""{i}. {name}\n""", attrs = ['bold']))

        event_participant_name = input(colored('''
                Enter the name whose details you want to fetch: ''', 'grey', attrs=['bold']))
        if event_participant_name in participants_in_specific_event:

            with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/partbasicdetails.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Name'] == event_participant_name:
                        print(colored(f'Details for {event_participant_name}:', 'cyan', attrs=['bold']))
                        for key, value in row.items():
                            print(f"{key}: {value}")
                        break
                else:
                    print(colored(f'Participant with name {event_participant_name} not found.', 'red', attrs=['bold']))
        else:
            print(colored(f'{event_participant_name} havan\'t participated in your {event}.'))


    

# -------------------------------------    Remove participant    ---------------------------------------- #   
   
   
    def remove_participant(self):        
        print('\n')
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_details.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('''Events & corresponding Participants ''', 'green', attrs = ['bold']))
            print(x)


        rem_part_event = input(colored('''From which Event you want to remove:  ''', 'grey', attrs = ['bold']))
        parts=[]
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_details.csv', 'r') as file:
            reader =csv.reader(file)
            for row in reader:
                if row[1] == rem_part_event:
                    parts = row[3].split(', ')
        
        print(colored(f'''These are the participants in {rem_part_event} ''', 'green', attrs = ['bold']))
        for i,name in enumerate(parts):
            print(f'{i}. {name}\n')

        rem_part = input(colored(f'''Whom you would like to remove from {rem_part_event} ''', 'grey', attrs = ['bold']))


        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_details.csv', 'r') as file:
            reader = csv.DictReader(file, fieldnames=['Coordinator','Event Name','Budget','Participants','Volunteers Req.'])
            data = list(reader)
            for row in reader:
                if rem_part_event==row[1] and rem_part in row[3]:
                    data[3].remove(rem_part)

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_details.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Coordinator','Event Name','Budget','Participants','Volunteers Req.'])
            writer.writerows(data)

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_details.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('After removing participant', 'green', attrs = ['bold']))
            print(x)
