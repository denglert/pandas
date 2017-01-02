import pandas as pd
import datetime
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

##############################

style.use('ggplot')


# - Start and end dates
start = datetime.datetime(2014, 1, 1)
end   = datetime.datetime(2016, 12, 1)

# - Get USD/GBP and USD/HUF rates from Yahoo! Finance
df_gbp = web.DataReader("GBP=X", "yahoo", start, end)
df_huf = web.DataReader("HUF=X", "yahoo", start, end)

# - Print out the head
print( df_gbp.head() )
print( df_huf.head() )

#print( df_gbp.tail() )
#print( df_huf.tail() )

# - Show USD/GBP exchange rates
#df_gbp['Adj Close'].plot()
#plt.show()


# - Make numpy arrays out of the */USD rates
gbp = np.array( df_gbp['Adj Close'] )
huf = np.array( df_huf['Adj Close'] )

# - The 'Date' field in the DataFrame is an index here
# - To transform it into a column, we use
df_gbp.reset_index(inplace=True,drop=False)
dates = np.array( df_gbp['Date'] )

# - Create HUF/GBP cross exchange rate
gbp2huf = huf/gbp[:761]

# - Plot
plt.plot( dates[:761], gbp2huf  )
plt.show()
