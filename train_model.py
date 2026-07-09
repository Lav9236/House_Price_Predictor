import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, StackingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# os.makedirs("images", exist_ok=True)
# Load dataset
data = pd.read_csv('data/house_prices_practice.csv')

# Remove unnecessary column
data = data.drop('Id', axis=1)

# Handle missing values
num_cols = data.select_dtypes(include='number').columns
data[num_cols] = data[num_cols].fillna(data[num_cols].mean())

# Features and target
X = data.drop('SalePrice', axis=1)
y = data['SalePrice']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
# ---------------------------
# Individual Models
# ---------------------------

# Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)

# Random Forest Regressor
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

# XGBoost Regressor
xgb_model = XGBRegressor(
    objective='reg:squarederror',
    max_depth=5,
    n_estimators=100,
    random_state=42
)
xgb_model.fit(X_train, y_train)
y_pred_xgb = xgb_model.predict(X_test)

# ---------------------------
# Stacking Regressor
# ---------------------------

base_models = [
    ('lr', LinearRegression()),
    ('rf', rf_model),
    ('xgb', xgb_model)
]

stack_model = StackingRegressor(
    estimators=base_models,
    final_estimator=LinearRegression()
)

stack_model.fit(X_train, y_train)

y_pred_stack = stack_model.predict(X_test)


# ---------------------------
# Evaluation Function
# ---------------------------

def evaluate_model(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    # print(f"RMSE : {rmse:.2f}")
    # print(f"MAE  : {mae:.2f}")
    # print(f"R²   : {r2:.4f}")
    # print("-" * 40)

    return {
        "RMSE": round(rmse, 2),
        "MAE": round(mae, 2),
        "R2": round(r2, 4)
    }


# print("Linear Regression")
lr_metrics = evaluate_model(y_test, y_pred_lr)

# print("Random Forest Regressor")
rf_metrics = evaluate_model(y_test, y_pred_rf)

# print("XGBoost Regressor")
xgb_metrics = evaluate_model(y_test, y_pred_xgb)

# print("Stacking Regressor")
stack_metrics = evaluate_model(y_test, y_pred_stack)

# save evaluation metrics

evaluation_metrics = {

    "Linear Regression": lr_metrics,

    "Random Forest": rf_metrics,

    "XGBoost": xgb_metrics,

    "Stacking Regressor": stack_metrics

}

joblib.dump(
    evaluation_metrics,
    "data/model_metrics.pkl"
)

# ---------------------------
# Save Model Files
# ---------------------------

feature_names = X.columns.tolist()

joblib.dump(stack_model, "data/house_price_model.pkl")
joblib.dump(scaler, "data/scaler.pkl")
joblib.dump(feature_names, "data/feature_names.pkl")

# Input feature
# try:
#     user_data = {}
#
#     for feature in feature_names:
#         value = float(input(f"Enter {feature}: "))
#         user_data[feature] = value
#
#     # dataframe
#     input_df = pd.DataFrame([user_data])
#     input_scaled = scaler.transform(input_df)
#     prediction = stack_model.predict(input_scaled)
#     print("Predicted House Price:", prediction[0])
# except Exception as e:
#     print("An error occured: ", e)

# ---------------------------
# Feature Importance Plot
# ---------------------------

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': np.abs(lr_model.coef_)
}).sort_values(
    by='Importance',
    ascending=False
)

# Feature Importance Plot save
plt.figure(figsize=(8, 5))

sns.barplot(
    x='Importance',
    y='Feature',
    data=importance_df
)

plt.title("Feature Importance")
plt.tight_layout()

plt.savefig(
    "static/images/feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# Scatter Plot Graph
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred_stack)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red",
    linewidth=2
)
plt.savefig(
    "static/images/actual_vs_predicted.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# Error Distribution Graph
error = abs(y_test - y_pred_stack)
plt.figure(figsize=(6, 6))
plt.hist(error, bins=20)
plt.title("Prediction Error Distribution")
plt.xlabel("Absolute Error")
plt.ylabel("Frequency")
plt.savefig(
    "static/images/error_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()
