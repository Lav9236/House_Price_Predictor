from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import time
import joblib
import os

# ==================================================
# Create Flask Application
# ==================================================

app = Flask(__name__)

# ==================================================
# Paths
# ==================================================

DATA_FOLDER = "data"

MODEL_PATH = os.path.join(DATA_FOLDER, "house_price_model.pkl")
SCALER_PATH = os.path.join(DATA_FOLDER, "scaler.pkl")
FEATURE_PATH = os.path.join(DATA_FOLDER, "feature_names.pkl")
METRICS_PATH = os.path.join(DATA_FOLDER, "model_metrics.pkl")

# ==================================================
# Load Machine Learning Files
# (Only once when Flask starts)
# ==================================================

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    feature_names = joblib.load(FEATURE_PATH)
    metrics = joblib.load(METRICS_PATH)

    print("✅ Model Loaded Successfully")
    print("✅ Scaler Loaded Successfully")
    print("✅ Feature Names Loaded Successfully")
    print("✅ Metrics Loaded Successfully")

except Exception as e:

    print("❌ Error Loading Files")
    print(e)

    model = None
    scaler = None
    feature_names = None
    metrics = None


# ==================================================
# Home Page
# ==================================================

@app.route("/")
def home():
    return render_template(
        "home.html",
        metrics=metrics,
        active_page="home"
    )


# ==================================================
# Prediction Page
# ==================================================

@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    prediction_time = None
    prediction_quality = None
    prediction_confidence = None
    prediction_status = "Ready"

    if request.method == "POST":

        try:

            start_time = time.time()

            input_data = {}

            for feature in feature_names:
                input_data[feature] = float(request.form[feature])

            input_df = pd.DataFrame([input_data])

            input_scaled = scaler.transform(input_df)

            prediction = model.predict(input_scaled)[0]

            prediction = round(prediction, 2)

            # Estimated Confidence

            r2 = metrics["Stacking Regressor"]["R2"]

            prediction_confidence = round(r2 * 100, 2)

            end_time = time.time()

            prediction_time = round(end_time - start_time, 4)

            prediction_status = "Success"

            # Prediction Quality
            # (Temporary Logic)

            if prediction_confidence >= 95:
                prediction_quality = "Excellent"

            elif prediction_confidence >= 90:
                prediction_quality = "Very Good"

            elif prediction_confidence >= 80:
                prediction_quality = "Good"

            else:
                prediction_quality = "Average"

        except Exception as e:

            prediction_status = "Failed"

            prediction_quality = "Not Available"

            print(e)

    return render_template(
        "predict.html",
        prediction=prediction,
        prediction_time=prediction_time,
        prediction_quality=prediction_quality,
        prediction_status=prediction_status,
        prediction_confidence=prediction_confidence,
        active_page="predict"
    )


# ==================================================
# Model Evaluation Page
# ==================================================

@app.route("/evaluation")
def evaluation():
    return render_template(
        "evaluation.html",
        metrics=metrics,
        active_page="evaluation"
    )


# ==================================================
# About Page
# ==================================================

@app.route("/about")
def about():
    return render_template(
        "about.html",
        active_page="about"
    )


# ==================================================
# Dataset Page
# ==================================================

@app.route("/dataset")
def dataset():
    df = pd.read_csv("data/house_prices_practice.csv")

    dataset_info = {

        "rows": df.shape[0],

        "columns": df.shape[1],

        "missing": int(df.isnull().sum().sum()),

        "target": "SalePrice",

        "features": len(df.columns) - 1

    }

    preview = df.head(10).to_dict(orient="records")

    columns = df.columns.tolist()

    summary = df.describe().round(2).to_dict()

    return render_template(

        "dataset.html",
        dataset_info=dataset_info,
        preview=preview,
        columns=columns,
        summary=summary,
        active_page="dataset"

    )


# ==================================================
# Run Flask
# ==================================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )


# ===========================================
# 404 Error
# ===========================================

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
