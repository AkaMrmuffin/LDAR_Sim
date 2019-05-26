#------------------------------------------------------------------------------
# Name:         LDAR-Sim Batch simulator / program comparison
#
# Purpose:      Simulate multiple programs.
#               Outputs: (1) A folder for each program with all simulations,
#               (2) A folder with results (equivalence determination).
#
# Authors:      Thomas Fox, Mozhou Gao, Thomas Barchyn, Chris Hugenholtz
#
# Created:      2019-Mar-26
#
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

from weather_lookup import *
from ldar_sim import *
from time_counter import *
import numpy as np
import os

#------------------------------------------------------------------------------
#--------------------------------Set programs----------------------------------
master_output_folder = 'reg_vs_aircraft/'
n_simulations = 20
programs = [{
            'output_folder': master_output_folder + 'OGI_regulatory',
            'simulation': None,
            'timesteps': 5600,
            'start_year': 2001,
            'methods': {
                    'OGI': {
                             'n_crews': 1,
                             'min_temp': -10,
                             'max_wind': 10,
                             'max_precip': 2,
                             'min_interval': 120,
                             'max_workday': 10,  
                             'cost_per_day': 600
                             }
                        },        
            'repair_delay': 14,
            'WT_data': '15YearWT2001_2016.nc',
            'P_data': '15YearPrecip2001_2016.nc',
            'infrastructure_file': 'AER_Baytex_OGI_reg.csv',
            'leak_file': 'FWAQS_all.csv',
            'working_directory': "D:/OneDrive - University of Calgary/Documents/Thomas/PhD/Thesis/LDAR_Sim/model/python_v2",
            'LPR': 0.00133,
            'consider_daylight': True,
            'max_det_op': 0.00   # Operator max additional detection probability of largest leak
        },
        {
            'output_folder': master_output_folder + 'aircraft_1',
            'simulation': None,
            'timesteps': 1000,
            'start_year': 2001,
            'methods': {
                    'aircraft': {
                             'n_crews': 1,
                             'min_temp': -35,
                             'max_wind': 25,
                             'max_precip': 10,
                             'min_interval': 60,
                             'max_workday': 10,
                             'cost_per_day': 2000
                             },
                    'OGI_FU': {
                             'n_crews': 1,
                             'min_temp': -10,
                             'max_wind': 10,
                             'max_precip': 2,
                             'max_workday': 10,
                             'cost_per_day': 600
                             }                        
                        },        
            'repair_delay': 14,
            'WT_data': '15YearWT2001_2016.nc',
            'P_data': '15YearPrecip2001_2016.nc',
            'infrastructure_file': 'AER_Baytex_aircraft6_only.csv',
            'leak_file': 'FWAQS_all.csv',
            'working_directory': "D:/OneDrive - University of Calgary/Documents/Thomas/PhD/Thesis/LDAR_Sim/model/python_v2",
            'LPR': 0.00133,
            'consider_daylight': True,
            'max_det_op': 0.00   # Operator max additional detection probability of largest leak
        }]

output_directory = os.path.join(programs[0]['working_directory'], master_output_folder)
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    
for program in programs:
    parameters = program
    
    for i in range(n_simulations): 
        parameters['simulation'] = str(i)
    
#------------------------------------------------------------------------------
#-----------------------Initialize dynamic model state-------------------------
    
        state = {
            't': None,   
            'operator': None,       # operator gets assigned during initialization
            'methods': [],          # list of methods in action
            'sites': [],            # sites in the simulation
            'flags': [],            # list of sites flagged for follow-up
            'leaks': [],            # list of all current leaks
            'tags': [],             # leaks that have been tagged for repair
            'weather': None,        # this gets assigned during initialization
            'daylight': None,
            'init_leaks': [],       # the initial leaks generated at timestep 1
            'max_rate': None        # the largest leak in the input file
        }
        
#------------------------Initialize timeseries data----------------------------
        
        timeseries = {
            'datetime': [],
            'active_leaks': [],
            'new_leaks': [],
            'n_tags': [],
            'cum_repaired_leaks': [],
            'daily_emissions_kg': []
        }
        
#-----------------------------Run simulations----------------------------------
        
        if __name__ == '__main__':
        
            # Initialize objects
            print('Initializing, please wait...')
            
            state['weather'] = weather_lookup (state, parameters)
            state['t'] = time_counter (parameters)
            sim = ldar_sim (state, parameters, timeseries)
            
            print ('Initialization complete!')
        
           
        # Loop through timeseries
        while state['t'].current_date <= state['t'].end_date:
            sim.update ()
            state['t'].next_day ()
        
        # Clean up and write files
        sim.finalize ()
    
    
    
#---------------------------------Method library-------------------------------
#
#                    'M21': {
#                             'n_crews': 1,
#                             'min_temp': -35,
#                             'max_wind': 25,
#                             'max_precip': 10,
#                             'min_interval': 60,
#                             'max_workday': 10,
#                             'cost_per_day': 400
#                             },
#                    'OGI': {
#                             'n_crews': 1,
#                             'min_temp': -35,
#                             'max_wind': 25,
#                             'max_precip': 10,
#                             'min_interval': 60,
#                             'max_workday': 10,  
#                             'cost_per_day': 600
#                             },
#                    'OGI_FU': {
#                             'n_crews': 1,
#                             'min_temp': -35,
#                             'max_wind': 25,
#                             'max_precip': 10,
#                             'max_workday': 10,
#                             'cost_per_day': 600
#                             },
#                    'truck': {
#                             'n_crews': 1,
#                             'min_temp': -35,
#                             'max_wind': 25,
#                             'max_precip': 10,
#                             'min_interval': 30,
#                             'max_workday': 10,
#                             'cost_per_day': 500
#                             },
#                    'aircraft': {
#                             'n_crews': 1,
#                             'min_temp': -35,
#                             'max_wind': 25,
#                             'max_precip': 10,
#                             'min_interval': 60,
#                             'max_workday': 10,
#                             'cost_per_day': 2000
#                             }