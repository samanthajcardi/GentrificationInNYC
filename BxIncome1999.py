# -*- coding: utf-8 -*-
"""
Created on Sun May  1 19:39:43 2016

@author: samanthacardi
"""
#Graph of Bronx income in 1999
import csv
import pandas as pd
from bokeh.charts import Bar
from bokeh.charts.attributes import CatAttr
from bokeh.plotting import output_file, show 


with open ('BronxGeneral1999H.csv', 'rU') as f:
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
    
        
    income1=income1[2]
    income2=income2[2]
    income3=income3[2]
    income4=income4[2]
    income5=income5[2]
    income6=income6[2]
    income7=income7[2]
    income8=income8[2]
    income9=income9[2]
    income10=income10[2]
    
    
    
    
    totalincome=[income1]+[income2]+[income3]+[income4]+[income5]+[income6]+[income7]+[income8]+[income9]+[income10]
    values=[float(i)/1000 for i in totalincome ]    
            
        
    category=['less than $10,000', '$10,000-$14,999', '$15,000-$24,000', 
             '$25,000-$34,999', '$35,000-$49,000', '$50,000-$74,999',
             '$75,000-$99,999', '$100,000-$149,000', '$150,000-$199,999',
             '$200,000+']
             
    d=pd.DataFrame({'labels':category, 'values':values}, index=[1,2,3,4,5,6,7,8,9,10])
    p=Bar(d,values='values',label=CatAttr(sort=False, columns=['labels']), xlabel='Income', 
          ylabel='Number of People in Thousands', agg='min', title='Bronx Income 1999',
          color='plum')


    output_file("BronxIncome1999.html")
    
    show(p)    
    