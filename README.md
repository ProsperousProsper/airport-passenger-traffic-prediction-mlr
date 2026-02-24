# Create README.md locally
readme_content = """
# ✈️ Airport Passenger Traffic Prediction Using Multiple Linear Regression

---

## 📌 Project Overview

This project focuses on predicting **monthly passenger traffic at airports** using a **Multiple Linear Regression (MLR) model**. The model uses operational and economic factors such as:

- Number of scheduled flights per month  
- Ticket price index  
- Seasonal demand index  

The aim is to provide **accurate forecasts** for airline scheduling, airport infrastructure planning, and passenger demand analysis.

---

## 🎯 Objectives

- Build a predictive model for airport passenger traffic  
- Evaluate the impact of key factors (flights, ticket prices, seasonal demand)  
- Analyze model coefficients to understand feature importance  
- Provide actionable insights for airport planning  

---

## 📊 Dataset Description

The dataset is **synthetically generated** and contains **504 records**, representing monthly airport operations.  

| Feature | Description |
|---------|-------------|
| Flights_per_Month | Number of flights scheduled per month |
| Ticket_Price_Index | Index representing average ticket price |
| Seasonal_Demand_Index | Index representing seasonal travel demand |
| Monthly_Passengers | Total passengers in the month (Target variable) |

---

## 🔍 Features and Target

### Input Features (Independent Variables)

X = [Flights_per_Month, Ticket_Price_Index, Seasonal_Demand_Index]

### Target Variable (Dependent Variable)

y = Monthly_Passengers

---

## 🧮 Mathematical Model Formulation

The project uses **Multiple Linear Regression**:

y = β0 + β1 * Flights_per_Month + β2 * Ticket_Price_Index + β3 * Seasonal_Demand_Index + ε

Where:  

- y = Predicted monthly passengers  
- β0 = Intercept  
- β1, β2, β3 = Feature coefficients  
- ε = Error term  

---

## 🔄 Data Splitting

The dataset is split as follows:

- 80% Training Data  
- 20% Testing Data  

---

## 🧠 Model Training

- Algorithm: Linear Regression  
- Input Features: Flights_per_Month, Ticket_Price_Index, Seasonal_Demand_Index  
- Target: Monthly_Passengers  

---

## 🔮 Prediction Stage

Once trained, the model predicts **monthly passengers** given new input values.

Example:

```python
# Predict passengers
model.predict([[850, 7.2, 6.5]])
## 👨‍🎓 Student Information

| Field | Details |
|-------|---------|
| Name | Soetan Prosper Okikijesu |
| Department | Computer Science |
| Matric Number | 240805027 |
| Course Code | COS 201 |