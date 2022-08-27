# Top brands

import pandas as pd

df = pd.read_csv("2019-Oct.csv")
df['event_time'] = pd.to_datetime(df.event_time)

# Get rows where products are purchased
purchase = df[df['event_type'] == 'purchase']

# Group the DataFrame on brands
top_brands = purchase.groupby('brand')

# Get number of products bought by computing length of each grouped brand
top_brands = top_brands['brand'].agg([len])

# Sort the result on obtained length in descending order
top_brands.sort_values('len', ascending = False, inplace = True)

print(top_brands)

# Top categories

import pandas as pd

df = pd.read_csv("2019-Oct.csv")
df['event_time'] = pd.to_datetime(df.event_time)

# Get rows where products are purchased
purchase = df[df['event_type'] == 'purchase']

# Group the DataFrame on category_code
top_catg = purchase.groupby('category_code')

# Get number of products bought by computing length of each grouped category_code
top_catg = top_catg['category_code'].agg([len])

# Sort the result on obtained length in descending order
top_catg.sort_values('len', ascending = False, inplace = True)

print(top_catg)


