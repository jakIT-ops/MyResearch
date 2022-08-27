import pandas as pd

df = pd.read_csv("2019-Oct.csv") # Reading the data from file

#Convert the type of event_time column to datetime
df['event_time'] = pd.to_datetime(df.event_time)

# Get rows with event_type equals purchase
purchased = df[df['event_type'] == 'purchase']

# Filter relevant data from Data Frame
purchased = purchased[['user_id', 'user_session', 'event_time' ,'price']]

print(purchased)

# Compute the R, F, and M values for each user
rfm = purchased.groupby('user_id').agg({'event_time': lambda date: ((purchased['event_time'].max()) - date.max()),
                                    'user_session': lambda num: num.count(),
                                    'price': lambda price: price.sum()})
print(rfm)


rfm['event_time'] = rfm['event_time'].apply(lambda days: int(str(days).split(' days')[0]) + 1)


rfm.columns=['recency','frequency','monetary']

print(rfm)

# Compute Ranks for Recency metric
def Compute_R(val,metric,quantile):
    if val <= quantile[metric][0.25]:
        return 1
    elif val <= quantile[metric][0.50]:
        return 2
    elif val <= quantile[metric][0.75]:
        return 3
    else:
        return 4

# Compute Ranks for Frequency & Monetary metrics
def Compute_FM(val,metric,quantile):
    if val <= quantile[metric][0.25]:
        return 4
    elif val <= quantile[metric][0.50]:
        return 3
    elif val <= quantile[metric][0.75]:
        return 2
    else:
        return 1

# Compute new column with recency rank of that row
rfm['R_rank'] = rfm_new['recency'].apply(Compute_R, args=('recency',quartiles))

# Compute new column with frequency rank of that row
rfm['F_rank'] = rfm_new['frequency'].apply(Compute_FM, args=('frequency',quartiles))

# Compute new column with monetary rank of that row
rfm['M_rank'] = rfm_new['monetary'].apply(Compute_FM, args=('monetary',quartiles))

print(rfm)

# Convert RFM values to type string
R = rfm.R_rank.astype(str)
F = rfm.F_rank.astype(str)
M = rfm.M_rank.astype(str)

# Compute new colum with combined RFM values
rfm['RFM_Score'] = R + F + M

print(rfm)

# Sort the DataFrame by RFM_Socre values
rfm = rfm.sort_values('RFM_Score')

print(rfm)


