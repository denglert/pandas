###########################
### --- Tutorial 6  --- ###
###########################

# - Covered topics:
# * Combining DataFrames
#   - merging
#   - joining

#!/usr/bin/env python

import pandas as pd

###################################


df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

###################################

##########################
### --- pd.merge() --- ###
##########################

# - pd.merge() properties:
# - have to specify 'what to merge on'
# - ignores index

print('\ndf1\n', df1 )
print('\ndf2\n', df2 )

#
merge_a = pd.merge(df1, df2, on='HPI')
print('\nmerge_a\n', merge_a )

#
merge_b = pd.merge(df1, df2, on=['HPI', 'Int_rate'])
print('\nmerge_b\n', merge_b )

##########################
### --- pd.join() --- ###
##########################

# - index is honoured by pd.join()

#joined = df1.join(df3)
#print('\njoined\n', joined )
# - This gives the following error:
# - ValueError: columns overlap but no suffix specified: Index(['HPI'], dtype='object')

df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)

joined = df1.join(df3)
print('\njoined\n', joined )


##############################

df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})

print('\nMerging of table: left, right, inner, outer' )

merged_left = pd.merge(df1, df3, on='Year', how='left')
print('\nmerged_left\n', merged_left )

merged_right = pd.merge(df1, df3, on='Year', how='right')
print('\nmerged_right\n', merged_right )

merged_inner = pd.merge(df1, df3, on='Year', how='inner')
print('\nmerged_inner\n', merged_inner )

merged_outer = pd.merge(df1, df3, on='Year', how='outer')
print('\nmerged_outer\n', merged_outer )


#merged.set_index('Year', inplace=True)
#print('\nmerged\n', merged )
