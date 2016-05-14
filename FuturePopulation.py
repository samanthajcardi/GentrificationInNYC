# -*- coding: utf-8 -*-
"""
Created on Fri May  6 23:04:32 2016

@author: samanthacardi
"""
import csv
from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d 



with open ('Projected_Population_2010-2040_-_Summary.csv', 'rU') as f:
    reader = csv.reader(f)  
    l=reader.next()
    
    P2010=[]
    P2020=[]
    P2030=[]
    P2040=[]
    
        
    for row in reader:
        P2010.append(row[2])
        P2020.append(row[4])
        P2030.append(row[6])
        P2040.append(row[8])
    #print P2010

    
    Bronx=[P2010[1]]+[P2020[1]]+[P2030[1]]+[P2040[1]]
    Brooklyn=[P2010[2]]+[P2020[2]]+[P2030[2]]+[P2040[2]]
    Manhattan=[P2010[3]]+[P2020[3]]+[P2030[3]]+[P2040[3]]
    Queens=[P2010[4]]+[P2020[4]]+[P2030[4]]+[P2040[4]]
    SIsland=[P2010[5]]+[P2020[5]]+[P2030[5]]+[P2040[5]]
    
    Boros=[Bronx, Brooklyn, Manhattan, Queens, SIsland]    
    
    print "Bronx", Bronx
    print "Brooklyn", Brooklyn     
        
    Bronx=[int(i)/1000 for i in Bronx]
    Brooklyn=[int(i)/1000 for i in Brooklyn]
    Manhattan=[int(i)/1000 for i in Manhattan]
    #Queens=[int(i)/1000 for i in Queens]
    #SIsland=[int(i)/1000 for i in SIsland]
    
    
    BxPrevPop=[1318000,1365000, 1371000, 1385000, 1389000, 1397000, 1388000, 1396000] #1408000, 1419000, 1441000]
    BkPrevPop=[2447000, 2511000, 2523000, 2550000, 2567000, 2510000, 2541000, 2568000] #, 2592000, 2621000]
    
    
    BxPrevPop=[i/1000 for i in BxPrevPop]
    BkPrevPop=[i/1000 for i in BkPrevPop]    
    HistoricYears=[1999,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]

    
    years=[2010, 2020,2030,2040]

             
             
    p = figure(width=800, height=500)
    output_file("NYCfuturePop.html", title="futurePopulation")
    
    p.line(years, Bronx, color='orange', legend='Bronx')
    p.line(years, Brooklyn, color='purple', legend='Brooklyn')
    p.line(HistoricYears, BxPrevPop, color='orange')
    p.line(HistoricYears, BkPrevPop, color='purple')
#    p.line(years, Manhattan, color='green', legend='Manhattan')
#    p.line(years, Queens, color='red', legend='Queens')
#    p.line(years, SIsland, color='blue', legend='Staten Island')
    
    p.title = "Population in NYC"
    p.legend.location = "top_left"
    p.grid.grid_line_alpha=0
    p.xaxis.axis_label = 'Years'
    p.yaxis.axis_label = 'Number of People in Thousands'
    p.ygrid.band_fill_color="olive"
    p.ygrid.band_fill_alpha = 0.1

show(p)

