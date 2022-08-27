# Importing the packages
import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt  
from scipy.stats import norm

# Preprocessing steps as before
sys = pd.read_csv('data/Year_2018/SYS.csv')
sys['Time'] = pd.to_datetime(sys.Time)
sys = sys.set_index('Time')

daily_returns = sys['Close'].pct_change() # Calculating daily returns
log_returns = np.log(1 + daily_returns) # Calculating log returns from daily returns

avg = log_returns.mean() # Calculating average of log returns
var = log_returns.var() # Calculating variance
drift = avg - (var / 2.0) # Calculating drift
drift = np.array(drift) # Convert to array


pred_price_overDays = 60 # Number of days
pred_count = 10 # Range of prediction

std = log_returns.std() # Calculating STD
std = np.array(std) # Convert to array

x = np.random.rand(pred_price_overDays, pred_count) # get random multidimensional array

Rv = std * norm.ppf(x) # Calculating Rv

print("The required Rv array is:\n", Rv)

e_value = np.exp(drift + Rv) # Calculating the E value

current_price = sys['Close'].iloc[-1] # Selecting last price of the year

new_prices = np.zeros_like(e_value) # create array to store the results

new_prices[0] = current_price

print(new_prices)

for i in range(1, pred_price_overDays): # Loop over all the days to find their prices
    new_prices[i] = new_prices[i - 1] * e_value[i] # Calculating the future price with formula

print("The Minimum Predicted Price:", new_prices[pred_price_overDays-1].min()) # Get minimum price
print("The Maximum Predicted Price:", new_prices[pred_price_overDays-1].max()) # Get maximum price

plt.xlabel('Days') # Assign name to x-axis
plt.ylabel('Price') # Assign name to y-axis
plt.title('Monte Carlo Analysis for Systems') # Assign name to the plot
plt.plot(new_prices)# plot the figure

print("\nThe price array:\n", new_prices)