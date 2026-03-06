# ❤️ Heart Disease Prediction using Machine Learning

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early detection can help doctors take preventive measures and improve patient outcomes.

This project uses **Machine Learning (Logistic Regression)** to predict whether a person has heart disease based on various medical attributes.

The dataset includes several health indicators such as age, cholesterol level, chest pain type, blood pressure, and heart rate.

---

## 🎯 Objective

The main objectives of this project are:

* Analyze heart disease dataset
* Perform exploratory data analysis (EDA)
* Handle outliers in the dataset
* Scale the features
* Train a machine learning model
* Predict heart disease presence
* Evaluate model performance

---

## 📂 Project Structure

```
Heart-Disease-Prediction
│
├── heart.csv        # Dataset
├── main.py          # Machine learning model code
├── README.md        # Project documentation
```

---

## 🧰 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 📊 Dataset Features

| Feature  | Description                              |
| -------- | ---------------------------------------- |
| age      | Age of the patient                       |
| sex      | Gender (1 = Male, 0 = Female)            |
| cp       | Chest pain type                          |
| trestbps | Resting blood pressure                   |
| chol     | Cholesterol level                        |
| fbs      | Fasting blood sugar                      |
| restecg  | Resting electrocardiographic results     |
| thalach  | Maximum heart rate achieved              |
| exang    | Exercise induced angina                  |
| oldpeak  | ST depression                            |
| slope    | Slope of peak exercise ST segment        |
| ca       | Number of major vessels                  |
| thal     | Thalassemia                              |
| target   | Heart disease presence (1 = Yes, 0 = No) |

---

## 🔄 Project Workflow

The machine learning pipeline followed in this project:

1. **Data Collection**

   * Load dataset using Pandas.

2. **Data Understanding**

   * Check dataset structure
   * Identify missing values
   * Analyze data types

3. **Exploratory Data Analysis (EDA)**

   * Feature distribution analysis
   * Correlation heatmap
   * Visualization of important features

4. **Data Preprocessing**

   * Outlier removal using IQR method
   * Feature and target separation

5. **Feature Scaling**

   * Standardize features using `StandardScaler`

6. **Train-Test Split**

   * Training data: 67%
   * Testing data: 33%

7. **Model Training**

   * Train **Logistic Regression** model

8. **Prediction**

   * Predict heart disease on test dataset

9. **Model Evaluation**

   * Accuracy Score
   * Classification Report
   * Precision, Recall, F1-score

---

## 📈 Machine Learning Flowchart

```
           +----------------------+
           |    Load Dataset      |
           |      (heart.csv)     |
           +----------+-----------+
                      |
                      v
           +----------------------+
           | Data Understanding   |
           | (EDA & Visualization)|
           +----------+-----------+
                      |
                      v
           +----------------------+
           |   Data Cleaning      |
           |  Outlier Removal     |
           +----------+-----------+
                      |
                      v
           +----------------------+
           |   Feature Scaling    |
           |   StandardScaler     |
           +----------+-----------+
                      |
                      v
           +----------------------+
           |  Train-Test Split    |
           +----------+-----------+
                      |
                      v
           +----------------------+
           |   Model Training     |
           | Logistic Regression  |
           +----------+-----------+
                      |
                      v
           +----------------------+
           |      Prediction      |
           +----------+-----------+
                      |
                      v
           +----------------------+
           |   Model Evaluation   |
           | Accuracy & Report    |
           +----------------------+
```

---

## 📈 Model Used

**Logistic Regression**

Logistic Regression is a supervised machine learning algorithm used for **binary classification problems**.
In this project, it predicts whether a patient **has heart disease or not**.

---

## 📊 Model Evaluation Metrics

The following metrics were used:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Classification Report

Example output:

```
Accuracy: 0.85
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/heart-disease-prediction.git
```

---

### 2️⃣ Install Required Libraries

```
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

### 3️⃣ Run the Python Script

```
python main.py
```

---

## 🚀 Future Improvements

* Add more ML models (Random Forest, SVM, XGBoost)
* Build a **Flask web application**
* Deploy the model on **AWS / Cloud**
* Add a **user interface for prediction**

---

## 👩‍💻 Author

**Reenamadhuri Vanga**

CSE Student | Machine Learning Beginner

---

## ⭐ Support

If you like this project, please **give it a star ⭐ on GitHub**.
