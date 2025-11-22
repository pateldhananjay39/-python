# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 16:22:59 2025

@author: Lenovo
"""

import pandas as pd import
seaborn as sns


# initialise data of lists data = {'Name':[ 'Mohe' , 'Karnal' , 'Yrik' , 'jack' ],
'Age':[ 30 , 21 , 29 , 28 ]} df
= pd.DataFrame( data ) sns.boxplot( data['Age'] )
