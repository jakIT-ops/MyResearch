### Problem statement

The IRIS data set is taken from the [UCI](https://archive.ics.uci.edu/ml/datasets/iris) repository of datasets. It has four features and a label that classifies the flower.

### Initialization parameters

The following table summarizes the initialization parameters:


|Variables	| Definition |
| :---------| -----------: |
| dataset	| Reads the value in the pandas dataframe using the csv_read method |
| X     |	Reads the first 4 columns of the dataset |
| Y	    | Reads the last column and then converts value to 0 if the label is Iris-setosa and 1 otherwise using np.where |
| weights |	The weights array of size 1 * 4 initialized with 0 |
| bias	| The bias of size 1 * 1 initialized with 0.0 |


#### Sample input

The train function takes in parameters, input X, target labels Y, weights, and bias.

#### Sample output

The predicted labels:

```py
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
```
