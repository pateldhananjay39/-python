# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 16:23:43 2025

@author: Lenovo
"""

Pandas import pandas as pd import seaborn as sns # initialise data of lists data = {'Name':[ 'Mohe' , 'Karnal' , 'Yrik' , 'jack' ],
'Age':[ 30 , 21 , 29 , 28 ]} df
= pd.DataFrame( data ) sns.violinplot(data['Age'])
