import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sys = pd.read_csv('data/Year_2018/SYS.csv')
#The "SYS" file name can be changed to "NETSOL", "AVN" and "PTC".
sys['Time'] = pd.to_datetime(sys.Time) # correct the format of date
sys = sys.set_index('Time') # Set Time column as row index

daily_return = sys['Close'].pct_change() # Calculate the daily returns

sys['daily_return'] = daily_return # Create new column and assign daily return values to it

plt.ylabel('Probability Density Value') # Assign a name to the y-axis of plot

sns.distplot(sys['daily_return'].dropna(), bins = 100, color = 'red') # plots a distribution graph of KDE and histogram
