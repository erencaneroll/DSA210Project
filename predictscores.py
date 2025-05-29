import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os

# --- Step 1: Load data ---
df = pd.read_csv("historical_player_data.csv")

# --- Step 2: Basic cleaning ---
df = df.dropna(subset=["Fantasy_Points", "Rebounds", "Assists", "Steals", "Blocks", "Turnovers"])

# Optional: Filter out extreme outliers (optional but can help model)
# df = df[df["Fantasy_Points"] < 100]

# --- Step 3: Feature selection ---
features = ["Rebounds", "Assists", "Steals", "Blocks", "Turnovers"]
X = df[features]
y = df["Fantasy_Points"]

# --- Step 4: Split the data ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Step 5: Train the model ---
reg = LinearRegression()
reg.fit(X_train, y_train)

# --- Step 6: Make predictions ---
y_pred = reg.predict(X_test)

# --- Step 7: Evaluate ---
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Evaluation:")
print(f"- Mean Squared Error: {mse:.2f}")
print(f"- R² Score: {r2:.4f}")

# --- Step 8: Plot predictions vs actual ---
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel("Actual Fantasy Points")
plt.ylabel("Predicted Fantasy Points")
plt.title("Actual vs Predicted Fantasy Points")
plt.tight_layout()

os.makedirs("figure", exist_ok=True)
plt.savefig("figure/regression_actual_vs_predicted.png")
plt.show()