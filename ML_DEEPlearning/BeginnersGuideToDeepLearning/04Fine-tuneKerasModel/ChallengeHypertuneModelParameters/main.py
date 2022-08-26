import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

# read in training data
train_data = pd.read_csv("train.csv")

# preprocess training data
train_X = train_data.drop(["PassengerId", "Name", "Cabin", "Embarked", "Ticket", "Fare", "Survived"], axis=1)


# assign an integer value of gender
def assign_gender_integer(row):
	if row['Gender'] == 'male':
		return 1
	else:
		return 0

# call the assign_gender_integer method to assign 1 to male and 0 to female
train_X['Gender'] = train_data.apply(assign_gender_integer, axis=1)
train_X.fillna(0, inplace=True)
train_X.head()

train_y = train_data["Survived"]


# get number of columns in training data
n_cols = train_X.shape[1]

# model for a binary classification to predict survival
model = Sequential()
# add a hidden layer with 32 nodes
model.add(Dense(60, activation='relu', input_shape=(n_cols,)))
# add a hidden layer with 64 nodes
model.add(Dense(60, activation='relu'))
# add dropout
model.add(Dropout(0.5))
# add the output layer with the sigmoid activation function
model.add(Dense(1, activation='sigmoid'))

# compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Define early_stopping_monitor
early_stopping_monitor = EarlyStopping(patience=2)

# fit the model
history = model.fit(train_X, train_y, validation_split = 0.3, epochs=100, batch_size=5, callbacks = [early_stopping_monitor], verbose=0)

# plot epoch vs. accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()
plt.savefig('output/legend.png')

_, accuracy = model.evaluate(train_X, train_y)
print('Training Accuracy: %.2f' % (accuracy * 100))

"--------------------------"
# read the test data
test_data = pd.read_csv("test.csv")

# Preprocess data
test_data.fillna(0, inplace=True)
# seperate features and label
test_y = test_data["Survived"]

# drop unncessary features
test_X = test_data.drop(["PassengerId", "Name", "Cabin", "Embarked", "Ticket", "Fare", "Survived"], axis=1)

# assign integer value to
test_X['Gender'] = test_data.apply(assign_gender_integer, axis=1)


# predict the output
predictions = model.predict(test_X)

_, accuracy = model.evaluate(test_X, test_y)
print('Testing Accuracy: %.2f' % (accuracy * 100))
