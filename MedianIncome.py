# -*- coding: utf-8 -*-
"""
Created on Sat May 14 14:12:17 2016

@author: samanthacardi
"""

import math
from numpy import dot 
from linear_algebra import sum_of_squares, dot
from bokeh.charts import Bar, Line, Scatter
from bokeh.plotting import figure, output_file, show  
from bokeh.plotting import *
from scipy import stats
from scipy.stats import linregress
import pandas as pd
import numpy as np


def mean(x): 
    return sum(x) / len(x)

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero
        
def main():
    BkMedianIncome=[31726, 42894, 43567, 44593, 45215, 46085, 46958]
    BkInflatedIncome=[45082, 47332, 47299, 46931, 46621, 46832, 46958]
    Bkyears=[1999, 2009, 2010, 2011, 2012, 2013, 2014]

    Bxyears=[1999,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
    BxMedianIncome=[27315,32893, 32568, 32058, 32460, 33009, 33712] 
    

    BxInflatedIncome=[38814, 35429, 36982, 38998, 38487, 
                      36296, 35357, 33739, 33469, 33544, 33712]# 35429, 36982, 38998, 38487,



    p = figure(width=800, height=500, title='Income')
    output_file("Income.html", title="Income")
    
    p.line(Bxyears, BxInflatedIncome, color= 'darkmagenta', legend='Bronx Median Income')
    p.line(Bkyears, BkInflatedIncome, color='olivedrab', legend='Brooklyn Median Income' )
    p.xaxis.axis_label = 'Years'
    p.yaxis.axis_label = 'Dollars'
    p.legend.location = "top_left"
    

    print "Correlation of Inocme:", correlation(BxMedianIncome, BkMedianIncome)

    show(p)
main()