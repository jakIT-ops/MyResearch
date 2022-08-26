### Problem statement

The sonar data for this challenge is taken from [UCI](https://archive.ics.uci.edu/ml/datasets/Connectionist+Bench+(Sonar,+Mines+vs.+Rocks)) Repository of datasets. Train a network to distinguish between sonar signals bouncing off of a metal cylinder and those bouncing off of a roughly cylindrical rock.

Each bouncing signal pattern is a set of 60 numbers between 0.0 and 1.0. Each number represents the energy within a particular frequency band that is integrated over a certain period of time. The label associated with each record contains the letter “R” if the object is a rock and “M” if it is a mine (metal cylinder).

Train the model with the configuration provided below:

* The model architecture should have 2 hidden layers with 30 and 60 nodes respectively and an output layer. The activation function of the hidden layers should be relu. The activation function of the output layer should be sigmoid.

* The model should be compiled with adam as an optimizer, loss as binary_crossentropy, and metrics=['accuracy'].

* The model should fit on the training data with 20 epochs and 10 batch size. Store the result in the history variable.

* Evaluate the model on the training data and store the loss and accuracy.


### Sample input

> 📝 Note: The data is already read and the features and labels are separated in train_X and train_y respectively.

* Line 5: Reads the dataset sonar.csv using the read_csv function of the pandas data frame.

* Line 9: Reads the features in train_X.

* Line 24: Reads the labels in train_y.

### Sample output

The trained model accuracy after defining the model architecture, the compile method, the fit method, and the evaluate model.
