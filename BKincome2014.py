# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:02:25 2016

@author: samanthacardi
"""
#Graph of Brooklyn Income in 2014

import csv
import matplotlib.pyplot as plt
import numpy as np
from bokeh.charts import Bar, Line
from bokeh.charts.attributes import CatAttr
from bokeh.models import Range1d, TickFormatter
from bokeh.plotting import figure, output_file, show 


with open ('BKgeneral2014H.csv', 'rU') as f:
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
        income1.append(row['HC01_VC75'])
        income2.append(row['HC01_VC76'])
        income3.append(row['HC01_VC77'])
        income4.append(row['HC01_VC78'])
        income5.append(row['HC01_VC79'])
        income6.append(row['HC01_VC80'])
        income7.append(row['HC01_VC81'])
        income8.append(row['HC01_VC82'])
        income9.append(row['HC01_VC83'])
        income10.append(row['HC01_VC84'])
        
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
    
    
    totalincome=[income1]+[income2]+[income3]+[income4]+[income5]+[income6]+[income7]+[income8]+[income9]+[income10]

    values=[float(i)/1000 for i in totalincome ]    
            
        
    category=['less than $10,000', '10,000-14,999', '15,000-24,000', 
             '25,000-34,999', '35,000-49,000', '50,000-74,999',
             '75,000-99,999', '100,000-149,000', '150,000-199,999',
             '200,000+']
    d=pd.DataFrame({'labels':category, 'values':values}, index=[1,2,3,4,5,6,7,8,9,10])
    p=Bar(d,values='values',label=CatAttr(sort=False, columns=['labels']), xlabel='Income', 
          ylabel='Number of People in Thousands', agg='min', title='BK Income 2014', color='darkseagreen')


    output_file("Income2014.html")
    
    show(p)