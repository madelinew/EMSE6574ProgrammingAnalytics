# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 20:12:17 2018

@author: Jonathan
"""
import pandas as pd
mort_data = pd.read_csv('mort.csv/mort.csv')

print(mort_data.shape)
print(mort_data.columns)

mask_states = mort_data.FIPS < 100

diseases_chosen = ['Neurological disorders',\
                   'Mental and substance use disorders',\
                   'Self-harm and interpersonal violence',\
                   'Transport injuries',\
                   'Nutritional deficiencies']
mask_disease = mort_data['Category'].isin(diseases_chosen)

filt_mort_data = mort_data[mask_states & mask_disease]
filt_mort_data.reset_index(inplace=True)
filt_mort_data.to_csv('filtered_mort_data.csv')