# Saving mechanics

import csv
import os

path = os.getcwd()



def fill_global_variables(global_variables):
    for key in global_variables:
        if key == 'case_depart':
            global_variables['case_depart'] = globals()['j1.case']
        else:
            global_variables[key] = globals()[key]
    return global_variables
    
def save_game(save_name, global_variables):
    with open(save_name+'.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in global_variables.items():
            writer.writerow([key, value])

def read_save(save_name):
    with open(save_name+'.csv') as csv_file:
        reader = csv.reader(csv_file)
        global_variables = dict(reader)
        return global_variables
