#!/usr/bin/env python

###########################
### --- Tutorial 8  --- ###
###########################

# - Covered topics:
# * Modifying columns
#  - add a new column

import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

def state_list():
    # - Read in list of US states abbreviations from Wikipedia
    # - pandas puts the info into a list of DataFrames
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def grab_initial_state_data_pct_change():

    # - Read in Quandl API key
    api_key = open('../quandl_api.key', 'r').read()

    states = state_list()

    # - Create an empty DataFrame
    main_df = pd.DataFrame()
    
    # - Print out the list of quandl codes
    for abbv in states:
    #    print('FMAC/HPI_{}'.format(abbv))
        query = 'FMAC/HPI_{}'.format(abbv)
        df = quandl.get(query, authtoken=api_key)
        df = df.pct_change()
    
        # - Rename the column to the state name
        # - (otherwise .join throws an error)
        df.columns = [ str(abbv) ]
    
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join( df )

    print( 'main_df:', main_df.head() )

    # - Save the DataFrame into a python pickle (default)
    # - option 'wb' = write bytes
    pickle_out = open('fiddy_states_pct_change.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

def grab_initial_state_data():

    # - Read in Quandl API key
    api_key = open('../quandl_api.key', 'r').read()

    states = state_list()

    # - Create an empty DataFrame
    main_df = pd.DataFrame()
    
    # - Print out the list of quandl codes
    for abbv in states:
    #    print('FMAC/HPI_{}'.format(abbv))
        query = 'FMAC/HPI_{}'.format(abbv)
        df = quandl.get(query, authtoken=api_key)
        df[abbv] = (df[abbv] - df[abbv][0])/df[abbv][0] * 100.0
    
        # - Rename the column to the state name
        # - (otherwise .join throws an error)
        df.columns = [ str(abbv) ]
    
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join( df )

    print( 'main_df:', main_df.head() )

    # - Save the DataFrame into a python pickle (default)
    # - option 'wb' = write bytes
    pickle_out = open('fiddy_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

# - Create pickles
#grab_initial_state_data_pct_change()
grab_initial_state_data()

# - Load in the pickle with pandas
HPI_data = pd.read_pickle('fiddy_states.pickle')

# - Add a new column to the DataFrame
#HPI_data['TX2'] = HPI_data['TX']  * 2.0
#print("HPI_data[['TX','TX2']]", HPI_data[ ['TX', 'TX2'] ] )

HPI_data.plot()
plt.legend().remove()
plt.show()
