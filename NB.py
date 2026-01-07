import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

def gaussian_pdf(x, mean, var):
    exponent = np.exp(-((mean - x)**2)/( 2 * var))
    return ( 1/ np.sqrt(2 * np.pi * var)) * exponent


def train_naive_bayes(X, y):
    classes = np.unique(y)
    mean = {}
    var = {}
    prior = {}
    for c in classes:
        X_c = X[y == c]
        mean[c] = np.mean(X_c, axis=0)
        var[c] = np.var(X_c, axis=0) + 1e-9
        prior[c] = X_c.shape[0] / X.shape[0]
    return mean, var, prior

def predict(X, mean, var, prior):
    predictions = []
    for x in X:
        posteriors = []
        for c in prior:
            likelihood = np.sum(np.log(gaussian_pdf(x, mean[c], var[c])))
            posterior = np.log(prior[c]) + likelihood
            posteriors.append(posterior)
        predictions.append(np.argmax(posteriors))
        
    return np.array(predictions)
            



data = pd.read_csv('Breastcancer_data.csv')

ids = data["id"].values

data = data.drop("id", axis=1)

data["diagnosis"] = data["diagnosis"].map({"M":1, "B": 0})

X = data.drop("diagnosis", axis=1).values
y = data["diagnosis"].values

X_train, X_test, y_train, y_test, id_train, id_test = train_test_split(
    X, y, ids, test_size=0.1, random_state=42
)

mean, var, prior = train_naive_bayes(X_train, y_train)
y_pred = predict(X_test, mean, var, prior)

print(" Actual vs Predicted: ")
for i in range(len(y_test)):
    actual = "M" if y_test[i] == 1 else "B"
    predicted = "M" if y_pred[i] == 1 else "B"
    print(f"ID: {id_test[i]} | Actual: {actual} | Predicted: {predicted}")
    
print("\n Confusion Matrix: ")
print(confusion_matrix(y_test, y_pred))

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
