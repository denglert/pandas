###########################
### --- Tutorial 3  --- ###
###########################

# - Covered topics:
# * pandas I/O supported file types:
#   - csv
#   - html
#   - hdf5
#   - ...
# * specifying index column

#######################################################

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

#######################################################

df = pd.read_csv( 'ZILL-Z77006_MLP.csv' )

print( 'df.head()' )
print(  df.head()  )

# - Set index to be 'Date'
df.set_index('Date', inplace=True)

# - Write to csv
df.to_csv('newcsv2.csv')

# - Read in csv, while specifying the key (index_col)
df = pd.read_csv('newcsv2.csv', index_col=0)

# - Looking at the contents
print( '\ndf.head()' )
print(  df.head() )

# - Renaming all columns
df.columns = ['Austing_HPI']
print(  "\ndf.head()" )
print(     df.head() )

# - Writing out without header
df.to_csv('newcsv3.csv', header=False)

df = pd.read_csv( 'newcsv3.csv', names=['Date', 'Austin_HPI'], index_col=0 )
print(  "\ndf.head()" )
print(     df.head() )

# - Write it to html
df.to_html('example.html')

# - Renaming a single column instead of all
df.rename( columns={ 'Austin_HPI' : '77006_HPI'}, inplace=True )
print(  "\ndf.head()" )
print(     df.head() )
