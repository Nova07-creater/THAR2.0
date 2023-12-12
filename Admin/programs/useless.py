

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
 


#  runner_up = sorted_participants[len(top_participants)][0] if len(sorted_participants) > len(top_participants) else None
# print(f"1st Runner-up(s): {runner_up} " if runner_up else colored('Not enough participants for 1st Runner-up.', 'yellow', attrs=['bold']))

# runner_up = sorted_participants[len(top_participants)][0] if len(sorted_participants) > len(top_participants) else None
# print(f"1st Runner-up(s): {runner_up}" if runner_up else colored('Not enough participants for 1st Runner-up.', 'yellow', attrs=['bold']))
