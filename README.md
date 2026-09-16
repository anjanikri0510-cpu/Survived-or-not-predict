# 🚢 Titanic Survival Prediction

A **Machine Learning project** that predicts whether a passenger would **Survive or Not Survive** the Titanic disaster based on passenger information such as class, age, gender, family members, fare, and port of embarkation.

The project uses **Logistic Regression** and is deployed using **Streamlit**.

---

## 🌐 Live Demo

👉 **Streamlit App:** [Click here to try the Titanic Survival Prediction App](YOUR_STREAMLIT_APP_LINK)

---

## 📌 Project Overview

The main objective of this project is to build a machine learning model that predicts the survival status of a Titanic passenger.

The user enters passenger details in the Streamlit application, and the trained model predicts:

* 🟢 **Survived**
* 🔴 **Not Survived**

---

## 🧠 Machine Learning Algorithm

**Logistic Regression**

Logistic Regression is a classification algorithm used to predict one of two possible outcomes.

In this project:

* `0` → Not Survived
* `1` → Survived

---

## 📊 Features Used

The model uses the following passenger information:

| Feature     | Description                       |
| ----------- | --------------------------------- |
| Pclass      | Passenger class                   |
| Age         | Passenger's age                   |
| SibSp       | Number of siblings/spouses aboard |
| Parch       | Number of parents/children aboard |
| Fare        | Passenger fare                    |
| Sex_encoded | Encoded gender                    |
| S           | Southampton                       |
| C           | Cherbourg                         |
| Q           | Queenstown                        |

### Sex Encoding

The application shows the user:

* Male
* Female

The gender is converted internally into the numerical format required by the machine learning model.

---

## 🔄 Project Workflow

```text
Titanic Dataset
      ↓
Data Cleaning
      ↓
Feature Selection
      ↓
Data Encoding
      ↓
Train-Test Split
      ↓
Logistic Regression
      ↓
Pipeline
      ↓
Model Prediction
      ↓
Streamlit Web App
```

---

## 🛠️ Technologies Used

* 🐍 Python
* 🧮 Pandas
* 🔢 NumPy
* 🤖 Scikit-learn
* 🎨 Streamlit
* 📓 Jupyter Notebook
* 💻 GitHub

---

## 📁 Project Files

```text
Survived-or-not-predict/
│
├── app (2).py
├── cleandata1.ipynb
├── survived_pipeline.pkl
├── requirements.txt
└── README.md
```

### `app (2).py`

Contains the Streamlit application used to take passenger details and display the prediction.

### `cleandata1.ipynb`

Contains the data cleaning, preprocessing, model training, and machine learning workflow.

### `survived_pipeline.pkl`

Contains the trained machine learning pipeline used for prediction.

### `requirements.txt`

Contains the Python libraries required to run the project.

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/anjanikri0510-cpu/Survived-or-not-predict.git
```

### 2. Open the project folder

```bash
cd Survived-or-not-predict
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run "app (2).py"
```

### 5. Open the local URL

Streamlit will provide a local URL in the terminal. Open it in your browser.

---

## 🎯 Prediction

The application takes passenger details as input and uses the trained Logistic Regression pipeline to predict the passenger's survival status.

### Example

```text
Passenger Details
       ↓
Model
       ↓
Prediction
       ↓
Survived / Not Survived
```

---

## 📚 Learning Outcomes

Through this project, I learned about:

* Data cleaning
* Feature selection
* Categorical data encoding
* Train-test splitting
* Logistic Regression
* Machine Learning pipelines
* Model prediction
* Saving a trained model using Pickle
* Building a Streamlit application
* Deploying a Machine Learning project

---

## 👩‍💻 Author

**Anjani Kumari**

BCA Student
Interested in Data Analytics & Machine Learning

---

## ⭐ Project

If you find this project useful, feel free to ⭐ the repository.
