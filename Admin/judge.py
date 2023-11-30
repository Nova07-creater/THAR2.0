# IMPORTS
import os
import csv
import pandas as pd
from prettytable import PrettyTable, from_csv, ALL
from termcolor import colored
from datetime import datetime
import getpass
import emoji





# -------------------------------------    JUDGE CLASS    ------------------------------------- #

class Judge:
    def __init__(self):
        print(colored('Judge class called', 'green'))