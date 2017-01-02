#!/usr/bin/env python

import pandas as pd

df1 = pd.DataFrame({'mH' :[100,100,100,100],
                    'mA' :[100,100,100,100],
                    'mHc':[100,200,300,400]},
                   index = [1, 2, 3, 4])

df2 = pd.DataFrame({'mH' :[200,200,200,200],
                    'mA' :[100,100,100,100],
                    'mHc':[100,200,300,400]},
                   index = [1, 2, 3, 4])

df3 = pd.DataFrame({'mH' :[200,200,200,200],
                    'mA' :[100,100,100,100],
                    'mHc':[100,200,300,400],
                    'xsec':[0.5,0.3,0.1,0.01]},
                   index = [1, 2, 3, 4])

print('\ndf1\n', df1)
print('\ndf2\n', df2)
print('\ndf3\n', df3)

#############

# - Add df1 and df2 together
a_1 = pd.concat([df1,df2])
print('\na_1\n', a_1)

a_2 = df1.append( df2 )
print('\na_2\n', a_2)

######

b_1 = pd.merge(df2,df3, on=['mHc', 'mA', 'mH'])
print('\nb\n', b_1)


#df2.set_index('mHc', inplace=True)
#df3.set_index('mHc', inplace=True)

#b_2 = df2.join(df3, on=['mHc', 'mA', 'mH'])
#print('\nb\n', b_2)
