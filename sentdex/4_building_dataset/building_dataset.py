#!/usr/bin/env python

import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

##########################################3

# - Read in Quandl API key
api_key = open('../quandl_api.key', 'r').read()

#df = quandl.get("FMAC/HPI_AK", authtoken=api_key, start_date="1999-01-31")

#print(df.head() )


# - Read in list of US states abbreviations from Wikipedia
# - pandas puts the info into a list of DataFrames

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

# - Print contents of the list
#print(fiddy_states)

# - Print contents of the first element of the list
#print(fiddy_states[0])


# - Print only the abbreviations
# - Note: This is a pandas.Series
#print(fiddy_states[0][0][1:])

# - Print out the list of quandl codes
for abbv in fiddy_states[0][0][1:]:
    print('FMAC/HPI_{}'.format(abbv))
