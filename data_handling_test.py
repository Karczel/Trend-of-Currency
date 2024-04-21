import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
# %matplotlib inline


df = pd.read_csv('Foreign_Exchange_Rates.csv')
df.head()