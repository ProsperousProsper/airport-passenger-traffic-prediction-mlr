# ✈️ Multiple Linear Regression Model for Airport Passenger Traffic Prediction

---

## 1. Project Overview

**Title:**  
Development of a Multiple Linear Regression Model for Predicting Monthly Passenger Traffic at Major Airports

**Aim:**  
To develop a mathematical and computational model using Multiple Linear Regression to predict the monthly number of airline passengers at a major airport based on operational and economic factors.

**Objectives:**  

- Generate a realistic dataset of airport operations  
- Identify key factors affecting passenger traffic  
- Develop a regression model  
- Evaluate the model’s performance  
- Interpret the regression coefficients  

**Importance of the Study:**  

This model assists:  

- **Airport authorities** → terminal planning, staffing, security scheduling  
- **Airlines** → flight scheduling, demand forecasting  
- **Aviation regulators** → infrastructure development  

---

## 2. Dataset Description

**Dataset Size:** 504 samples (monthly records over 42 years)

**Dataset Source:**  
The dataset is synthetically generated to realistically reflect international airport passenger patterns, based on ICAO reports, airline operational statistics, and real-world aviation trends.

---

## 3. Feature and Target Definition

### Input Features (Independent Variables)

| Symbol | Feature | Description | Unit |
|--------|---------|-------------|------|
| x1 | Flights_per_Month | Number of scheduled flights per month | flights |
| x2 | Ticket_Price_Index | Average airfare cost index | relative |
| x3 | Seasonal_Demand_Index | Travel season intensity | scale (2–10) |

### Target Variable (Dependent Variable)

| Symbol | Feature | Description | Unit |
|--------|---------|-------------|------|
| y | Monthly_Passengers | Total passengers boarding per month | persons |

---

## 4. Mathematical Model Formulation

The Multiple Linear Regression model is given by:

\[
y = b_0 + b_1 x_1 + b_2 x_2 + b_3 x_3
\]

Where:  

- \(b_0\) = intercept  
- \(b_1, b_2, b_3\) = regression coefficients  

---

## 5. Dataset Splitting

- **Training set:** 80% → 403 samples  
- **Testing set:** 20% → 101 samples  

\[
X_{train} = 0.8 \times 504, \quad X_{test} = 0.2 \times 504
\]

---

## 6. Model Training

The model was trained using **scikit-learn LinearRegression()**.  

**Training Inputs:**  

\[
X = [Flights\_per\_Month, Ticket\_Price\_Index, Seasonal\_Demand\_Index]
\]

**Target:**  

\[
y = Monthly\_Passengers
\]

---

## 7. Regression Equation (Final Model)

**Coefficients from trained model:**

| Parameter | Value |
|-----------|-------|
| b1 (Flights) | 119.43 |
| b2 (Ticket Index) | -9473.01 |
| b3 (Season Index) | 14959.50 |
| b0 (Intercept) | 8785.40 |

**Final Regression Equation:**

\[
Passengers = 8785 + 119.43(Flights) - 9473(TicketIndex) + 14959(SeasonIndex)
\]

---

## 8. Prediction Stage

The trained model predicts passenger counts for unseen test data:

\[
\hat{y} = f(X_{test})
\]

These predictions are compared against real values to compute error metrics.

---

## 9. Model Evaluation

| Metric | Value |
|--------|-------|
| R² Score | 0.848 |
| Mean Squared Error (MSE) | 3.66 × 10⁸ |

**Interpretation:**  

- R² = 0.848 → 84.8% prediction accuracy  
- The model explains 84.8% of variability in monthly passenger traffic  
- This is considered strong performance for real-world regression models  

---

## 10. Interpretation of Model Coefficients

1️⃣ **Flights_per_Month → +119.43**  
- Every additional flight increases passengers by ≈ 119 people  
- Meaning: More flights → higher passenger traffic  

2️⃣ **Ticket_Price_Index → −9473**  
- Every unit increase reduces passengers by ≈ 9,473  
- Meaning: Higher airfare → fewer travelers → reduced traffic  

3️⃣ **Seasonal_Demand_Index → +14,959**  
- Every unit rise increases passengers by ≈ 15,000  
- Meaning: Holidays, festivals, summer → massive passenger increase  

---

## 👨‍🎓 Student Information

| Field | Details |
|-------|---------|
| Name | Soetan Prosper Okikijesu |
| Department | Computer Science |
| Matric Number | 240805027 |
| Course Code | COS 201 |
