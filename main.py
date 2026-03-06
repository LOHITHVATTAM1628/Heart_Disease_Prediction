import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("heart.csv")

# Basic info
print(df.head())
print(df.shape)
print(df.isnull().sum())

# Correlation heatmap
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(), annot=True)
plt.show()

# Feature Target split
X = df.drop("target", axis=1)
y = df["target"]

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train test split
X_train,X_test,y_train,y_test = train_test_split(
    X_scaled,y,test_size=0.33,random_state=42
)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)

# Prediction
y_pred = model.predict(X_test)

# Results
print("Accuracy:",accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))