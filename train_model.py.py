
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
data = pd.read_csv("dataset/airport_passenger_data.csv")

X = data[["Flights_per_Month", "Ticket_Price_Index", "Seasonal_Demand_Index"]]
y = data["Monthly_Passengers"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("R2 Score:", r2)
print("Mean Squared Error:", mse)
print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
