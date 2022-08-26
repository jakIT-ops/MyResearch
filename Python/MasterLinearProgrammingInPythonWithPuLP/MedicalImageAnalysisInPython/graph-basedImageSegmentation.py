# Importing the required libraries
import numpy as np
import pydicom
from matplotlib import pyplot as plt
from skimage.exposure import equalize_hist
from skimage.filters.rank import median
from skimage.morphology import disk
from skimage.segmentation import felzenszwalb
from skimage.transform import rescale
example = 'stage_2_images/ID_01fe90211.dcm'
imagedata= pydicom.dcmread(example)

im_thres = imagedata.pixel_array.copy()
im_thres[im_thres > 65] = 0

im_small = rescale(im_thres, 0.5)
im_small_filt = median(im_small, disk(50))
im_small_filt = equalize_hist(im_small_filt)

segments = felzenszwalb(im_small_filt, scale=0.5)
f = plt.figure(figsize=(12,12))
ax = f.add_subplot(121)
ax2 = f.add_subplot(122)
ax.imshow(imagedata.pixel_array, cmap=plt.cm.bone)
ax2.imshow(segments, cmap=plt.cm.bone)
