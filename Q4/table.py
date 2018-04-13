#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:17:55 2017

@author: feng
"""

import pandas as pd
import numpy as np
import glob

# Use file_names to keep all excel file names, and two lists to classify ira/mtc
file_names = glob.glob('*.xlsx')
files_ira = []
files_mtc = []

for s in file_names:
    if s[:14] == 'Report tom_ira':
        files_ira.append(s)
    else:
        files_mtc.append(s)

# Use two lists to keep the names of the first day of each month
names_ira = []
names_mtc = []

# Implement a for loop, to extract the first day
for i in range(4, 11):
    for s in files_ira:
        if i == int(s[20:22]):
            names_ira.append(s)
            break
for i in range(4, 11):
    for t in files_mtc:
        if i == int(t[20:22]):
            names_mtc.append(t)
            break

# Data Frame to store the data of the first day of each month
df_list_ira = []
df_list_mtc = []

# Read excel files, and extract 'count' column
for s in names_ira:
    temp_df = pd.read_excel(s, 'Account Stats by Status')
    temp_df = temp_df[['loanStatus', 'count']]
    df_list_ira.append(temp_df)
for t in names_mtc:
    temp_df = pd.read_excel(t, 'Account Stats by Status')
    temp_df = temp_df[['loanStatus', 'count']]
    df_list_mtc.append(temp_df)

# Create loan status and merge all Data Frame
d = {'loanStatus': ['In Funding', 'Issued', 'Current', 'In Grace Period', 'Late (16-30 days)', 'Late (31-120 days)', 'Default', 'Charged Off']}
temp = pd.DataFrame(data=d)
result1 = pd.merge(temp, df_list_ira[0], how='left', on=['loanStatus'])
result2 = pd.merge(temp, df_list_mtc[0], how='left', on=['loanStatus'])

for i in range(1, 7):
    result1 = pd.merge(result1, df_list_ira[i], how='left', on=['loanStatus'])
    result2 = pd.merge(result2, df_list_mtc[i], how='left', on=['loanStatus'])

header1 = ['Loan Status']
header2 = ['Loan Status']

# Extract dates from name lists, and set dates as column names
for s in names_ira:
    header1.append(s[15:-5])
for t in names_mtc:
    header2.append(t[15:-5])

# Set loan status as index
result1.columns = header1
result2.columns = header2
result1['Loan Status'].replace(['In Funding', 'In Grace Period', 'Late (16-30 days)', 'Late (31-120 days)'], ['Funding', 'Grace Period', 'Late Stage 1', 'Late Stage 2'], inplace=True)
result2['Loan Status'].replace(['In Funding', 'In Grace Period', 'Late (16-30 days)', 'Late (31-120 days)'], ['Funding', 'Grace Period', 'Late Stage 1', 'Late Stage 2'], inplace=True)
result1.set_index('Loan Status', inplace=True)
result2.set_index('Loan Status', inplace=True)
result1 = result1.fillna(0).astype(int)
result2 = result2.fillna(0).astype(int)

print result1
print '\n'
print result2

# Convert to CSV files
result1.to_csv('tom_ira.csv', sep='\t', encoding='utf-8')
result2.to_csv('tom_mtc.csv', sep='\t', encoding='utf-8')
