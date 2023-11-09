import csv
from prettytable import PrettyTable 
from termcolor import colored
# So I have used prettyTable library here to show the table content of csv created beolow in a pretty manner!!

x= PrettyTable()
file_path = '/home/narayanj/Practice/THAR2.0/Admin/everyone.csv'
with open(file_path, 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerow(["SNo.", "Name", "Username", "Password", "Role"])
    writer.writerow([1, 'Narayan', 'Admin', 'admin123', 'Administration'])
    x.field_names = ["SNo.", "Name", "Username", "Password", "Role"]
    x.add_row([1, 'Narayan', 'Admin', 'admin123', 'Administration'])
    print(x) 

text =  colored('Table is created', 'green')
print(text)
# Now admin will create Organisers


class Create_roles:
    def __init__(self):
        pass
    def roles(self):
        self.list_organiser = []
        self.list_judge = []
        self.list_of_roles = ['Organiser', 'Judge']
        for i in self.list_of_roles:
            print(i)
        self.set_what = input('What role you want to create: ')
        if self.set_what.lower() == 'organiser':
            self.num_organisers = int(input("How many organiser you want to create: "))
            for i in range(1, self.num_organisers+1):
                self.org_name = input('Name of Organiser')
                self.org_username = input('Set Username: ')
                self.org_password = input('Set Password: ')
        elif self.set_what.lower() == 'judge':
            self.num_judge = int(input("How many Judges you want to create: "))
            for _ in range(1, self.num_judge+1):
                self.org_name = input('Name of Judge')
                self.which_event = input('Which event he is going to judge: ')
                self.judge_username = input('Set Username: ')
                self.judge_password = input('Set Password: ')
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([2, ])

class Create_Event:
    def __init__(self):
        pass

    def event(self):
        self.event_name = input('Event name: ')
        self.event_venue = input('Event place: ')
        self.event_time = input('Event Time: ')
    def update(self):
        self.choice = input("Do you want to update something? (Yes/No)")
        if self.choice.lower == 'yes':
            pass
class Exhibition:
    def __init__(self):
        pass
    
    def Create_exhibition(self):
        self.ex_name = input('Set exhibition name: ')
        self.ex_venue = input('Exhibition place: ')
        self.ex_time = input('What will be time: ')

class Workshop:
    def __init__(self):
        pass

    def Create_workshop(self):
        self.work_name = input('Set workshop name: ')
        self.work_venue = input('Workshop place: ')
        self.work_time = input('What will be time: ')

class Create_pro_nites:
    def __init__(self):
        pass

    def create_pro_nite(self):
        self.name_pro_nite = input('Set "Pro Nite" name: ')
        self.pro_venue = input('Where it will be helo: ')
        self.pro_time = input('What time will it start: ')


class Create_Coordinators_forevents:
    def __init__(self):
        pass
    def create_coordinator(self):
        self.cor_name = input('Name of Coordinator: ')
        self.cor_event = input('Coordinate which event: ')
        
# obj = Create_Event()
# obj.event()
# obj.update()