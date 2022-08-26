from keras.models import Sequential, load_model
import cv2
from PIL import Image
from matplotlib import pyplot as plt

# reload the model
model = load_model("output/mnist.h5")

# read the input
img_array = cv2.imread('__ed_input.png', cv2.IMREAD_GRAYSCALE)
plt.imshow(img_array, cmap = plt.cm.binary)
plt.show()
plt.savefig("output/image.png")

# convert input to gray scale
img_array = cv2.bitwise_not(img_array)
plt.imshow(img_array, cmap = plt.cm.binary)
plt.show()
plt.savefig("output/grayscale_image.png")

# resize the image
img_size = 28
new_array = cv2.resize(img_array, (img_size, img_size), interpolation = cv2.INTER_AREA)
plt.imshow(new_array, cmap = plt.cm.binary)
plt.show()
plt.savefig("output/resized_image.png")

# resize the vector to size (1, 784)
mynumber = new_array.reshape(1, 784)
# normalize the feature array
mynumber = mynumber/255

# predict the label
predictions = model.predict(mynumber)
print("Predictions:", predictions)
preds = [np.argmax(pred) for pred in predictions]
# print the predicted label
print("Predicted label:", preds)
