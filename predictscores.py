import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os
import seaborn as sns

# --- Step 1: Load data ---
df = pd.read_csv("historical_player_data.csv")

# --- Step 2: Basic cleaning ---
df = df.dropna(subset=["Fantasy_Points", "3PM", "REB", "AST", "STL", "BLK", "TO", "PTS", "Position"])

# --- Step 3: Feature selection ---
stat_features = ["3PM", "REB", "AST", "STL", "BLK", "TO", "PTS"]
X = df[stat_features + ["Position"]]
y = df["Fantasy_Points"]

# --- Step 4: Encode Position as one-hot ---
X = pd.get_dummies(X, columns=["Position"])

# --- Step 5: Split the data ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Step 6: Train the model ---
reg = LinearRegression()
reg.fit(X_train, y_train)

# --- Step 7: Make predictions ---
y_pred = reg.predict(X_test)

# --- Step 8: Evaluate ---
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Evaluation:")
print(f"- Mean Squared Error: {mse:.2f}")
print(f"- R² Score: {r2:.4f}")

# --- Step 9: Analyze feature impact (coefficients) ---
# Create a DataFrame for the coefficients
coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": reg.coef_
}).sort_values(by="Coefficient", ascending=False)

# Print to console
print("\nFeature Impact (Regression Coefficients):")
print(coef_df)

# --- Step 10: Plot feature importance ---
plt.figure(figsize=(10, 6))
sns.barplot(x="Coefficient", y="Feature", data=coef_df, palette="coolwarm")
plt.title("Regression Coefficients: Impact on Fantasy Points")
plt.xlabel("Coefficient Value")
plt.ylabel("Feature")
plt.tight_layout()

# Save the plot
plt.savefig("figure/feature_importance_with_position.png")
plt.show()

# --- Step 9: Plot predictions vs actual ---
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel("Actual Fantasy Points")
plt.ylabel("Predicted Fantasy Points")
plt.title("Actual vs Predicted Fantasy Points (with Position)")
plt.tight_layout()

os.makedirs("figure", exist_ok=True)
plt.savefig("figure/regression_actual_vs_predicted_with_position.png")
plt.show()