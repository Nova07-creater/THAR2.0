import csv
import os
from prettytable import PrettyTable, from_csv, ALL
from termcolor import colored
# ------------------------------------- JUDGE CLASS ------------------------------------- #
 
class Judge:
    def __init__(self, part_name):
        self.part_name = part_name
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
 

    def judge_read(self):
        while True:
            user_input = input(
                colored('''
                    What operation do you want to proceed with?''', 'cyan', attrs=['bold']) +
 
                colored('''
                             
                    1. EVENT RESULT
   
                    2. WORKSHOP RESULT
                                 
                    3. BACK
                     
                    4. Log Out
                               
                    Enter your preferred operation: ''', 'grey', attrs=['bold']))
 
            if user_input == '1':
                self.event_results()
            elif user_input == '2':
                self.workshop_result()
            elif user_input == '3':
                return False
            elif user_input == '4':
                print(colored('''
                    Logged out successfully ''', 'green', attrs = ['bold']))
                break
            else:
                print(colored(''''
                    Invalid input''', 'red', attrs=['bold']))
     
    def event_results(self):
        print('\n')
        print(colored('''Event Results ''', 'cyan', attrs = ['bold']))            
   
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_results.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(x)
 
    def workshop_result(self):
        print('\n')
        print(colored('''Workshop Results ''', 'cyan', attrs = ['bold']))            
   
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_results.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(x)



# -------------------------------------    CHANGE PASSWORD    ------------------------------------- #
 
 
    def change_pass(self):
        judge_csv_path = "/home/narayanj/Practice/THAR2.0/Admin/csvs/judge.csv"
        everyone_csv_path = "/home/narayanj/Practice/THAR2.0/Admin/csvs/everyone.csv"
       
        with open(judge_csv_path, 'r') as file:
            reader = csv.DictReader(file)
            judges_data = list(reader)
 
        for judge in judges_data:
            if judge['Name'] == self.part_name:
                self.part_pass = judge['Password']
                new_password = input(colored('Enter your new password: ', 'grey', attrs=['bold']))
                judge['Password'] = new_password
 
                with open(judge_csv_path, 'w', newline='') as file:
                    fieldnames = ['Name', 'Password', 'Role']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(judges_data)
 
                print(colored('Password updated successfully!', 'green', attrs=['bold']))
 
                with open(everyone_csv_path, 'r') as file:
                    reader = csv.DictReader(file)
                    data = list(reader)
 
                for everyone in data:
                    if everyone['Name'] == self.part_name:
                        self.part_pass = everyone['Password']
                        everyone['Password'] = new_password
 
                with open(everyone_csv_path, 'w', newline='') as file:
                    fieldnames = ['Name', 'Password', 'Role']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(data)
 
                print(colored('Password updated successfully in everyone file', 'green', attrs=['bold']))
                return
 
        print(colored('Judge not found!', 'red', attrs=['bold']))
 
 
 
 
 
 
# ------------------------------------- GIVE SCORES ------------------------------------- #
 
    def judge_give_scores(self):
        while True:
            user_input = input(
                colored('''
                    What operation do you want to proceed with?''', 'cyan', attrs=['bold']) +
 
                colored('''
                             
                    1. IN EVENTS
   
                    2. IN WORKSHOPS
                                         
                    3. EXIT
                               
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
 
 
    def event_judge(self):
        event_results_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/event_results.csv'
        if not os.path.exists(event_results_path):
            with open(event_results_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Event Name', 'Winner', 'Runner Up'])
        
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('The events available to be judged: ', 'green', attrs=['bold']))
            print(x)

        events = []
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/events.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                events.append(row[0])
        print('\n')
        while True:
            event_judge = input(colored('Which event you want to judge:  ', 'grey', attrs=['bold']))
            if event_judge in events:
                events_already_judged = []
                
                with open(event_results_path, 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        events_already_judged.append(row[0])

                if event_judge not in events_already_judged:
                    all_parts = []
                    with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv', 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if event_judge in row[1]:
                                all_parts.append(row[0])

                    print(colored(f'The participants in {event_judge} are: \n'))
                    for i, name in enumerate(all_parts, start=1):
                        print(f'{i}. {name}\n')

                    participants_scores = {}
                    for participant in all_parts:
                        while True:
                            score = input(f"Enter score for {participant} (1-10): ")
                            if score.isdigit() and 1 <= int(score) <= 10:
                                participants_scores[participant] = int(score)
                                break
                            else:
                                print(colored('Invalid input. Please enter a numeric score between 1 and 10.', 'red', attrs=['bold']))
                    sorted_participants = sorted(participants_scores.items(), key=lambda x: x[1], reverse=True)
                    if sorted_participants:
                        print(colored('Results:', 'cyan', attrs=['bold']))
                        
                        top_score = sorted_participants[0][1]
                        top_participants = [part for part, score in sorted_participants if score == top_score]
                        
                        winners = ', '.join(top_participants)
                        print(f"Winner(s): {winners} with a score of {top_score}")

                                                
                        if len(sorted_participants)> len(top_participants):
                            runner_up = sorted_participants[len(top_participants)][0]
                            print(f"1st Runner-up(s): {runner_up} ")
                        else:
                            print(colored('Not Enough participants', 'red', attrs =['bold']))

                        with open(event_results_path, 'a', newline='') as results_file:
                            writer = csv.writer(results_file)
                            if os.stat(event_results_path).st_size == 0:
                                writer.writerow(['Event Name', 'Winner', 'Runner Up'])
                            writer.writerow([event_judge, winners, runner_up])

                        with open(event_results_path, 'r') as file:
                            x = from_csv(file)
                            x.hrules = ALL
                            print(colored('Result Declared', 'green', attrs=['bold']))
                            print(x)
                        break        
                    else:
                        print(colored('No participants found for the specified event.', 'red', attrs=['bold']))
                else:
                    all_parts = []
                    with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/event_participate.csv', 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if event_judge in row[1]:
                                all_parts.append(row[0])

                    print(colored(f'The participants in {event_judge} are: '))
                    for i, name in enumerate(all_parts, start=1):
                        print(f'{i}. {name}')

                    participants_scores = {}
                    for participant in all_parts:
                        while True:
                            score = input(f"Enter score for {participant} (1-10): ")
                            if score.isdigit() and 1 <= int(score) <= 10:
                                participants_scores[participant] = int(score)
                                break
                            else:
                                print(colored('Invalid input. Please enter a numeric score between 1 and 10.', 'red', attrs=['bold']))                    
                    sorted_participants = sorted(participants_scores.items(), key=lambda x: x[1], reverse=True)
                    if sorted_participants:
                        print(colored('Results:', 'cyan', attrs=['bold']))
                        
                        top_score = sorted_participants[0][1]
                        top_participants = [part for part, score in sorted_participants if score == top_score]
                        
                        winners = ', '.join(top_participants)
                        print(f"Winner(s): {winners} with a score of {top_score}")

                        if len(sorted_participants)> len(top_participants):
                            runner_up = sorted_participants[len(top_participants)][0]
                            print(f"1st Runner-up(s): {runner_up} ")
                        else:
                            print(colored('Not Enough participants', 'red', attrs =['bold']))

                        with open(event_results_path, 'r') as file:
                            reader = csv.reader(file)
                            rows = [row for row in reader]
                            for row in rows:
                                if row[0] == event_judge:
                                    row[1] = winners
                                    row[2] = runner_up  
                        with open(event_results_path, 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(rows)
                        break
            else:
                print(colored(f'{event_judge} does not exist, Try another..', 'red', attrs=['bold']))
                continue
                  
        
# ------------------------------------- JUDGE WORKSHOPS ------------------------------------- #
 
 
    def workshop_judge(self):
        workshop_results_path = '/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_results.csv'

        if not os.path.exists(workshop_results_path):
            with open(workshop_results_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Workshop Name', 'Winner', 'Runner Up'])

        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv', 'r') as file:
            x = from_csv(file)
            x.hrules = ALL
            print(colored('The workshops available to be judged: ', 'green', attrs=['bold']))
            print(x)

        workshops = []
        with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/wrokshops.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                workshops.append(row[0])

        while True:
            workshop_judge = input(colored('Which workshop do you want to judge:  ', 'grey', attrs=['bold']))
            if workshop_judge not in workshops:
                print(colored(f'{workshop_judge} does not exist. Please enter another...', 'red', attrs=['bold']))
            else:
                workshop_already_judged = []
                with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_results.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        workshop_already_judged.append(row[0])

                if workshop_judge not in workshop_already_judged:
                    all_parts = []
                    with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv', 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if workshop_judge in row[1]:
                                all_parts.append(row[0])
                    print(colored(f'The participants in {workshop_judge} are: '))
                    for i, name in enumerate(all_parts, start=1):
                        print(f'{i}. {name}')
                    participants_scores = {}
                    for participant in all_parts:
                        while True:
                            score = input(f"Enter score for {participant} (1-10): ")
                            if score.isdigit() and 1 <= int(score) <= 10:
                                participants_scores[participant] = int(score)
                                break
                            else:
                                print(colored('Invalid input. Please enter a numeric score between 1 and 10.', 'red', attrs=['bold']))
                    sorted_participants = sorted(participants_scores.items(), key=lambda x: x[1], reverse=True)
                    if sorted_participants:
                        print(colored(f'Participants for {workshop_judge}:', 'cyan', attrs=['bold']))
                        for i, participant in enumerate(all_parts, start=1):
                            print(f"{i}. {participant}: Score = {participants_scores[participant]}")

                        top_score = sorted_participants[0][1]
                        top_participants = [part for part, score in sorted_participants if score == top_score]

                        winners = ', '.join(top_participants)
                        print(f"Winner(s): {winners} with a score of {top_score}")

                        if len(sorted_participants)> len(top_participants):
                            runner_up = sorted_participants[len(top_participants)][0]
                            print(f"1st Runner-up(s): {runner_up} ")
                        else:
                            print(colored('Not Enough participants', 'red', attrs =['bold']))

                        with open(workshop_results_path, 'a', newline='') as results_file:
                            writer = csv.writer(results_file)
                            if os.stat(workshop_results_path).st_size == 0:
                                writer.writerow(['Workshop Name', 'Winner', 'Runner Up'])
                            writer.writerow([workshop_judge, winners, runner_up])

                    else:
                        print(colored('No participants found for the specified workshop.', 'red', attrs=['bold']))
                elif workshop_judge in workshop_already_judged:
                    all_parts = []
                    with open('/home/narayanj/Practice/THAR2.0/Admin/csvs/workshop_participate.csv', 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if workshop_judge in row[1]:
                                all_parts.append(row[0])
                    print(colored(f'The participants in {workshop_judge} are: '))
                    for i, name in enumerate(all_parts, start=1):
                        print(f'{i}. {name}')
                    for participant in all_parts:
                        while True:
                            score = input(f"Enter score for {participant} (1-10): ")
                            if score.isdigit() and 1 <= int(score) <= 10:
                                participants_scores[participant] = int(score)
                                break
                            else:
                                print(colored('Invalid input. Please enter a numeric score between 1 and 10.', 'red', attrs=['bold']))
                    print(colored(f'Participants for {workshop_judge}:', 'cyan', attrs=['bold']))
                    for i, participant in enumerate(all_parts, start=1):
                        print(f"{i}. {participant}: Score = {participants_scores[participant]}")

                    sorted_participants = sorted(participants_scores.items(), key=lambda x: x[1], reverse=True)

                    if sorted_participants:
                        top_score = sorted_participants[0][1]
                        top_participants = [part for part, score in sorted_participants if score == top_score]

                        winners = ', '.join(top_participants)
                        print(f"Winner(s): {winners} with a score of {top_score}")

                        if len(sorted_participants)> len(top_participants):
                            runner_up = sorted_participants[len(top_participants)][0]
                            print(f"1st Runner-up(s): {runner_up} ")
                        else:
                            print(colored('Not Enough participants', 'red', attrs =['bold']))
                        with open(workshop_results_path, 'r') as file:
                            reader = csv.reader(file)
                            for row in reader:
                                if row[0] == workshop_judge:
                                    row = [workshop_judge, winners, runner_up]
                        with open(workshop_results_path, 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(reader)

                break