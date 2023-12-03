# IMPORTS
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
    
                    3. UPDATE
                               
                    4. DELETE
                     
                    5. EXIT
                               
                    Enter your preferred operation: ''', 'grey', attrs=['bold']))

            if user_input == '1':
                self.judge_give_scores()
            elif user_input == '2':
                self.judge_read()
            elif user_input == '3':
                self.judge_update()
            elif user_input == '4':
                self.judge_delete()
            elif user_input == '5':
                self.exit()
                break
            else:
                print(colored(''''
                    Invalid input''', 'red', attrs=['bold']))

    def judge_give_scores(self):
        while True:
            user_input = input(
                colored('''
                    What operation do you want to proceed with?''', 'cyan', attrs=['bold']) +

                colored('''
                              
                    1. IN EVENTS
    
                    2. IN WORKSHOPS
                                         
                    3. UPDATE SCORES

                    4. EXIT
                               
                    Enter your preferred operation: ''', 'grey', attrs=['bold']))
            print('\n')
            if user_input == '1':
                self.event_judge()
            elif user_input == '2':
                self.workshop_judge()
            elif user_input == '3':
                self.update_judging()
            elif user_input == '4':
                self.exit()
                break
            else:
                print(colored(''''
                    Invalid input''', 'red', attrs=['bold']))

    def event_judge(self):
        with open('event_participate.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(x)
            print("\n")
        self.part_name = input(colored('''
                    Whom do you want to give score: ''', 'cyan', attrs=['bold']))
        print(colored(f'''
                    {self.part_name} is to be judged in events:''', 'green', attrs=['bold']))
        events_participated = []

        with open('event_participate.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['Name'] == self.part_name:
                    events_participated = row['Event Participated'].split(', ')

            print(colored(f'''
                    {self.part_name} has participated in: {events_participated}''', 'yellow', attrs=['bold']))

            scores = self.load_existing_scores()

            for event in events_participated:
                existing_score = scores.get(event)
                if existing_score is not None:
                    overwrite = input(colored(f'Scores already exist for {event} ({existing_score}). Do you want to overwrite? (y/n): ', 'yellow', attrs=['bold']))
                    if overwrite.lower() != 'y':
                        continue

                score = float(input(f'''
                    Enter the score for {event} (0-10): '''))
                scores[event] = score

            # Update the CSV file with scores
            self.update_scores_in_csv(scores)

    def load_existing_scores(self):
        scores = {}
        with open('event_participate.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == self.part_name:
                    scores_str = row.get('Scores', '{}')
                    scores = ast.literal_eval(scores_str)
        return scores

    def update_scores_in_csv(self, scores):
        df = pd.read_csv('event_participate.csv')
        for index, row in df.iterrows():
            if row['Name'] == self.part_name:
                row['Scores'] = str(scores)

        df.to_csv('event_participate.csv', index=False)
        print(colored('''Scores have been updated''', 'green', attrs=['bold']))
        with open("event_participate.csv", 'r') as file:
            x = from_csv(file)
            x.hrules =ALL
            print(x)

    def exit(self):
        print(colored('''
                    Exiting the Judge class''', 'red', attrs = ['bold']))

