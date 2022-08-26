from tensorflow.python.keras.applications.resnet50 import ResNet50
from tensorflow.python.keras.optimizers import Adam
from tensorflow.python.keras.layers import *
from tensorflow.python.keras.models import Model
import numpy as np
print("Imported Successfully!")

# Load the ResNet50 model
model = ResNet50(include_top = False, weights = 'imagenet', input_shape = (224,224,3))
print(model.summary())

# Building our classifier
av1 = GlobalAveragePooling2D()(model.output)

fc1 = Dense(256, activation = 'relu')(av1)

d1 = Dropout(0.5)(fc1)

fc2 = Dense(10, activation = 'softmax')(d1)


# Perform the feature extractor strategy
model_new = Model(inputs = model.input, outputs = fc2)
model_new.summary()

# Make predictions
from keras.applications.resnet50 import preprocess_input

image_path = 'pikachu.png'
img = image.load_img(image_path,target_size = (224,224))
x = image.img_to_array(img)
x = np.expand_dims(x,axis=0)
x = preprocess_input(x)

pred = model_new.predict(x)
print(np.argmax(pred))

# Compile the new model
adam = Adam(lr = 0.00003)
model_new.compile(loss = 'categorical_crossentropy', optimizer = adam, metrics = ['accuracy'])

# Fine-tune the new model
for ix in range(len(model_new.layers)):
    print(ix, model_new.layers[ix])

# Train the model
hist = model_new.fit(X_train, Y_train, shuffle = True, batch_size = 16, epochs = 8, validation_split = 0.20)
