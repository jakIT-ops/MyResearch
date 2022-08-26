# 1. Medical Imaging Exploration

### Introduction to medical imaging

The first X-ray image appeared in 1895, and it has become an integral part of clinical care. By 2021, the United States alone had created more than three and a half billion terabytes of medical images. This opens up enormous opportunities for image analysis, including those listed below:

* Predict pathology using neural networks.

* Measure the shape and size of organs.

* Create 3D reconstructions.

### Formats of medical images#

**Digital Imaging and Communications in Medicine **(DICOM), developed by the NEMA, allows us a number of facilities, including:

* Creation

* Storing

* Sending

* Printing

We can employ these functions for not only a single image but a series of images along with other information like patient information, research, equipment, facilities, important inspection data, and so on.

The DICOM Standard defines two informational levels, as noted below.

1. At file level, a DICOM file object is a file with tags. These tags contain information about the organization to represent the image frame (or series of frames) and accompanying control information.

2. At the network (communication) level, DICOM network protocols transfer DICOM files and control commands across networks with TCP and IP support.

## Standards of file layer

The file layer of the 2008 DICOM 3.0 Standard describes the following:

* Patient attributes and demographics.
* Model upon which the survey is carried out and name of the device’s manufacturer.
* Attributes of the medical institution where the survey is carried out.
* Attributes of those who examined the patient.
* Type of examination and time of its conduct.
* Conditions and parameters of the patient’s examination.
* Parameters of an image or a series of images recorded in a DICOM file.
* Unique identification keys or Unique Identifier (UID), of data groups described in the DICOM file.
* Image, series, or set of series obtained during the examination of the patient.
* Presentation of PDF documents in a DICOM file.
* Representation of DICOM recording using optical media, including DVD format.
* DICOM protocol for transmission and reception of medical images over TCP and IP.

# Loading and Visualization

### Data and format

In this course, we’ll use open-source data. We’ll use the X-ray dataset for pneumothorax segmentation in the DICOM format. For the NIfTI-1 Data Format, we’ll use the CT dataset for liver cancer segmentation. This course does not require you to download the dataset to your computer. However, if you want to save it to your computer, see the course’s appendix.

### DICOM
To work with DICOM files, we’ll use the pydicom library. We import all the libraries necessary for the work. After importing the required libraries, we read the file using the dcmread(). Let’s take the file as an example to display the given X-ray image.

As a result, the image data variable is of type pydicom.dataset.FileDataset since it contains not only the snapshot but also the metadata. To access the image, we need to use the pixel_array attribute of the DICOM image. Render the image using Matplotlib and use plt.cm.bone as a color scheme to make the image look like an X-ray.

```py
import pydicom # library for working with DICOM files
from matplotlib import cm # color schemes for visualization
from matplotlib import pyplot as plt # library for visualization
example = 'stage_2_images/ID_01fe90211.dcm'
imagedata= pydicom.dcmread(example)
plt.figure(figsize=(12, 12))
plt.imshow(imagedata.pixel_array, cmap=plt.cm.bone)
plt.show()
```

### NIfTI-1

The NIfTI DFWG (Data Format Working Group) suggested NIfTI-1 as a short-term approach to enhance the interoperability of functional MRI data analysis software packages.

Let’s look at an example to understand this approach.

* First, we import all the libraries necessary for this work.

* Then, we read the file using load().

* We use get_fdata()to get an image.

* We work with the file volume_pt5/volume-44.nii. Turn the image 90
90
 degrees, and look at the shape of the file contents.
* The “depth” here means CT slices. We use imshow() to visualize 50
50
 and 118
118
 CT slices.

```py
import nibabel # library for working with NIfTI-1 Data Format
import numpy as np # numpy for image manipulation
from matplotlib import cm # color schemes for visualization
from matplotlib import pyplot as plt # library for visualization
filepath = 'volume_pt5/volume-44.nii'
imagedata=nibabel.load(filepath)
array = imagedata.get_fdata()
array = np.rot90(np.array(array))
print(array.shape)
f = plt.figure(figsize=(12,12))
ax = f.add_subplot(121)
ax2 = f.add_subplot(122)
ax.imshow(array[...,50].astype(np.float32), cmap=plt.cm.bone)
ax2.imshow(array[...,118].astype(np.float32), cmap=plt.cm.bone)
```

# Exploration of Metadata

| Attribute      | Description    |
| :------------- | :------------- |
| PatientID      | It contains the ID of the patient. |
| PatientAge     | It contains the age of the patient.|
| PatientSex     | It contains the gender of the patient. |
| Modality       | It contains the diagnosis technology. |
| BodyPart       | It contains the body part of the patient that is affected. |
| ViewPosition   |It contains an X-ray view of the image in relation to the orientation of the object.|

### The metadata of the DICOM file

```py
import pydicom # library for working with DICOM files
example = 'stage_2_images/ID_01fe90211.dcm'
imagedata= pydicom.dcmread(example)
print("ID:", imagedata.PatientID)
print("Age:", imagedata.PatientAge)
print("Sex:", imagedata.PatientSex)
print("Modality:", imagedata.Modality)
print("BodyPart:", imagedata.BodyPartExamined)
print("X-ray view of the image in relation to the orientation of the object:", imagedata.ViewPosition)
'''
ID:
Age: 26
Sex: F
Modality: CR
BodyPart: CHEST
X-ray view of the image in relation to the orientation of the object: PA
'''
```

Everything is clear with ID, Age, and Sex (F=Female, M=Male). Let’s explain Modality (CR=Computed Radiography). The main types (modalities) of medical images supported by the DICOM Standard are presented below:

* Computed Radiography (CR)

* Computed Tomography (CT)

* Digital Radiography (DX)

* Mammography (MG)

### Plotting to analyze metadata

Now let’s do a little data overview.

* We have all the patients’ data, such as ID, Age, Sex, Modality, BodyPart, ViewPosition.

* We’ll choose only the age of the patients to plot the histogram.

* We’ll count the number of patients of the same age on the x-axis and the age of the patients on the y-axis.

```py
import pydicom
import numpy as np
from matplotlib import pyplot as plt
from glob import glob
import pandas as pd
import seaborn as sns
data = sorted(glob("/content/drive/MyDrive/Colab Notebooks/stage_2_images/*.dcm")) # create a list containing paths to all files
# For the convenience of analysis, we will create a dataframe with metadata
patients = []
for t in data:
    data = pydicom.dcmread(t)
    patient = {}
    patient["UID"] = data.SOPInstanceUID
    patient["Age"] = data.PatientAge
    patient["Sex"] = data.PatientSex
    patient["Modality"] = data.Modality
    patient["BodyPart"] = data.BodyPartExamined
    patient["ViewPosition"] = data.ViewPosition
    patients.append(patient)
    df_patients = pd.DataFrame(patients, columns=["UID", "Age", "Sex", "Modality", "BodyPart", "ViewPosition"])
    df_patients["Age"] = pd.to_numeric(df_patients["Age"])
# Let's make a histogram
sorted_ages = np.sort(df_patients["Age"].values)
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(15, 5))
plt.hist(sorted_ages[:-2], bins=[i for i in range(100)])
plt.title("Distribution by age", fontsize=18, pad=10)
plt.xlabel("Age", labelpad=10)
plt.xticks([i*10 for i in range(11)])
plt.ylabel("Count", labelpad=10)
plt.show()
```

# Visualize the Windowing

### An image before and after windowed()

Let’s visualize the image before and after applying the windowed() function. In the code below, we can see the difference between the original image and the image after applying windowed().

```py
from matplotlib import pyplot as plt
import nibabel
import numpy as np
filepath = 'volume_pt5/volume-44.nii'
imagedata = nibabel.load(filepath)
array = imagedata.get_fdata()
array = np.rot90(np.array(array))
def windowed(px, w, l):
        px_min = l - w//2
        px_max = l + w//2
        px[px<px_min] = px_min
        px[px>px_max] = px_max
        return (px-px_min) / (px_max-px_min)
f = plt.figure(figsize=(12,12))
ax = f.add_subplot(121)
ax2 = f.add_subplot(122)
ax.imshow(array[...,50].astype(np.float32),cmap=plt.cm.bone)
ax.title.set_text('Original image')
ax2.imshow(windowed(array[...,50].astype(np.float32), 150,30), cmap=plt.cm.bone)
ax2.title.set_text('Windowing image')
```

### Other kinds of windowing

We reviewed the recommended window settings. Let’s look at a few lesser-known options. For example, we can mix windowing by performing the functions below.

* We’ll apply the rainbow_bsb_window() for other windowing options.

* IIn this function, we’ll adjust the width and level to get a colorful image.

* In the code below, we can see the difference between the original and the colorful image after applying rainbow_bsb_window().

```py
from matplotlib import pyplot as plt
import nibabel
import numpy as np
filepath = 'volume_pt5/volume-44.nii'
imagedata = nibabel.load(filepath)
array = imagedata.get_fdata()
array = np.rot90(np.array(array))
def windowed(px, w, l):
        px_min = l - w//2
        px_max = l + w//2
        px[px<px_min] = px_min
        px[px>px_max] = px_max
        return (px-px_min) / (px_max-px_min)
def rainbow_bsb_window(img):
        brain_img = windowed(img, 40, 80)
        subdural_img = windowed(img, 80, 200)
        bone_img = windowed(img, 600, 2000)
        combo = (brain_img*0.3 + subdural_img*0.5 + bone_img*0.2)
        return combo
f = plt.figure(figsize=(12,12))
ax = f.add_subplot(121)
ax2 = f.add_subplot(122)
ax.imshow(array[...,50].astype(np.float32), cmap=plt.cm.bone)
ax.title.set_text('Original image')
ax2.imshow(rainbow_bsb_window(array[...,50].astype(np.float32)))
ax2.title.set_text('Windowing image')
```
