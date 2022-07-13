# -*- coding: utf-8 -*-
"""Append max values to summary.csv

This script searches data files in all subfolders from this directory and picks
out the highest-values spectroscopic data for each month and appends the
results to a summary file.

This is an example of an inefficient script. Find ways to refactor this script
into a more robust and maintanable version.

@author: David Curie
@version: 1.0
"""

import pandas as pd
from glob import glob

MONTHS = {1: "January",
          2: "Februrary",
          3: "March",
          4: "April",
          5: "May",
          6: "June",
          7: "July",
          8: "August",
          9: "September",
         10: "October",
         11: "November",
         12: "December",
         }

# Search through months by int, name pair in 2021.
for month, name in MONTHS.items():
    MM = f'{month:02}' # pad with leading zero
    filenames = glob(f'*/2021-{MM}-*') # get all files in this month
    data_as_list = []
    for file in filenames:
        month_entry = pd.read_csv(file, delimiter='\t', header=None)
        data_as_list.append(month_entry[1])
    try:
        month_df = pd.concat(data_as_list, axis=0, ignore_index=True)
    except ValueError:
        month_df = pd.DataFrame()
    with open('summary.csv', 'a') as outfile:
        outfile.write(f'2021 {name}, {month_df.values.max()}\n')

# Search through months by int, name pair in 2022.
for month, name in MONTHS.items():
    MM = f'{month:02}' # pad with leading zero
    filenames = glob(f'*/2022-{MM}-*') # get all files in this month
    data_as_list = []:
    for file in filenames:
        month_entry = pd.read_csv(file, delimiter='\t', header=None)
        data_as_list.append(month_entry[1])
    try:
        month_df = pd.concat(data_as_list, axis=0, ignore_index=True)
    except ValueError:
        month_df = pd.DataFrame()
    with open('summary.csv', 'a') as outfile:
        outfile.write(f'2022 {name}, {month_df.values.max()}\n')
