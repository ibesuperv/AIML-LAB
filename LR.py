import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

def sigmoid(z):
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))


def logistic(X, y, alpha, num_iterations):
    m, n = X.shape
    w = np.zeros(n)
    b = 0

    for _ in range(num_iterations):
        z = np.dot(X, w) + b
        a = sigmoid(z)

        dw = (1 / m) * np.dot(X.T, (a - y))
        db = (1 / m) * np.sum(a - y)

        w -= alpha * dw
        b -= alpha * db

    return w, b


def predict(X, w, b):
    z = np.dot(X, w) + b
    return np.where(sigmoid(z) >= 0.5, 1, 0)


data = pd.read_csv("Breastcancer_data.csv")

ids = data["id"].values

data = data.drop("id", axis=1)

data["diagnosis"] = data["diagnosis"].map({"M": 1, "B": 0})


X = data.drop("diagnosis", axis=1).values
y = data["diagnosis"].values


X_train, X_test, y_train, y_test, id_train, id_test = train_test_split(
    X, y, ids, test_size=3, random_state=42
)


w, b = logistic(X_train, y_train, alpha=0.01, num_iterations=1000)

y_pred = predict(X_test, w, b)

print("\nTest Results")
for i in range(len(y_test)):
    actual = "M" if y_test[i] == 1 else "B"
    predicted = "M" if y_pred[i] == 1 else "B"
    print(f"ID: {id_test[i]} | Actual: {actual} | Predicted: {predicted}")


print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
print("F1 Score:", f1_score(y_test, y_pred, zero_division=0))



z_vals = np.linspace(-10, 10, 200)
plt.plot(z_vals, sigmoid(z_vals))
plt.xlabel("z = w·x + b")
plt.ylabel("Probability")
plt.title("Sigmoid Function (Logistic Regression)")
plt.show()
