from keras.layers import Dense
from keras.models import Sequential
import pandas as pd
from matplotlib import pyplot as plt
# read dataset using pandas as dataframe
data = pd.read_csv("sonar.csv")

# assign R to 1 and 0 to M
def assign_label_integer(row):
	if row["R"] == 'R':
		return 1
	else:
		return 0

# seperate features and label
## features
train_X = data.drop(["R"], axis = 1)
# make the last column as integer
data["R"] = data.apply(assign_label_integer, axis = 1)

## label
train_y = data["R"]

# get number of columns in training data
n_cols = train_X.shape[1]

# model for a binary classification to predict
model = Sequential()
# first hidden layer
model.add(Dense(30, activation='relu', input_shape=(n_cols,)))
# second hidden layer
model.add(Dense(60, activation='relu'))
# output layer
model.add(Dense(1, activation='sigmoid'))

# compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(train_X, train_y, epochs = 20, batch_size = 10)

# Evaluate the keras model
_, accuracy = model.evaluate(train_X, train_y)
print('Accuracy: %.2f' % (accuracy * 100))
