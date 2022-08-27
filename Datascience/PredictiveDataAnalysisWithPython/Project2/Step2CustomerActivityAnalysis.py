import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("2019-Oct.csv") # Reading the data from file

#Convert the type of event_time column to datetime
df['event_time'] = pd.to_datetime(df.event_time)

df["week_day"] = df['event_time'].map(lambda x: x.dayofweek + 1)
df["day"] = df['event_time'].map(lambda x: x.day)
df["hour"] = df['event_time'].map(lambda x: x.hour)

# Get all the view events of all users
viewed = df[df['event_type'] == 'view']

# Plot the number views against all 24 hours of the days in a bar chart
view_plot = viewed.groupby('event_type')['hour'].value_counts().sort_index().plot(kind = 'bar', figsize = (15,6))

# Set properties of the plot
view_plot.set_xlabel('Hour',fontsize = 15)
view_plot.set_ylabel('Number of Views',fontsize = 15)
view_plot.set_title('Number of views for different Hours of Days',fontsize = 15)
view_plot.set_xticklabels(range(1,32), rotation='horizontal', fontsize=15)

#plot the graph
plt.show()
