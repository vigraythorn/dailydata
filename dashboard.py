# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

time_series = pd.read_excel('time-series 6 Jan 2018v2.xlsx', 'With Numerical Values')

# 创建两个header与原文件一样的dataframe
'''
up = time_series.copy()
down = time_series.copy()
up.set_index('LoanID', inplace=True)
down.set_index('LoanID', inplace=True)
up.drop(up.index, inplace=True)
down.drop(down.index, inplace=True)
'''

chart = time_series.copy()
chart.set_index('LoanID', inplace=True)
chart.drop(chart.index, inplace=True)

# bad, good六，四排全部初始为0
'''
for i in range(6):
    up.loc[i] = [0 for n in range(684)]
for i in range(4):
    down.loc[i] = [0 for n in range(684)]
'''

for i in range(5):
    chart.loc[i] = [0 for n in range(684)]

for index, row in time_series.iterrows():
    for i in range(1, 685):
        if row[i] == 2:
            chart.loc[0, time_series.columns[i]] += 1
        if row[i] == 3:
            chart.loc[1, time_series.columns[i]] += 1
        if row[i] == 4:
            chart.loc[2, time_series.columns[i]] += 1
        if row[i] == 5:
            chart.loc[3, time_series.columns[i]] += 1
        if row[i] == 6:
            chart.loc[4, time_series.columns[i]] += 1
# 循环表格
'''
for index, row in time_series.iterrows():
    last = row[1]
    for i in range(1, 685):
        if row[i] > last:
            if row[i] == 1:
                up.loc[0, time_series.columns[i]] += 1
            elif row[i] == 2:
                up.loc[1, time_series.columns[i]] += 1
            elif row[i] == 3:
                up.loc[2, time_series.columns[i]] += 1
            elif row[i] == 4:
                up.loc[3, time_series.columns[i]] += 1
            elif row[i] == 5:
                up.loc[4, time_series.columns[i]] += 1
            elif row[i] == 6:
                up.loc[5, time_series.columns[i]] += 1
            last = row[i]
        else:
            continue

for index, row in time_series.iterrows():
    last = row[1]
    for i in range(1, 685):
        if row[i] < last:
            if row[i] == -1:
                down.loc[0, time_series.columns[i]] += 1
            elif row[i] == 1:
                down.loc[1, time_series.columns[i]] += 1
            elif row[i] == 2:
                down.loc[2, time_series.columns[i]] += 1
            else:
                down.loc[3, time_series.columns[i]] += 1
            last = row[i]
        elif row[i] > last:
            last = row[i]
        else:
            continue
'''

#up.index = pd.to_datetime(up.index)
#up1 = up.groupby(pd.Grouper(key='date', freq='1M')).sum() # groupby each 1 month
#up1.index = up1.index.strftime('%B')

chart = chart.T

print chart.index
'''
up.T.to_csv('bad.csv', sep=',', encoding='utf-8')
down.T.to_csv('good.csv', sep=',', encoding='utf-8')
'''

chart.to_csv('chart.csv', sep=',', encoding='utf-8')