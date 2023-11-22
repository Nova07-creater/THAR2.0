# import csv
# from admin import *
# from prettytable import PrettyTable, from_csv, ALL
# from termcolor import colored
 
 
# class UserAuthenticator:
#     def __init__(self):
#         self.authenticate_user()
 
#     def authenticate_user(self):
#         name = input("Please enter your Name: ")
#         password = input("Please enter your password: ")
 
#         with open('/home/narayanj/Practice/THAR2.0/Admin/everyone.csv', 'r') as file:
#             reader = csv.DictReader(file)
 
#             for row in reader:
#                 if row['Name'] == name and row['Password'] == password:
#                     role = row['Role']
#                     if role.lower() == 'admin':
#                         Admin()
#                     elif role.lower() == 'co-ordinator':
#                         Coordinator()
#                     elif role.lower() == 'organiser':
#                         Organiser()
#                     elif role.lower() == 'judge':
#                         Judge()
#                     else:
#                         print("Invalid role detected.")
#                     break
#             else:
#                 print("Incorrect name or password. Exiting...")
 
 
# class Admin:
#     pass
    
 
# class Coordinator:
#     def
 
# class Organiser:
#     pass
    
 
# class Judge:
#     pass
 
 
# if __name__ == "__main__":
#     UserAuthenticator()


from termcolor import colored
import csv

ch_event = input(colored('Which event name you want to change: ', 'yellow'))
if ch_event in event_name_list:
    chd_event = input(colored('Enter the event name replacement value: ', 'yellow'))
    
    

    #

    # Write the updated data back to the CSV file
    fieldnames = reader.fieldnames
    with open('/home/narayanj/Practice/THAR2.0/Admin/events.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Event name '{ch_event}' replaced with '{chd_event}'.")
else:
    print(f"Event name '{ch_event}' not found.")

import csv
from termcolor import colored  # Make sure to import the 'colored' function from the termcolor module

def remove_event(self):
    file_path = '/home/narayanj/Practice/THAR2.0/Admin/events.csv'

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        events = list(reader)

    event_name_list = [event['Event Name'] for event in events]

    for i, item in enumerate(event_name_list):
        print(f'{i+1}. {item}\n')

    ch_event = input(colored('Which event name you want to remove: ', 'yellow'))

    if ch_event in event_name_list:
        print('Removing...')

        index_to_remove = event_name_list.index(ch_event)

        removed_event = events.pop(index_to_remove)

        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(events)

        print(f'The event "{removed_event["Event Name"]}" has been removed.')
    else:
        print(f'The event "{ch_event}" does not exist in the list.')




def remove_event(self):
    file_path = '/home/narayanj/Practice/THAR2.0/Admin/events.csv'

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        event_name_list = [col['Event Name'] for col in reader]

    for i, item in enumerate(event_name_list):
        print(f'{i+1}.{item}\n')        

    ch_event = input(colored('Which event you want to remove: \n', 'yellow'))

    if ch_event in event_name_list:
        index_to_remove = event_name_list.index(ch_event)
        event_name_list.pop(index_to_remove)

        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer.writeheader()

            # Write rows excluding the one to be removed
            for row in reader:
                if row['Event Name'] != ch_event:
                    writer.writerow(row)

        print(colored('Event has been removed', 'green'))

        with open(file_path, "r") as fp:
            x = csv.reader(fp)
            for row in x:
                print(row)

    else:
        print(colored('The entered event not found', 'red'))

# Call the function
# remove_event()
# 