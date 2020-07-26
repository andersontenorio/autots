# -*- coding: utf-8 -*-

import pandas as pd

def load_temperatures():
    
    df = pd.read_csv("data/daily-min-temperatures.csv", index_col="index")
    
    return df

def load_births():
    
    df = pd.read_csv("data/daily-total-female-births.csv", index_col="index")
    
    return df

def load_sunspots():
    
    df = pd.read_csv("data/monthly-sunspots.csv", index_col="index")
    
    return df

def load_shampoo():
    
    df = pd.read_csv("data/shampoo.csv", index_col="index")
    
    return df