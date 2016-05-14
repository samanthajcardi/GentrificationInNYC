# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:18:30 2016

@author: samanthacardi
"""

#Bronx Rent in 2014

import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
from bokeh.charts import Bar
from bokeh.charts.attributes import CatAttr
from bokeh.plotting import figure, output_file, show 

with open ('BronxRent2014H.csv', 'rU') as f:
    
    reader=csv.DictReader(f)
    l=reader.next()
  #  l=reader.next()
    
    Rent1=[]    
    Rent2=[]
    Rent3=[]
    Rent4=[]
    Rent5=[]
    Rent6=[]
    Rent7=[]
    Rent8=[]
    Rent9=[]
    Rent10=[]
    Rent11=[]
    Rent12=[]
    Rent13=[]
    Rent14=[]
    Rent15=[]
    Rent16=[]
    Rent17=[]
    Rent18=[]
    Rent19=[]
    Rent20=[]
    Rent21=[]

    
    for row in reader:
        Rent1.append(int(row['HD01_VD03']))
        Rent2.append(int(row['HD01_VD04']))
        Rent3.append(int(row['HD01_VD05']))
        Rent4.append(int(row['HD01_VD06']))
        Rent5.append(int(row['HD01_VD07']))
        Rent6.append(int(row['HD01_VD08']))
        Rent7.append(int(row['HD01_VD09']))
        Rent8.append(int(row['HD01_VD10']))
        Rent9.append(int(row['HD01_VD11']))
        Rent10.append(int(row['HD01_VD12']))
        Rent11.append(int(row['HD01_VD13']))
        Rent12.append(int(row['HD01_VD14']))
        Rent13.append(int(row['HD01_VD15']))
        Rent14.append(int(row['HD01_VD16']))
        Rent15.append(int(row['HD01_VD17']))
        Rent16.append(int(row['HD01_VD18']))
        Rent17.append(int(row['HD01_VD19']))
        Rent18.append(int(row['HD01_VD20']))
        Rent19.append(int(row['HD01_VD21']))
        Rent20.append(int(row['HD01_VD22']))
        Rent21.append(int(row['HD01_VD23']))
     
         

    
    totes=(Rent1+Rent2+Rent3+Rent4+Rent5+Rent6+Rent7+Rent8+Rent9+
           Rent10+Rent11+Rent12+Rent13+Rent14+Rent15+Rent16+
           Rent17+Rent18+Rent19+Rent20+Rent21)
    fiveless=totes[0:9]
    sum1=sum(fiveless)
    fivemore=totes[9:17]
    sum2=sum(fivemore)
    thousand1=totes[17:20]
    sum3=sum(thousand1)
    thousand2=totes[20:22]
    sum4=sum(thousand2)
    BlockList=[sum1]+[sum2]+[sum3]+[sum4]
    print BlockList
    BlockList=[i/1000 for i in BlockList]   
    
    category=['< $500', '$500-$999', '$1,000-$1,999', '$2,000 plus']


    d=pd.DataFrame({'labels':category, 'values':BlockList}, index=[1,2,3,4])
    p=Bar(d,values='values',label=CatAttr(sort=False, columns=['labels']), xlabel='Gross Rent', 
          ylabel='Number of People in Thousands', agg='min', title='Bronx Rent-2014',
          color='lightsalmon')
          
    output_file("BronxRent2014.html", title="Bronx Rent 2014")
    show (p)
    #http://factfinder.census.gov/bkmk/table/1.0/en/ACS/14_5YR/S1901/0600000US3604710022