#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:11:30 2017

@author: feng
"""

import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Extract all file names, and use two lists to save file names
file_names = glob.glob('*.xlsx')
files_ira = []
files_mtc = []

# Classify the file names according to ira/mtc
for s in file_names:
    if s[:14] == 'Report tom_ira':
        files_ira.append(s)
    else:
        files_mtc.append(s)

# Read excel files, and save the dates and DataFrame in lists
date_ira = []
date_mtc = []
df_ira = []
df_mtc = []

for s in files_ira:
    temp_date = s[15:-5]
    temp_df = pd.read_excel(s, 'Account Stats by Status')
    date_ira.append(temp_date)
    df_ira.append(temp_df)

for s in files_mtc:
    temp_date = s[15:-5]
    temp_df = pd.read_excel(s, 'Account Stats by Status')
    date_mtc.append(temp_date)
    df_mtc.append(temp_df)

# Use 5 lists to record the data in each month
grace_period_ira = [0] * 7
late_stage_1_ira = [0] * 7
late_stage_2_ira = [0] * 7
default_ira = [0] * 7
charged_off_ira = [0] * 7
index = 0

for d in df_ira:
    if 'In Grace Period' in d.loanStatus.values:
        temp1 = d.get_value(d.loanStatus[d.loanStatus == 'In Grace Period'].index.tolist()[0], 'count')
    else:
        temp1 = 0
    if 'Late (16-30 days)' in d.loanStatus.values:
        temp2 = d.get_value(d.loanStatus[d.loanStatus == 'Late (16-30 days)'].index.tolist()[0], 'count')
    else:
        temp2 = 0
    if 'Late (31-120 days)' in d.loanStatus.values:
        temp3 = d.get_value(d.loanStatus[d.loanStatus == 'Late (31-120 days)'].index.tolist()[0], 'count')
    else:
        temp3 = 0
    if 'Default' in d.loanStatus.values:
        temp4 = d.get_value(d.loanStatus[d.loanStatus == 'Default'].index.tolist()[0], 'count')
    else:
        temp4 = 0
    if 'Charged Off' in d.loanStatus.values:
        temp5 = d.get_value(d.loanStatus[d.loanStatus == 'Charged Off'].index.tolist()[0], 'count')
    else:
        temp5 = 0
    # Append the values to the 5 lists
    if date_ira[index][5:-3] == '04':
        grace_period_ira[0] += temp1
        late_stage_1_ira[0] += temp2
        late_stage_2_ira[0] += temp3
        default_ira[0] += temp4
        charged_off_ira[0] += temp5
    if date_ira[index][5:-3] == '05':
        grace_period_ira[1] += temp1
        late_stage_1_ira[1] += temp2
        late_stage_2_ira[1] += temp3
        default_ira[1] += temp4
        charged_off_ira[1] += temp5
    if date_ira[index][5:-3] == '06':
        grace_period_ira[2] += temp1
        late_stage_1_ira[2] += temp2
        late_stage_2_ira[2] += temp3
        default_ira[2] += temp4
        charged_off_ira[2] += temp5
    if date_ira[index][5:-3] == '07':
        grace_period_ira[3] += temp1
        late_stage_1_ira[3] += temp2
        late_stage_2_ira[3] += temp3
        default_ira[3] += temp4
        charged_off_ira[3] += temp5
    if date_ira[index][5:-3] == '08':
        grace_period_ira[4] += temp1
        late_stage_1_ira[4] += temp2
        late_stage_2_ira[4] += temp3
        default_ira[4] += temp4
        charged_off_ira[4] += temp5
    if date_ira[index][5:-3] == '09':
        grace_period_ira[5] += temp1
        late_stage_1_ira[5] += temp2
        late_stage_2_ira[5] += temp3
        default_ira[5] += temp4
        charged_off_ira[5] += temp5
    if date_ira[index][5:-3] == '10':
        grace_period_ira[6] += temp1
        late_stage_1_ira[6] += temp2
        late_stage_2_ira[6] += temp3
        default_ira[6] += temp4
        charged_off_ira[6] += temp5
    index += 1

# Use 5 lists to record the data in each month
grace_period_mtc = [0] * 7
late_stage_1_mtc = [0] * 7
late_stage_2_mtc = [0] * 7
default_mtc = [0] * 7
charged_off_mtc = [0] * 7
index = 0

for d in df_mtc:
    if 'In Grace Period' in d.loanStatus.values:
        temp1 = d.get_value(d.loanStatus[d.loanStatus == 'In Grace Period'].index.tolist()[0], 'count')
    else:
        temp1 = 0
    if 'Late (16-30 days)' in d.loanStatus.values:
        temp2 = d.get_value(d.loanStatus[d.loanStatus == 'Late (16-30 days)'].index.tolist()[0], 'count')
    else:
        temp2 = 0
    if 'Late (31-120 days)' in d.loanStatus.values:
        temp3 = d.get_value(d.loanStatus[d.loanStatus == 'Late (31-120 days)'].index.tolist()[0], 'count')
    else:
        temp3 = 0
    if 'Default' in d.loanStatus.values:
        temp4 = d.get_value(d.loanStatus[d.loanStatus == 'Default'].index.tolist()[0], 'count')
    else:
        temp4 = 0
    if 'Charged Off' in d.loanStatus.values:
        temp5 = d.get_value(d.loanStatus[d.loanStatus == 'Charged Off'].index.tolist()[0], 'count')
    else:
        temp5 = 0
    # Append the values to the 5 lists
    if date_mtc[index][5:-3] == '04':
        grace_period_mtc[0] += temp1
        late_stage_1_mtc[0] += temp2
        late_stage_2_mtc[0] += temp3
        default_mtc[0] += temp4
        charged_off_mtc[0] += temp5
    if date_mtc[index][5:-3] == '05':
        grace_period_mtc[1] += temp1
        late_stage_1_mtc[1] += temp2
        late_stage_2_mtc[1] += temp3
        default_mtc[1] += temp4
        charged_off_mtc[1] += temp5
    if date_mtc[index][5:-3] == '06':
        grace_period_mtc[2] += temp1
        late_stage_1_mtc[2] += temp2
        late_stage_2_mtc[2] += temp3
        default_mtc[2] += temp4
        charged_off_mtc[2] += temp5
    if date_mtc[index][5:-3] == '07':
        grace_period_mtc[3] += temp1
        late_stage_1_mtc[3] += temp2
        late_stage_2_mtc[3] += temp3
        default_mtc[3] += temp4
        charged_off_mtc[3] += temp5
    if date_mtc[index][5:-3] == '08':
        grace_period_mtc[4] += temp1
        late_stage_1_mtc[4] += temp2
        late_stage_2_mtc[4] += temp3
        default_mtc[4] += temp4
        charged_off_mtc[4] += temp5
    if date_mtc[index][5:-3] == '09':
        grace_period_mtc[5] += temp1
        late_stage_1_mtc[5] += temp2
        late_stage_2_mtc[5] += temp3
        default_mtc[5] += temp4
        charged_off_mtc[5] += temp5
    if date_mtc[index][5:-3] == '10':
        grace_period_mtc[6] += temp1
        late_stage_1_mtc[6] += temp2
        late_stage_2_mtc[6] += temp3
        default_mtc[6] += temp4
        charged_off_mtc[6] += temp5
    index += 1

print grace_period_ira
print late_stage_1_ira
print late_stage_2_ira
print default_ira
print charged_off_ira
print '\n'
print grace_period_mtc
print late_stage_1_mtc
print late_stage_2_mtc
print default_mtc
print charged_off_mtc

# Line chart
plt.plot(grace_period_ira)
plt.plot(late_stage_1_ira)
plt.plot(late_stage_2_ira)
plt.plot(default_ira)
plt.plot(charged_off_ira)
plt.show()

plt.plot(grace_period_mtc)
plt.plot(late_stage_1_mtc)
plt.plot(late_stage_2_mtc)
plt.plot(default_mtc)
plt.plot(charged_off_mtc)
plt.show()

# Axis of area chart
x = np.arange(4, 11)
y1 = default_ira
y2 = [0] * 7
y3 = [0] * 7
y4 = [0] * 7
y5 = [0] * 7

for i in range(0, 7):
    y2[i] = late_stage_1_ira[i] - default_ira[i]
    y3[i] = grace_period_ira[i] - late_stage_1_ira[i]
    y4[i] = late_stage_2_ira[i] - grace_period_ira[i]
    y5[i] = charged_off_ira[i] - late_stage_2_ira[i]

# Use area chart
y = np.row_stack((y1, y2, y3, y4, y5))
fig, ax = plt.subplots()
ax.stackplot(x, y, colors=['#4775c2', '#eb7e3c', '#a5a5a5', '#fec02d', '#5e9dd3'])
fig.suptitle('Loan Evolution', fontsize=16)
plt.legend([mpatches.Patch(color='#4775c2'),  
            mpatches.Patch(color='#eb7e3c'), 
            mpatches.Patch(color='#a5a5a5'),
            mpatches.Patch(color='#fec02d'), 
            mpatches.Patch(color='#5e9dd3')], 
           ['Default', 'Late Stage 1', 'Grace Period', 'Late Stage 2', 'Charged Off'],
           loc='upper left')
plt.show()

# Axis of area chart
m = np.arange(4, 11)
n1 = default_mtc
n2 = [0] * 7
n3 = [0] * 7
n4 = [0] * 7
n5 = [0] * 7

for i in range(0, 7):
    n2[i] = late_stage_1_mtc[i] - default_mtc[i]
    n3[i] = charged_off_mtc[i] - late_stage_1_mtc[i]
    n4[i] = grace_period_mtc[i] - charged_off_mtc[i]
    n5[i] = late_stage_2_mtc[i] - grace_period_mtc[i]

# Use area chart
n = np.row_stack((n1, n2, n3, n4, n5))
fig, ax = plt.subplots()
ax.stackplot(m, n, colors=['#4775c2', '#eb7e3c', '#a5a5a5', '#fec02d', '#5e9dd3'])
fig.suptitle('Loan Evolution', fontsize=16)
plt.legend([mpatches.Patch(color='#4775c2'),  
            mpatches.Patch(color='#eb7e3c'), 
            mpatches.Patch(color='#a5a5a5'),
            mpatches.Patch(color='#fec02d'), 
            mpatches.Patch(color='#5e9dd3')], 
           ['Default', 'Late Stage 1', 'Charged Off', 'Grace Period', 'Late Stage 2'],
           loc='upper left')
plt.show()
