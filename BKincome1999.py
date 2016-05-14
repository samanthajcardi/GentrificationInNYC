# -*- coding: utf-8 -*-
"""
Created on Sun May  1 12:51:26 2016

@author: samanthacardi
"""

import csv
import matplotlib.pyplot as plt
import pandas as pd
from bokeh.charts import Bar, Line
from bokeh.charts.attributes import CatAttr
from bokeh.models import Range1d, TickFormatter
from bokeh.plotting import figure, output_file, show 


with open ('1999BKgeneral.csv', 'rU') as f:
    reader=csv.DictReader(f)
    l=reader.next
    l=reader.next
    
    
    income1=[]
    income2=[]
    income3=[]
    income4=[]
    income5=[]
    income6=[]
    income7=[]
    income8=[]
    income9=[]
    income10=[]
    
    for row in reader:
        income1.append(row['HC01_VC54'])
        income2.append(row['HC01_VC55'])
        income3.append(row['HC01_VC56'])
        income4.append(row['HC01_VC57'])
        income5.append(row['HC01_VC58'])
        income6.append(row['HC01_VC59'])
        income7.append(row['HC01_VC60'])
        income8.append(row['HC01_VC61'])
        income9.append(row['HC01_VC62'])
        income10.append(row['HC01_VC63'])
    print income1
        
        
    income1=income1[1]
    income2=income2[1]
    income3=income3[1]
    income4=income4[1]
    income5=income5[1]
    income6=income6[1]
    income7=income7[1]
    income8=income8[1]
    income9=income9[1]
    income10=income10[1]
    print income1
    

    totalincome=[income1]+[income2]+[income3]+[income4]+[income5]+[income6]+[income7]+[income8]+[income9]+[income10]
    values=[float(i)/1000 for i in totalincome ]    
            
        
    category=['less than $10,000', '10,000-14,999', '15,000-24,000', 
             '25,000-34,999', '35,000-49,000', '50,000-74,999',
             '75,000-99,999', '100,000-149,000', '150,000-199,999',
             '200,000+']
    d=pd.DataFrame({'labels':category, 'values':values}, index=[1,2,3,4,5,6,7,8,9,10])
    p=Bar(d,values='values',label=CatAttr(sort=False, columns=['labels']), xlabel='Income', 
          ylabel='Number of People in Thousands', agg='min', title='Brooklyn Income 1999')


    output_file("bar2.html")
    
    show(p)