#------------------------------------------------------------------------------
# Name:        Generic functions
# Purpose:     Generic functions for running LDAR Simulator
#
# Authors:     Thomas Fox, Mozhou Gao, Thomas Barchyn, Chris Hugenholtz
#
# Created:     18-11-2018

#------------------------------------------------------------------------------
import numpy as np

def gap_calculator (condition_vector):
    """
    This function calculates max gaps between daily activites in a time series.
    Requires only a single binary vector describing whether a condition was met.
    """
    
    # Find the index of all days in which the condition is true
    max_gap = None
    indices = np.where(condition_vector == True)
    
    # If there are no condition days, max_gap equals the vector length
    if len(indices[0]) == 0:
        max_gap = len(condition_vector)

    # If there is only one condition day, get max_gap
    elif len(indices[0]) == 1:
        start_gap = indices[0][0]   
        end_gap = len(condition_vector) - indices[0][0]
        max_gap = max(start_gap, end_gap)
        
    # If there are multiple condition days, calculate longest gap   
    elif len(indices[0] > 1):  
        start_gap = indices[0][0]   
        mid_gap = max(abs(x - y) for (x, y) in zip(indices[0][1:], indices[0][:-1]))
        end_gap = len(condition_vector) - indices[0][-1]
        max_gap = max(start_gap, mid_gap, end_gap)
        
    return (max_gap)

