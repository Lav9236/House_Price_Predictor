# 🏡 HousePriceAI – AI Powered House Price Prediction System

An end-to-end Machine Learning web application that predicts house prices using a Stacking Regressor model. The project provides a modern Flask-based web interface where users can enter house details and receive an instant price prediction along with model evaluation metrics and dataset insights.

---

# 📌 Project Overview

HousePriceAI is an AI-powered web application developed using Python, Flask, and Machine Learning. The application predicts the estimated selling price of a house based on important property features such as area, construction year, quality, garage capacity, basement size, and more.

The project combines multiple regression algorithms using Ensemble Learning (Stacking Regressor) to improve prediction performance and accuracy.

---

# 🚀 Features

- Modern Responsive Flask Web Application
- AI Powered House Price Prediction
- Ensemble Learning (Stacking Regressor)
- Interactive Prediction Dashboard
- Model Evaluation Dashboard
- Feature Importance Visualization
- Actual vs Predicted Price Visualization
- Error Distribution Analysis
- Dataset Overview Page
- About Project Page
- Responsive UI using Bootstrap 5
- Clean Folder Structure
- Professional Project Architecture

---

# 🧠 Machine Learning Pipeline

Dataset

↓

Data Cleaning

↓

Missing Value Handling

↓

Feature Selection

↓

Train-Test Split

↓

Feature Scaling (StandardScaler)

↓

Model Training

• Linear Regression

• Random Forest Regressor

• XGBoost Regressor

↓

Stacking Regressor

↓

Model Evaluation

↓

Model Serialization (.pkl)

↓

Flask Deployment

---

# 🤖 Machine Learning Models Used

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
- Stacking Regressor (Final Model)

---

# 📊 Evaluation Metrics

The model is evaluated using:

- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score

The trained evaluation metrics are automatically stored in:

```
data/model_metrics.pkl
```

and displayed dynamically inside the Flask dashboard.

---

# 📁 Project Structure

```
HousePricePrediction/

│

├── app.py

├── train_model.py

├── Home_Price_Model.ipynb

├── requirements.txt

├── README.md

│

├── data/

│   ├── house_prices_practice.csv

│   ├── house_price_model.pkl

│   ├── scaler.pkl

│   ├── feature_names.pkl

│   └── model_metrics.pkl

│

├── static/

│   ├── css/

│   ├── js/

│   └── images/

│

├── templates/

│   ├── base.html

│   ├── home.html

│   ├── predict.html

│   ├── evaluation.html

│   ├── dataset.html

│   ├── about.html

│   └── 404.html
```

---

# ⚙️ Technologies Used

### Programming

- Python

### Machine Learning

- Scikit-Learn
- XGBoost

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Backend

- Flask

### Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap 5

### Model Serialization

- Joblib

---

# 📈 Model Workflow

1. Load Dataset
2. Clean Data
3. Handle Missing Values
4. Split Dataset
5. Standardize Features
6. Train Base Models
7. Train Stacking Regressor
8. Evaluate Performance
9. Save Model
10. Deploy Using Flask

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/your-username/HousePricePrediction.git
```

Move into project folder

```bash
cd HousePricePrediction
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

Add screenshots of:

- Home Page
- Prediction Page
- Evaluation Dashboard
- Dataset Page
- About Page

---

# 🌟 Future Improvements

- Deep Learning Model
- Model Explainability (SHAP)
- Cloud Deployment
- User Authentication
- Prediction History
- Export Prediction as PDF
- REST API Support

---

# 👨‍💻 Author

**Lavakush Gond**

AI & Machine Learning Enthusiast

Python | Flask | Machine Learning | Data Science

---

