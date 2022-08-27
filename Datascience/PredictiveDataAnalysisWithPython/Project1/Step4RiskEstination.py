import numpy as np
from scipy import stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sys = pd.read_csv('data/Year_2018/SYS.csv')
ns = pd.read_csv('data/Year_2018/NETSOL.csv')
ptc = pd.read_csv('data/Year_2018/PTC.csv')
avn = pd.read_csv('data/Year_2018/AVN.csv') 

sys['Time'] = pd.to_datetime(sys.Time)
ns['Time'] = pd.to_datetime(ns.Time)
ptc['Time'] = pd.to_datetime(ptc.Time)
avn['Time'] = pd.to_datetime(avn.Time)

sys = sys.set_index('Time')
ns = ns.set_index('Time')
ptc = ptc.set_index('Time')
avn = avn.set_index('Time')


df = pd.DataFrame({'SYS': sys['Close'], 
                   'NETSOL': ns['Close'], 
                   'PTC': ptc['Close'], 
                   'AVN': avn['Close']})

all_returns = df.pct_change()

ret = all_returns.dropna()

avg_daily_return = ret.mean()
daily_risk = ret.std()

plt.xlabel("Daily Average Expected Return")
plt.ylabel("Daily Risk")

plt.xlim(ret.mean().min() + ret.mean().min()*2, ret.mean().max() + ret.mean().max()*2)

for label, x, y in zip(ret.columns, ret.mean(), ret.std()):
    plt.annotate(
        label,
        xy = (x,y), xytext = (50, 50),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        arrowprops = dict(arrowstyle = '<-', connectionstyle = 'arc3,rad=-0.4'))

plt.grid()

plt.scatter(avg_daily_return, daily_risk, s = 30)

# Quantiles
investment = 100000

loss = (abs(all_returns.quantile(0.1))) * investment
print(loss)