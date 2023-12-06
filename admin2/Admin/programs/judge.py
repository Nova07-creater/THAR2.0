import os
import csv
import pandas as pd
from prettytable import PrettyTable, from_csv, ALL
from termcolor import colored
from datetime import datetime
import ast
# ------------------------------------- JUDGE CLASS ------------------------------------- #
 
class Judge:
    def __init__(self):
        self.part_name = None
        self.crud()
 
    def crud(self):
        while True:
            user_input = input(
                colored('''
                    What operation do you want to proceed with?''', 'cyan', attrs=['bold']) +
 
                colored('''
                             
                    1. GIVE SCORES
   
                    2. READ
                                  
                    3. CHANGE PASSWORD
                     
                    4. Log Out
                               
                    Enter your preferred operation: ''', 'grey', attrs=['bold']))
 
            if user_input == '1':
                self.judge_give_scores()
            elif user_input == '2':
                self.judge_read()
            elif user_input == '3':
                self.change_pass()
            elif user_input == '4':
                print(colored('''
                    Logged out successfully ''', 'green', attrs = ['bold']))
                break
            else:
                print(colored(''''
                    Invalid input''', 'red', attrs=['bold']))
 
# -------------------------------------    CHANGE PASSWORD    ------------------------------------- #

    def change_pass(self):
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/judge.csv', 'r') as file:
            reader = csv.DictReader(file)
            judges_data = list(reader)
 
        participant_found = False
        for judge in judges_data:
            if judge['Name'] == self.part_name:
                participant_found = True
                self.part_pass = judge['Password']
                new_password = input(colored('Enter your new password: ', 'grey', attrs=['bold']))
               
                judge['Password'] = new_password
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/judge.csv', 'w', newline='') as file:
                    fieldnames = ['Name', 'Password']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(judges_data)
 
                print(colored('Password updated successfully!', 'green', attrs=['bold']))
                break
 
        if not participant_found:
            print(colored('Participant not found. Password not updated.', 'red', attrs=['bold']))





# ------------------------------------- GIVE SCORES ------------------------------------- #

    def judge_give_scores(self):
        while True:
            user_input = input(
                colored('''
                    What operation do you want to proceed with?''', 'cyan', attrs=['bold']) +
 
                colored('''
                             
                    1. IN EVENTS
   
                    2. IN WORKSHOPS
                                          
                    4. EXIT
                               
                    Enter your preferred operation: ''', 'grey', attrs=['bold']))
            print('\n')
            if user_input == '1':
                self.event_judge()
            elif user_input == '2':
                self.workshop_judge()
            elif user_input == '3':
                self.exit()
                break
            else:
                print(colored(''''
                    Invalid input''', 'red', attrs=['bold']))
                
    
    
    def exit(self):
        print(colored('''
                    Exiting the Judge class''', 'red', attrs = ['bold']))
        

# ------------------------------------- JUDGE EVENTS ------------------------------------- #


#     def event_judge(self):
#         with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv', 'r') as file:
#             x = from_csv(file)
#             x.hrules = ALL
#             print(x)
#             print("\n")
#         self.part_name = input(colored('''
#                     Whom do you want to give score: ''', 'cyan', attrs=['bold']))
#         print(colored(f'''
#                     {self.part_name} is to be judged in events:''', 'green', attrs=['bold']))
#         events_participated = []
 
#         with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv', 'r') as file:
#             reader = csv.DictReader(file)
 
#             for row in reader:
#                 if row['Name'] == self.part_name:
#                     events_participated = row['Event Participated'].split(', ')
 
#             print(colored(f'''
#                     {self.part_name} has participated in: {events_participated}''', 'yellow', attrs=['bold']))
 
#             scores = self.load_existing_scores()
 
#             for event in events_participated:
#                 existing_score = scores.get(event)
#                 if existing_score is not None:
#                     overwrite = input(colored(f'Scores already exist for {event} ({existing_score}). Do you want to overwrite? (y/n): ', 'yellow', attrs=['bold']))
#                     if overwrite.lower() != 'y':
#                         continue
#                 while True:
#                     score = float(input(f'''
#                         Enter the score for {event} (0-10): '''))
#                     if score >=0 and score <= 10:
#                         scores[event] = score
#                         break
#                     else:
#                         print(colored('''Please follow scoring criteria ''', 'red', attrs =['bold']))
#                         continue
#             self.update_scores_in_csv(scores)
 
#     def load_existing_scores(self):
#         scores = {}
#         with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv', 'r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 if row['Name'] == self.part_name:
#                     scores_str = row.get('Scores', '{}')
#                     scores = ast.literal_eval(scores_str)
#         return scores
 
#     def update_scores_in_csv(self, scores):
#         df = pd.read_csv('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv')
#         for index, row in df.iterrows():
#             if row['Name'] == self.part_name:
#                 row['Scores'] = str(scores)
 
#         df.to_csv('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv', index=False)
#         print(colored('''Scores have been updated''', 'green', attrs=['bold']))
#         with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv", 'r') as file:
#             x = from_csv(file)
#             x.hrules =ALL
#             print(x)
 


# # ------------------------------------- JUDGE WORKDHOPS ------------------------------------- #


#     def workshop_judge(self):
#         with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv', 'r') as file:
#             x = from_csv(file)
#             x.hrules = ALL
#             print(x)
#             print("\n")
#         self.part_name = input(colored('''
#                     Whom do you want to give score: ''', 'cyan', attrs=['bold']))
#         print(colored(f'''
#                     {self.part_name} is to be judged in workshops:''', 'green', attrs=['bold']))
#         workshops_participated = []
 
#         with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv', 'r') as file:
#             reader = csv.DictReader(file)
 
#             for row in reader:
#                 if row['Name'] == self.part_name:
#                     workshops_participated = row['Workshop Participated'].split(', ')
 
#             print(colored(f'''
#                     {self.part_name} has participated in: {workshops_participated}''', 'yellow', attrs=['bold']))
 
#             scores = self.load_existing_scores()
 
#             for workshop in workshops_participated:
#                 existing_score = scores.get(workshop)
#                 if existing_score is not None:
#                     overwrite = input(colored(f'Scores already exist for {workshop} ({existing_score}). Do you want to overwrite? (y/n): ', 'yellow', attrs=['bold']))
#                     if overwrite.lower() != 'y':
#                         continue
 
#                 score = float(input(f'''
#                     Enter the score for {workshop} (0-10): '''))
#                 scores[workshop] = score
 
#             self.update_scores_in_csv(scores)
 
#     def load_existing_scores(self):
#         scores = {}
#         with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv', 'r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 if row['Name'] == self.part_name:
#                     scores_str = row.get('Scores', '{}')
#                     scores = ast.literal_eval(scores_str)
#         return scores
 
#     def update_scores_in_csv(self, scores):
#         df = pd.read_csv('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv')
#         for index, row in df.iterrows():
#             if row['Name'] == self.part_name:
#                 row['Scores'] = str(scores)
 
#         df.to_csv('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv', index=False)
#         print(colored('''Scores have been updated''', 'green', attrs=['bold']))
#         with open("/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv", 'r') as file:
#             x = from_csv(file)
#             x.hrules =ALL
#             print(x)



# ------------------------------------- JUDGE EVENTS ------------------------------------- #


    def event_judge(self):
        print('\n')
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('The events available to be judged: ', 'green', attrs=['bold']))
            print(x)
 
        event_judge = input(colored('''
                Which event you want to judge:  ''', 'grey', attrs=['bold']))
 
        all_parts = []
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_details.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == event_judge:
                    all_parts = [part.strip() for part in row[3].split(',')]

        
        participants_scores = {}


        for participant in all_parts:
            while True:
                try:
                    score = float(input(f"Enter score for {participant} (0-10): "))
                    if 0 <= score <= 10:
                        participants_scores[participant] = score
                        break
                    print(colored('Invalid input. Please enter a score between 0 and 10.', 'red', attrs=['bold']))
                except ValueError:
                    print(colored('Invalid input. Please enter a valid number.', 'red', attrs=['bold']))
 
        print(colored(f'Participants for {event_judge}:', 'cyan', attrs=['bold']))
        for i, participant in enumerate(all_parts, start=1):
            print(f"{i}. {participant}: Score = {participants_scores[participant]}")

        sorted_participants = sorted(participants_scores.items(), key=lambda x: x[1], reverse=True)

        if sorted_participants:
            print(colored('Results:', 'cyan', attrs=['bold']))
            print(f"Winner: {sorted_participants[0][0]} with a score of {sorted_participants[0][1]}")
            if len(sorted_participants) > 1:
                print(f"1st Runner-up: {sorted_participants[1][0]} with a score of {sorted_participants[1][1]}")
            elif sorted_participants:
                print(colored('Not enough participants for 1st Runner-up.', 'yellow', attrs=['bold']))
        else:
            print(colored('No participants found for the specified event.', 'red', attrs=['bold']))
            

# ------------------------------------- JUDGE WORKSHOPS ------------------------------------- #


    def workshop_judge(self):
        print('\n')
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('The workshops available to be judged: ', 'green', attrs=['bold']))
            print(x)
 
        event_judge = input(colored('''
                Which workshop you want to judge:  ''', 'grey', attrs=['bold']))
 
        all_parts = []
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_details.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == event_judge:
                    all_parts = [part.strip() for part in row[3].split(',')]

        
        participants_scores = {}


        for participant in all_parts:
            while True:
                try:
                    score = float(input(f"Enter score for {participant} (0-10): "))
                    if 0 <= score <= 10:
                        participants_scores[participant] = score
                        break
                    print(colored('Invalid input. Please enter a score between 0 and 10.', 'red', attrs=['bold']))
                except ValueError:
                    print(colored('Invalid input. Please enter a valid number.', 'red', attrs=['bold']))
 
        print(colored(f'Participants for {event_judge}:', 'cyan', attrs=['bold']))
        for i, participant in enumerate(all_parts, start=1):
            print(f"{i}. {participant}: Score = {participants_scores[participant]}")

        sorted_participants = sorted(participants_scores.items(), key=lambda x: x[1], reverse=True)

        if sorted_participants:
            print(colored('Results:', 'cyan', attrs=['bold']))
            print(f"Winner: {sorted_participants[0][0]} with a score of {sorted_participants[0][1]}")
            if len(sorted_participants) > 1:
                print(f"1st Runner-up: {sorted_participants[1][0]} with a score of {sorted_participants[1][1]}")
            elif sorted_participants:
                print(colored('Not enough participants for 1st Runner-up.', 'yellow', attrs=['bold']))
        else:
            print(colored('No participants found for the specified event.', 'red', attrs=['bold']))
            