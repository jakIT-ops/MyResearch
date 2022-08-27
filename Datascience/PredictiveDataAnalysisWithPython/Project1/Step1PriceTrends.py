import pandas as pd
import matplotlib.pyplot as plt

sys = pd.read_csv('/data/Year_2018/SYS.csv') #The "SYS" file name can be changed to "NETSOL", "AVN" and "PTC".
sys['Time'] = pd.to_datetime(sys.Time) # correc the format of date
sys = sys.set_index('Time') # Set time column as row index


days = [10, 30 , 60] # Multiple number of days
for day in days:
    col_name = "mv_avg for " + str(day) + " days" # New column to store moving average values
    sys[col_name] = sys['Close'].rolling(day).mean() # Calculating moving average
    
sys[['Close', 'mv_avg for 10 days', 'mv_avg for 30 days', 'mv_avg for 60 days']].plot(subplots = False, figsize=(15,10))

