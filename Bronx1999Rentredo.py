# -*- coding: utf-8 -*-
"""
Created on Sun May  1 22:40:57 2016

@author: samanthacardi
"""

#Bronx Rent from 1999--REDO BETTER ONE
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
from bokeh.charts import Bar
from bokeh.charts.attributes import CatAttr
from bokeh.plotting import figure, output_file, show 

with open ('BronxRent1999H.csv', 'rU') as f:
    
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
        Rent1.append(int(row['VD03']))
        Rent2.append(int(row['VD04']))
        Rent3.append(int(row['VD05']))
        Rent4.append(int(row['VD06']))
        Rent5.append(int(row['VD07']))
        Rent6.append(int(row['VD08']))
        Rent7.append(int(row['VD09']))
        Rent8.append(int(row['VD10']))
        Rent9.append(int(row['VD11']))
        Rent10.append(int(row['VD12']))
        Rent11.append(int(row['VD13']))
        Rent12.append(int(row['VD14']))
        Rent13.append(int(row['VD15']))
        Rent14.append(int(row['VD16']))
        Rent15.append(int(row['VD17']))
        Rent16.append(int(row['VD18']))
        Rent17.append(int(row['VD19']))
        Rent18.append(int(row['VD20']))
        Rent19.append(int(row['VD21']))
        Rent20.append(int(row['VD22']))
        Rent21.append(int(row['VD23']))
        
     
    Rent1=Rent1[0]
    Rent2=Rent2[0]
    Rent3=Rent3[0]
    Rent4=Rent4[0]
    Rent5=Rent5[0]
    Rent6=Rent6[0]
    Rent7=Rent7[0]
    Rent8=Rent8[0]
    Rent9=Rent9[0]
    Rent10=Rent10[0]
    Rent11=Rent11[0]
    Rent12=Rent12[0]
    Rent13=Rent13[0]
    Rent14=Rent14[0]
    Rent15=Rent15[0]
    Rent16=Rent16[0]
    Rent17=Rent17[0]
    Rent18=Rent18[0]
    Rent19=Rent19[0]
    Rent20=Rent20[0]
    Rent21=Rent21[0]
           

    
    totes=[Rent1,Rent2,Rent3,Rent4,Rent5,Rent6,Rent7,Rent8,Rent9,
           Rent10,Rent11,Rent12,Rent13,Rent14,Rent15,Rent16,
           Rent17,Rent18,Rent19,Rent20,Rent21]
   # print totes
       
    fiveless=totes[0:9]
    sum1=sum(fiveless)
    fivemore=totes[9:17]
    sum2=sum(fivemore)
    thousand1=totes[17:20]
    sum3=sum(thousand1)
    thousand2=totes[20:22]
    sum4=sum(thousand2)
    BlockList=[sum1]+[sum2]+[sum3]+[sum4]
    BlockList=[i/1000 for i in BlockList]   
    
    category=['< $500', '$500-$999', '$1,000-$1,999', '$2,000 plus']


    d=pd.DataFrame({'labels':category, 'values':BlockList}, index=[1,2,3,4])
    p=Bar(d,values='values',label=CatAttr(sort=False, columns=['labels']), xlabel='Gross Rent', 
          ylabel='Number of People in Thousands', agg='min', title='Bronx Rent-1999',
          color='plum')
          
    output_file("BronxRent1999.html", title="Bronx Rent 1999")
    show (p)
          
    
    