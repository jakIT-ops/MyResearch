# 1. Introduction

### A. XGBoost vs. scikit-learn

The previous 3 sections of this course used scikit-learn for a variety of tasks. In this section, we cover XGBoost, a state-of-the-art data science library for performing classification and regression. XGBoost makes use of gradient boosted decision trees, which provides better performance than regular decision trees.

In addition to the performance boost, XGBoost implements an extremely efficient version of gradient boosted trees. The XGBoost models train much faster than scikit-learn models, while still providing the same ease of use.

For data science and machine learning competitions that use small to medium sized datasets (e.g. Kaggle), XGBoost is always among the top performing models.

### Gradient boosted trees

The problem with regular decision trees is that they are often not complex enough to capture the intricacies of many large datasets. We could continuously increase the maximum depth of a decision tree to fit larger datasets, but decision trees with many nodes tend to overfit the data.

Instead, we make use of gradient boosting to combine many decision trees into a single model for classification or regression. Gradient boosting starts off with a single decision tree, then iteratively adds more decision trees to the overall model to correct the model's errors on the training dataset.

The XGBoost API handles the gradient boosting process for us, which produces a much better model than if we had used a single decision tree.

# 2. XGBoost Basics

### A. Basic data structures

```py
data = np.array([
  [1.2, 3.3, 1.4],
  [5.1, 2.2, 6.6]])

import xgboost as xgb
dmat1 = xgb.DMatrix(data)

labels = np.array([0, 1])
dmat2 = xgb.DMatrix(data, label=labels)
```

### B. Using a <code>Booster</code>

```py
# predefined evaluation data and labels
print('Data shape: {}'.format(eval_data.shape))
print('Labels shape: {}'.format(eval_labels.shape))
deval = xgb.DMatrix(eval_data, label=eval_labels)

# Trained bst from previous code
print(bst.eval(deval))  # evaluation

# new_data contains 2 new data observations
dpred = xgb.DMatrix(new_data)
# predictions represents probabilities
predictions = bst.predict(dpred)
print('{}\n'.format(predictions))
```

# 3. Cross-Validation

### A. Choosing parameters

```py
# predefined data and labels
dtrain = xgb.DMatrix(data, label=labels)
params = {
  'max_depth': 2,
  'lambda': 1.5,
  'objective':'binary:logistic',
  'eval_metric':'logloss'

}
cv_results = xgb.cv(params, dtrain)
print('CV Results:\n{}'.format(cv_results))
```

# 4. Storing Boosters

### A. Saving and loading binary data

```py
# predefined data and labels
dtrain = xgb.DMatrix(data, label=labels)
params = {
  'max_depth': 3,
  'objective':'binary:logistic',
  'eval_metric':'logloss'
}
bst = xgb.train(params, dtrain)

# 2 new data observations
dpred = xgb.DMatrix(new_data)
print('Probabilities:\n{}'.format(
  repr(bst.predict(dpred))))

bst.save_model('model.bin')
```

# 4. XGBoost Classifier

### A. Following the scikit-learn API

While XGBoost provides a more efficient model than scikit-learn, using the model can be a bit convoluted. For people who are used to scikit-learn, XGBoost provides wrapper APIs around its model for classification and regression. These wrapper APIs allow us to use XGBoost's efficient model in the same style as scikit-learn.

```py
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
# predefined data and labels
model.fit(data, labels)

# new_data contains 2 new data observations
predictions = model.predict(new_data)
print('Predictions:\n{}'.format(repr(predictions)))
```

# 5. XGBoost Regressor

### A. XGBoost linear regression

```py
model = xgb.XGBRegressor(max_depth=2)
# predefined data and labels (for regression)
model.fit(data, labels)

# new_data contains 2 new data observations
predictions = model.predict(new_data)
print('Predictions:\n{}'.format(repr(predictions)))
```

# 6. Feature Importance

### A. Determining important features

```py
model = xgb.XGBClassifier(objective='multi:softmax', eval_metric='mlogloss', use_label_encoder=False)
# predefined data and labels
model.fit(data, labels)

# Array of feature importances
print('Feature importances:\n{}'.format(
  repr(model.feature_importances_)))
```

### B. Plotting important features

```py
model = xgb.XGBRegressor()
# predefined data and labels (for regression)
model.fit(data, labels)

xgb.plot_importance(model)
plt.show() # matplotlib plot
```

# 7. Hyperparameter Tuning

### A. Using scikit-learn's <code>GridSearchCV</code>

```py
model = xgb.XGBClassifier(objective='binary:logistic', eval_metric='logloss', use_label_encoder=False)
params = {'max_depth': range(2, 5)}

from sklearn.model_selection import GridSearchCV
cv_model = GridSearchCV(model, params, cv=4)

# predefined data and labels
cv_model.fit(data, labels)
print('Best max_depth: {}\n'.format(
  cv_model.best_params_['max_depth']))

# new_data contains 2 new data observations
print('Predictions:\n{}'.format(
  repr(cv_model.predict(new_data))))
```





















