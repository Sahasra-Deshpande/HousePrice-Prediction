import numpy as np
import joblib
import os
from sklearn.linear_model import LinearRegression

# Features:
# Area (sq ft), Bedrooms, Bathrooms, Age (years)

X = np.array([
    [500, 1, 1, 10],
    [600, 1, 1, 8],
    [800, 2, 1, 7],
    [900, 2, 2, 6],
    [1000, 2, 2, 5],
    [1200, 3, 2, 5],
    [1400, 3, 2, 4],
    [1600, 3, 3, 4],
    [1800, 3, 3, 3],
    [2000, 4, 3, 3],
    [2200, 4, 4, 2],
    [2500, 4, 4, 2],
    [3000, 5, 4, 1]
])

# Price in Lakhs
y = np.array([
    25,
    30,
    40,
    48,
    55,
    65,
    75,
    85,
    95,
    110,
    125,
    140,
    170
])

model = LinearRegression()

model.fit(X, y)

os.makedirs("model", exist_ok=True)

joblib.dump(
    model,
    "model/house_price_model.pkl"
)

print("Model trained successfully!")
print("Model saved as model/house_price_model.pkl")