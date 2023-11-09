import numpy as np
from scipy.stats import zscore

# Define the prior measurements
x = np.array(
    [
        1.40796533,
        0.29104673,
        1.74539197,
        -0.17648601,
        0.60321751,
        2.90038798,
        2.06495026,
        1.37243758,
        0.93980907,
        -0.04161072,
    ]
)

# Calculate the mean and standard deviation of the prior measurements
mean = np.mean(x)
std = np.std(x, ddof=1)

# Calculate the z-score of the new measurement
new_measurement = 10.0
z = (new_measurement - mean) / std

print("The z-score of the new measurement is:", z)
