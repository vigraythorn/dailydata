#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 12:21:27 2018

@author: butter
"""

import pandas as pd

dates = pd.read_csv('chart1.csv')

dates.date = pd.to_datetime(dates.date)
df = dates.groupby(pd.Grouper(key='date', freq='1M')).sum() # groupby each 1 month
df.index = df.index.strftime('%B')

print df
df.to_csv('df.csv', sep=',', encoding='utf-8')