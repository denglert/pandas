#!/usr/bin/env python

import Quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

##########################################3

# - Read in Quandl API key
api_key = open('quandl_api.key', 'r').read()

df = quandl.get("FMAC/HPI_AK", authtoken=api_key, start_date="1999-01-31")

