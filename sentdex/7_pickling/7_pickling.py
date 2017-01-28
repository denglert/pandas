#!/usr/bin/env python

###########################
### --- Tutorial 7  --- ###
###########################

# - Covered topics:
# * Pickling

import quandl
import pandas as pd
import pickle


def state_list():
    # - Read in list of US states abbreviations from Wikipedia
    # - pandas puts the info into a list of DataFrames
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]


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

# - Download the data once
#grab_initial_state_data()

# - Open the pickle with default python pickle library
pickle_in = open('fiddy_states.pickle', 'rb')
HPI_data  = pickle.load(pickle_in)
print('HPI_data', HPI_data)

# - Open the pickle with default python pickle library
pickle_in = open('fiddy_states.pickle', 'rb')
HPI_data  = pickle.load(pickle_in)
#print('HPI_data', HPI_data)

# - Load in the pickle with pandas
HPI_data2 = pd.read_pickle('fiddy_states.pickle')
print('HPI_data2', HPI_data2)

# - You can write to pickle in pandas using
# df.to_pickle('fiddy_states2.pickle')
