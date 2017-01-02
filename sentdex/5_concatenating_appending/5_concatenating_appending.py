###########################
### --- Tutorial 5  --- ###
###########################

# - Covered topics:
# * Combining DataFrames
#   - concatenating
#   - appending

#!/usr/bin/env python

import pandas as pd

###################################


df1 = pd.DataFrame( {'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004] ) 

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004] )

####################################

###########################
### --- pd.concat() --- ###
###########################


# - Concatenate df1 and df2
# - df1 indeces: 2001, 2002, 2003, 2004
# - df2 indeces: 2005, 2006, 2007, 2008
# - Result: DataFrame containing both df1 and df2
#   concat() = just adds the DataFrame to the bottom
concat = pd.concat([df1, df2])

print('\nconcat( [df1, df2 ] )\n', concat)

# - Concatenate df1, df2 and df3
# - df1 indeces: 2001, 2002, 2003, 2004
# - df2 indeces: 2005, 2006, 2007, 2008
# - df3 indeces: 2001, 2002, 2003, 2004
# - Result: DataFrame containing df1, df2 and df3
#     Note: Repeating indeces coming from df1 and df3.
#   concat() = just adds the DataFrame to the bottom

concat = pd.concat([df1, df2, df3])

print('\nconcat( [df1, df2, df3] )\n', concat)

###########################
### --- pd.append() --- ###
###########################


# - Append df2 to df1
# - Result: DataFrame df2 is appended into df1

df4 = df1.append(df2)
print('\ndf1.append( df2 )\n', df4)

# - Append df3 to df1
# - Result: DataFrame df3 is appended into df1

df5 = df1.append(df3)
print('\ndf5.append( df3 )\n', df5)

###########

s = pd.Series([80, 2, 50], index = ['HPI','Int_rate', 'US_GDP_Thousands'])

df6 = df1.append(s, ignore_index = True)
print('\ndf6.append(a, ignore_index  )\n', df6 )
