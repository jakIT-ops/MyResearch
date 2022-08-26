from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.layers import *
from tensorflow.python.keras.models import *
print('Imported Successfully!')

# Create the model architecture
model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation="relu",input_shape=(224,224,3)))
model.add(Conv2D(64, kernel_size=(3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(128, kernel_size=(3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(64, activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam",metrics = ["accuracy"])
model.summary()

# Processing the images
train_datagen = image.ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = image.ImageDataGenerator(rescale = 1./255)

print('Created the Data Generator Objects.')

# Load the dataset
train_generator = train_datagen.flow_from_directory('CovidDataset/Train',target_size=(224,224),batch_size=32, class_mode="binary")
val_generator = test_datagen.flow_from_directory('CovidDataset/Val',target_size=(224,224),batch_size=32, class_mode="binary")

# Train the model
hist = model.fit(train_generator, epochs = 6, validation_data=val_generator, validation_steps=2)
