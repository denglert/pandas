###########################
### --- Tutorial 2  --- ###
###########################

# - Covered topics:
# * Creating a pd.DataFrame from dictionary
# * Creating a pd.DataFrame from a np.array
# * Accessing pd.DataFrame columns
#   - single column
#   - multiple columns

#######################################################

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

#######################################################

# - pandas.DataFrame
# - lot like a python dictionary at its heart
# - the way we can reference it is like a dictionary

web_stats = {
             'Day':         [1,2,3,4,5,6],
             'Visitors':    [45,53,34,45,64,34],
             'Bounce_Rate': [65,72,62,64,54,66]
            }

# - Dictionary suits the DataFrame really easily
df = pd.DataFrame( web_stats )

print( df )
print( df.head(3) )
print( df.tail(3) )

# - Setting the index for the DataFrame
# - Note: set_index() returns the modified DataFrame,
# - it doesn't set it in place on default.

print( df.set_index('Day') )
print( "After print( df.set_index('Day') )." )
print( "df.head(3):" )
print( df.head(3) )

df_new = df.set_index('Day')

print( "df_new.head():" )
print( df_new.head() )

# - Set the index in place of the DataFrame
df.set_index('Day', inplace=True)

print( "\ndf.head():" )
print(    df.head(3) )


# - Reference the column like with dictionaries
print( "\ndf['Visitors']" )
print(    df['Visitors'] )


# - Reference the column as an attribute
print( "\ndf.Visitors" )
print(   df.Visitors )

# - Reference multiple columns
print( "\ndf[ ['Bounce_Rate','Visitors'] ]" )
print(    df[ ['Bounce_Rate','Visitors']  ] )

# - How to convert a DataFrame column into a list
print( "\ndf.Visitors.tolist()" )
print(    df.Visitors.tolist()  )

# - Q: Can we convert multiple DataFrame coumns into a list in a list?
# print( "df[ ['Visitors', 'Bounce_Rate'] ].tolist()" )
# print(  df[ ['Visitors', 'Bounce_Rate'] ].tolist()  )

# - A: No.
# - Instead: Use numpy arrays: np.array(  ) 

print( "\nnp.array( df[ ['Visitors', 'Bounce_Rate'] ] )" )
print(    np.array( df[ ['Visitors', 'Bounce_Rate'] ] )  )


# - Creating a DataFrame from a numpy array.

arrayVB = np.array( df[ ['Visitors', 'Bounce_Rate'] ] )
df2     = pd.DataFrame( arrayVB )

print( "df2" )
print(  df2 )
