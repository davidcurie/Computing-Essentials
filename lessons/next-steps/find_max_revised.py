# -*- coding: utf-8 -*-
"""Append max values to summary.csv

This script searches data files in all subfolders from this directory and picks
out the highest-values spectroscopic data for each month and appends the
results to a summary file.

This is an example of an improved script as outlined in the 'Next Steps with
Python' lesson.

@author: David Curie
@version: 1.1

Notable changes from version 1.0:
    - Reorganized logic to gather files -> manage data -> write results
    - Moved logic into dedicated functions
        - Non user-facing functions hidden with _function()
    - Defined script action when called explicitly (if __name__ == '__main__')
    - Added docstrings
    - Moved this file to scripts/ folder, adjusted filepaths as necessary
"""

import pandas as pd
from glob import glob
from itertools import groupby
import os

# LOGIC FOR GATHERING FILES

def get_all_filenames(pattern):
    all_filenames_as_list = glob(pattern)
    return all_filenames_as_list

def _get_date_from(filename):
    """Return (YYYY, MM, DD) from filename string"""
    # Assumes filename: YYYY-MM-DD_other_text
    YYYYMMDD = os.path.basename(filename).split('_')[0]
    YYYY, MM, DD = YYYYMMDD.split('-')
    return YYYY, MM, DD

def _project_YYYY(filename):
    """Return YYYY from filename string"""
    return int(_get_date_from(filename)[0])

def _project_YYYYMM(filename):
    """Return YYYY-MM string from filename string"""
    return '-'.join(_get_date_from(filename)[0:2])

def _project_YYYYMMDD(filename):
    """ Return YYYY-MM-DD string from filename string"""
    return '-'.join(_get_date_from(filename))

# https://stackoverflow.com/questions/37568763/python-group-a-list-into-sublists-by-a-equality-of-projected-value
def sort_filenames(list_of_filenames, key=_project_YYYYMM):
    """Group list of filenames by key.
    Default grouping key is by month. Each subgroup is ordered by date.
    
    Assumptions
    -----------
    Filename begins with YYYY-MM-DD_
    """
    # Define a new projection above to specify a new grouping
    sorted_list = sorted(list_of_filenames, key=key)
    grouped_list = [sorted(list(it), key=_project_YYYYMMDD) for k, it in groupby(sorted_list, key)]
    return grouped_list

# LOGIC FOR MANAGING DATA

def _import_data(file):
    return pd.read_csv(file, delimiter='\t', header=None)

def import_files_into_dataframe(parsed_list):
    list_of_dataframes = []
    for sublist in parsed_list:
        sublist_df = pd.concat(map(_import_data, sublist))
        list_of_dataframes.append(sublist_df)
    return list_of_dataframes

def get_max_values(list_of_dataframes):
    list_of_max_values = []
    for dataframe in list_of_dataframes:
       group_max = dataframe.max()
       list_of_max_values.append(group_max)
    max_values_df = pd.DataFrame(list_of_max_values)
    return max_values_df


# INTENDED SEQUENCE OF OPERATIONS

if __name__ == "__main__":
    files_to_search = '../data/*/*'
    files_as_list = get_all_filenames(files_to_search)
    grouped_files = sort_filenames(files_as_list)
    df_list = import_files_into_dataframe(grouped_files)
    df_max_vals = get_max_values(df_list)
    with open('../results/summary.csv', 'w') as outfile:
        df_max_vals.to_csv(outfile, header=None)

