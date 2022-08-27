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
print(all_returns)

corr = (all_returns.dropna()).corr()
sns.heatmap(corr, annot = True)

