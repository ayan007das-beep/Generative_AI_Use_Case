import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate synthetic sales data
np.random.seed(42)
months = np.arange(1, 25)
sales = 100 + months * 5 + np.random.normal(0, 10, 24)

df = pd.DataFrame({"month": months, "sales": sales})

# Train ML model
model = LinearRegression()
model.fit(df[["month"]], df["sales"])

# Predict next 6 months
future_months = np.arange(25, 31).reshape(-1, 1)
predictions = model.predict(future_months)

plt.figure()
plt.plot(df["month"], df["sales"])
plt.plot(future_months, predictions)
plt.title("Sales Forecast")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()