import pandas as pd

df = pd.read_csv("2019-Oct.csv") # Reading the data from file




# Step 1

# Fetch rows with brand
with_brand = df[df['brand'].notna()]

# Fetch rows without brand
without_brand = df[df['brand'].isna()]

# Step 2

# Purchased products with brands
with_brand = with_brand[with_brand['event_type'] == 'purchase']
print(with_brand)

# Purchased products without brands
without_brand = without_brand[without_brand['event_type'] == 'purchase']
print(without_brand)

# Get length of original dataframe with purchased products
org = len(df[df['event_type'] == 'purchase'])

# Divide the length of with_brand dataframe with length org dataframe
brand_p = len(with_brand) / org
print(brand_p * 100)

# Divide the length of without_brand dataframe with length org dataframe
brand_a = len(without_brand) / org
print(brand_a * 100)
