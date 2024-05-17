# Saving mechanics

import csv

global_variables = {'Equipe': None, 'collection': None, 'environnement':None, 'nb_inventory':None, 'nb_team':None, 'slide':None, 'pix':None, 'piy':None, 'j1.map.area_tab':None, 'case_depart':None} 

def fill_global_variables(global_variables):
    for key in global_variables:
        if key == 'area':
            pass
        if key == 'case_depart':
            pass
        else:
            global_variables[key] = globals()[key]



def save_game():
    pass
