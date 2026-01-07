import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

def distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


def KNN(X_train, y_train, X_test, k):
    predictions = []
    for x_test in X_test:
        distances = []
        for i in range(len(X_train)):
            dist = distance(x_test, X_train[i])
            distances.append((dist, y_train[i]))
        distances.sort(key=lambda x: x[0])
        k_nearest = distances[:k]
        
        labels = [label for _, label in k_nearest]
        prediction = max(set(labels), key=labels.count)
        predictions.append(prediction)
    return np.array(predictions)

data = pd.read_csv("Breastcancer_data.csv")
ids = data["id"].values
data = data.drop("id", axis=1)

data["diagnosis"] = data["diagnosis"].map({"M": 1, "B": 0})

X = data.drop("diagnosis", axis=1).values
y = data["diagnosis"].values

X_train, X_test, y_train, y_test, id_train, id_test = train_test_split(
    X, y, ids, test_size=0.1, random_state=42
)

k = 5
y_pred = KNN(X_train, y_train, X_test, k)


print("\nTest Results (KNN):")
for i in range(len(y_test)):
    actual = "M" if y_test[i] == 1 else "B"
    predicted = "M" if y_pred[i] == 1 else "B"
    print(f"ID: {id_test[i]} | Actual: {actual} | Predicted: {predicted}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
print("F1 Score:", f1_score(y_test, y_pred, zero_division=0))
