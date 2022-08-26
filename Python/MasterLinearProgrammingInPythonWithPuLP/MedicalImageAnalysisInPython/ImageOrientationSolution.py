import seaborn as sns
from matplotlib import pyplot as plt
basic_palette = sns.color_palette("pastel")
plt.style.use('seaborn-whitegrid')
pa = 61
ap =39
plt.pie([pa, ap], labels = ["PA", "AP"], colors=[basic_palette[-2],basic_palette[4]], autopct='%1.1f%%', startangle=70)
plt.title("Orientation", fontsize=16)
plt.savefig("output/graph.png")
