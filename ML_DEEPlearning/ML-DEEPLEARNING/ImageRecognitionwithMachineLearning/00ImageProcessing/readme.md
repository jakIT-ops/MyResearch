# Introduction

In this section you will learn about image processing with TensorFlow and PIL. Before doing any image-related tasks, we need to convert the images into a usable form for deep learning models. TensorFlow and PIL provide us utilities that make image processing very straightforward.

## A. Image recognition

Computer vision, the field concerning machines being able to understand images and videos, is one of the hottest topics in the tech industry. Robotics, self-driving cars, and facial recognition all rely on computer vision to work. At the core of computer vision is image recognition, the task of recognizing what an image represents.

Before performing any task related to images, it is almost always necessary to first process the images to make them more suitable as input data. This section of the course focuses on image processing, specifically how we can convert images from JPEG or PNG files to usable data for our neural networks.

## B. Core libraries

The two main libraries that will be used in this Lab for image processing are TensorFlow and PIL. TensorFlow provides a variety of utility functions to obtain image data from files, resize the images, and even transform a large set of images all at once. The original PIL (Python Imaging Library) is an image manipulation library built for Python. Although its development stopped in 2011, an offshoot called Pillow was created and continues to be developed to provide better image manipulation tools for Python users. We'll use the [Pillow](https://python-pillow.org/) version of PIL for more fine-grain image processing.

# 1. Image Files

### A. Image data

Before we do any image processing, we need to understand how image files work. Specifically, we'll discuss how these files use byte data and pixels to represent images.

### B. Pixels

So what exactly is a pixel? A pixel is essentially just a point on an image, with a specific shade, color, and/or opacity. We normally represent a pixel as a single integer or multiple integers. Pixels take a specific form based on the interpretation of the image, which is usually one of the following:

* Grayscale: Viewing the image as shades of black and white. Each pixel is an integer between 0-255, where 0 is completely black and 255 is completely white.

* RGB: The default interpretation for color images. Each pixel is made up of 3 integers between 0-255, where the integers represent the intensity of red, green, and blue, respectively, for the pixel.

* RGBA: An extension of RGB with an added alpha field. The alpha field represents the opacity of an image, and in this Lab we'll represent a pixel's alpha value as an integer from 0-255 with 0 being fully transparent and 255 being fully opaque.

```py
import tensorflow as tf
# Decode image data from a file in Tensorflow
def decode_image(filename, image_type, resize_shape, channels=0):
    value = tf.io.read_file(filename)
```

# 2. Image Types

## A. Decoding

We'll now decode the raw byte data into usable pixel data. The decoding function that we use depends on the format of the image. If the input is a PNG image then we use [tf.io.decode_png](https://www.tensorflow.org/api_docs/python/tf/io/decode_png), and if the input is a JPEG image we use [tf.io.decode_jpeg](https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg). For generic decoding (i.e. decoding any image format), we use [tf.io.decode_image](https://www.tensorflow.org/api_docs/python/tf/io/decode_image).

Since `tf.io.decode_image` can decode any type of image, you might be wondering why we even bother with the other two decoding functions. One reason is that you may want to only use specific image formats, in which case it's more efficient and better for code clarity to just use the format-specific decoding function.

Another reason is that `tf.io.decode_image` supports GIF decoding, which results in an output shape of (`num_frames`, height, width, channels). Since the function can return data with different shapes, we can't use `tf.io.decode_image` when we also need to resize the image with `tf.image.resize` (see next chapter).

## B. Channels

In the previous chapter we discussed image interpretations. If we only pass in value as the required argument for one of the decoding functions, we're using the interpretation specified in the raw image data. Normally it's fine to do this, but sometimes we want to use a specific format for the pixels.

We can change the pixel format of the decoded image via the channels keyword argument.

```py
import tensorflow as tf
value = tf.io.read_file('image3.jpg')
with tf.compat.v1.Session() as sess:
    arr = sess.run(tf.io.decode_jpeg(value, channels=1))
    print(arr.shape)
    print(repr(arr))
```

In this chapter we'll continue to work on the decode_image function from the previous chapter. The previous chapter's code is already filled in the function.

We decode value based on the image type. There are two image types, PNG and JPEG, that we will specifically check for.

```py
import tensorflow as tf

# Decode image data from a file in Tensorflow
def decode_image(filename, image_type, resize_shape, channels=0):
    value = tf.io.read_file(filename)
    if image_type == 'png':
        decoded_image = tf.io.decode_png(value, channels=channels)
    elif image_type == 'jpeg':
        decoded_image = tf.io.decode_jpeg(value, channels=channels)
    else:
        decoded_image = tf.io.decode_image(value, channels=channels)
```


# 3. Resizing

## A. Basic resizing

The function we use for resizing pixel data is [tf.image.resize](https://www.tensorflow.org/api_docs/python/tf/image/resize). It takes in two required arguments: the original image's decoded data and the new size of the image, which is a tuple/list of two integers representing new_height and new_width, in that order.

```py
import tensorflow as tf

with tf.compat.v1.Session() as sess:
    print('Original: {}'.format(
        repr(sess.run(decoded_image))))  # Decoded image data
    resized_img = tf.image.resize(decoded_image, (3, 2))
    print('Resized: {}'.format(
        repr(sess.run(resized_img))))
```

## B. Resizing methods

The TensorFlow tf.image.resize function allows us to specify a keyword argument called method. The method argument represents the image scaling algorithm. There are 4 possible values for method:

* tf.image.ResizeMethod.BILINEAR

* tf.image.ResizeMethod.NEAREST_NEIGHBOR

* tf.image.ResizeMethod.BICUBIC

* tf.image.ResizeMethod.AREA


## C. Unknown type

As mentioned in the previous chapter, a benefit to using tf.io.decode_image is when we don't know the type of input image (e.g. PNG vs. JPEG). However, we can't use tf.image.resize if the decoding function was tf.io.decode_image. This is because the input data for tf.image.resize needs to have a known number of dimensions, but the output of tf.io.decode_image can have 3 or 4 dimensions depending on the image type.

```py
import tensorflow as tf
sess = tf.compat.v1.Session()
print('Original: {}'.format(
    repr(sess.run(decoded_image))))  # Decoded image data
resized_img = tf.image.resize_with_crop_or_pad(decoded_image, 5, 2)
print('Resized: {}'.format(
    repr(sess.run(resized_img))))
```


## Time to Code

```py
import tensorflow as tf

# Decode image data from a file in Tensorflow
def decode_image(filename, image_type, resize_shape, channels=0):
    value = tf.io.read_file(filename)
    if image_type == 'png':
        decoded_image = tf.io.decode_png(value, channels=channels)
    elif image_type == 'jpeg':
        decoded_image = tf.io.decode_jpeg(value, channels=channels)
    else:
        decoded_image = tf.io.decode_image(value, channels=channels)
    if resize_shape is not None and image_type in ['png', 'jpeg']:
        decoded_image = tf.image.resize(decoded_image, resize_shape)
    return decoded_image
```

# 4. Dataset

## A. Image dataset

Normally when we do image related tasks we're dealing with a large amount of image data. In this case, it's best to use a TensorFlow dataset, i.e. tf.data.Dataset, to store all the images. We can create a dataset using the from_tensor_slices function.

The Dataset class makes it easier and more efficient to perform tasks with all the image files. If you want to learn more about using TensorFlow's tf.data API, check out the Industry Case Study course on Educative.

## B. Mapping

After we create a dataset with the image files, we will need to decode each file’s contents into usable pixel data. Since the decode_image function works for single image files, we will need to use the dataset object's map function to apply decode_image to each image file in our dataset.

The output of the map function is a new dataset with each element now converted from the original image file to its corresponding pixel data. We use map rather than using a for loop to manually convert each image file because map does the image decoding in parallel across the files, making it a more efficient solution.

```py
import tensorflow as tf

image_paths = ['img1.jpg', 'img2.jpg']
dataset = tf.data.Dataset.from_tensor_slices(image_paths)
def _map_fn(filename):
    # FUNCTION FROM PREVIOUS CHAPTERS
    return decode_image(...)
map_dataset = dataset.map(_map_fn)
```

# 5. Iterator

## A. Using Iterator

The way we can extract the decoded image data from our Dataset is through a tf.data.Iterator. For a more in-depth look at tf.data.Iterator, check out the Industry Case Study course on Educative.

We use the get_next function to obtain a next-element tensor, which is used for data extraction. Note that the next-element tensor doesn't have an actual value until we execute the iteration process using tf.compat.v1.Session (see next chapter).

```py
import tensorflow as tf

def get_image_data(image_paths, image_type=None, resize_shape=None, channels=0):
    dataset = get_dataset(image_paths, image_type, resize_shape, channels)
    iterator = tf.compat.v1.data.make_one_shot_iterator(dataset)
    next_image = iterator.get_next()
```

# 6. Execution

## A. Data iteration

In the previous chapter we set up a next-element tensor using the get_next function. The way we actually execute the data extraction is by using the run function of tf.compat.v1.Session.

Each time we use sess.run(next_image), we are iterating a single step through our dataset. So the first time we use sess.run(next_image), it’ll return the first pixel array in dataset (as a NumPy array), and the i^{th}
i
th

 time it’ll return the i^{th}
i
th

 pixel array in dataset.

```py
 it = tf.compat.v1.data.make_one_shot_iterator(dataset)
 next_image = it.get_next()
 sess = tf.compat.v1.Session()
 for i in range(3):
     sess.run(next_image)
```

## B. Using data

Rather than going through the decoding process every time we use a dataset of image files, it is usually better to just decode once and save the NumPy pixel data in a file. This can be done with the numpy.save function.

The code below shows examples of using numpy.save. The file itself is not human-readable, but can be loaded back into a NumPy array with numpy.load.

```py
import numpy as np

arr = np.array([1, 2, 3])
# Saves to 'arr.npy'
np.save('arr.npy', arr)
# Also saves to 'arr.npy'
np.save('arr', arr)
# Loading from that file
arr_copy = np.load('arr.npy')
print(repr(arr_copy))
```

# 7. PIL Library

## A. PIL module

While we can do large scale image processing in TensorFlow, the PIL module (from Pillow) allows us to do more fine-grained image processing. In this Lab we will demonstrate basic resizing and filtering as an introduction to PIL. However, the library also has many more utility functions for advanced image processing and analysis. Documentation and extended examples using the PIL module can be found [here](https://pillow.readthedocs.io/en/stable/reference/index.html).

The PIL module has a submodule called Image, which is the main module used for image processing. With it, we can create an Image object from an image file and obtain the image’s pixel data. The nice thing about PIL is that the methods are more user-friendly than the TensorFlow methods; for example, the file reading and decoding are done together and resizing can work with unknown image formats.

The image_mode variable refers to the interpretation of the pixels, e.g. Grayscale vs. RGB vs. RGBA. PIL provides us with many types of [modes](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes).

We’ll use image_mode to convert our image into RGBA format so that we can resize it without worrying about what format it’s in.

## B. Image modification

Similar to TensorFlow, the Image module allows us to resize our image. Also like TensorFlow, the Image module’s resizing function takes in an optional resizing method, which the PIL documentation refers to as resampling filters. Detailed descriptions, as well as a scaling quality and performance comparison for each resampling filter can be found [here](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-filters). In the code at the end of this chapter, we will use the Lanczos resampling filter for the best quality resizing.

PIL also allows us to apply filtering to an image, which is provided via the ImageFilter submodule. The ImageFilter module has a substantial list of predefined filters, as well as some more advanced filter classes.

Filtering allows us to perform tasks such as sharpening or blurring an image’s features. Filters like these are actually the crux of image recognition, and they’re discussed in more detail in the CNN section of this course.


```py
import numpy as np
from PIL import Image, ImageFilter

# Load and resize an image using PIL, and return its pixel data
def pil_resize_image(image_path, resize_shape,
    image_mode='RGBA', image_filter=None):
    im = Image.open(image_path)
    converted_im = im.convert(image_mode)
    resized_im = converted_im.resize(resize_shape, Image.LANCZOS)
    if image_filter is not None:
        resized_im = resized_im.filter(image_filter)
    return np.asarray(resized_im.getdata())
```
