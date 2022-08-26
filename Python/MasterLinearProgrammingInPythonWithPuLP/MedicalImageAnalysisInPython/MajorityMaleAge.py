from glob import glob
import pandas as pd
import seaborn as sns
import pydicom
import numpy as np
from matplotlib import pyplot as plt
data = sorted(glob("stage_2_images/*.dcm"))
patients = []
for t in data:
    data = pydicom.dcmread(t)
    patient = {}
    patient["Age"] = data.PatientAge
    patient["Sex"] = data.PatientSex
    patients.append(patient)
df_patients = pd.DataFrame(patients, columns=["Age", "Sex"])
df_patients["Age"] = pd.to_numeric(df_patients["Age"])
df_patients["Age"] = pd.to_numeric(df_patients[df_patients['Sex']=='M']["Age"])
sorted_ages = np.sort(df_patients["Age"].values)

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(15, 5))
plt.hist(sorted_ages[:-2], bins=[i for i in range(100)])
plt.title("distribution by age", fontsize=18, pad=10)
plt.xlabel("age", labelpad=10)
plt.xticks([i*10 for i in range(11)])
plt.ylabel("count of male patients", labelpad=10)
plt.show()
plt.savefig("output/graph.png")
