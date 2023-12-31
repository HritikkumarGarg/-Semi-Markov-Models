# -*- coding: utf-8 -*-
"""Semi Markov.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10kXOEqBT2Z3hceN3Ahr2IDhhPi_OA75E
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your dataset from a CSV file
# Assuming the CSV file has columns named 'DATE' and 'Value'
file_path = 'Electric_Production.csv'
df = pd.read_csv(file_path, parse_dates=['DATE'], dayfirst=True)  # Parse 'DATE' column as datetime
df = df.sort_values(by='DATE')  # Ensure the data is sorted by date
data = df['Value'].values

# Function to detect change-points using a Semi-Markov Model
def detect_change_points(data, num_regimes=3, num_samples=1000):
    # Initialize regime lengths and emission parameters (mean and std)
    regime_lengths = np.random.randint(low=50, high=200, size=num_regimes)
    regime_params = []
    for _ in range(num_regimes):
        regime_params.append((np.random.uniform(low=-5, high=5), np.random.uniform(low=1, high=3)))

    # Sampling regime lengths using a prior distribution
    sampled_lengths = np.random.choice(regime_lengths, size=num_samples)

    # Initialize variables for change-points and regime assignments
    change_points = [0]
    regime_assignments = [0]

    # Generate change-points based on sampled regime lengths
    for length in sampled_lengths:
        next_change_point = change_points[-1] + length
        if next_change_point < len(data):
            change_points.append(next_change_point)
            regime_assignments.extend([i % num_regimes for i in range(length)])

    # Generate synthetic data based on regime assignments and emission parameters
    synthetic_data = np.array([np.random.normal(loc=regime_params[i][0], scale=regime_params[i][1]) for i in regime_assignments])

    return synthetic_data, change_points, regime_assignments

# Detect change-points using the Semi-Markov Model
synthetic_data, change_points, regime_assignments = detect_change_points(data, num_regimes=3)

# Plot the original data and the synthetic data with change-points
plt.figure(figsize=(12, 6))
plt.plot(df['DATE'], data, label='Original Data', color='blue')
plt.scatter(df['DATE'].iloc[change_points[:-1]], synthetic_data[change_points[:-1]], color='red', marker='x', label='Change Points')
plt.title('Change-Point Detection using Semi-Markov Model')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load your dataset from a CSV file
# Assuming the CSV file has columns named 'DATE' and 'Value'
file_path = 'Electric_Production.csv'
df = pd.read_csv(file_path, parse_dates=['DATE'], dayfirst=True)  # Parse 'DATE' column as datetime
df = df.sort_values(by='DATE')  # Ensure the data is sorted by date
data = df['Value'].values

# Function to detect change-points using a Semi-Markov Model
def detect_change_points(data, num_regimes=3, num_samples=1000):
    # Initialize regime lengths and emission parameters (mean and std)
    regime_lengths = np.random.randint(low=50, high=200, size=num_regimes)
    regime_params = []
    for _ in range(num_regimes):
        regime_params.append((np.random.uniform(low=-5, high=5), np.random.uniform(low=1, high=3)))

    # Sampling regime lengths using a prior distribution
    sampled_lengths = np.random.choice(regime_lengths, size=num_samples)

    # Initialize variables for change-points and regime assignments
    change_points = [0]
    regime_assignments = [0]

    # Generate change-points based on sampled regime lengths
    for length in sampled_lengths:
        next_change_point = change_points[-1] + length
        if next_change_point < len(data):
            change_points.append(next_change_point)
            regime_assignments.extend([i % num_regimes for i in range(length)])

    # Generate synthetic data based on regime assignments and emission parameters
    synthetic_data = np.array([np.random.normal(loc=regime_params[i][0], scale=regime_params[i][1]) for i in regime_assignments])

    return synthetic_data, change_points, regime_assignments

# Detect change-points using the Semi-Markov Model
synthetic_data, change_points, regime_assignments = detect_change_points(data, num_regimes=3)

# Plot the original data and the synthetic data with change-points
plt.figure(figsize=(12, 6))
plt.plot(df['DATE'], data, label='Original Data', color='blue')
plt.scatter(df['DATE'].iloc[change_points[:-1]], synthetic_data[change_points[:-1]], color='red', marker='x', label='Change Points')
plt.title('Change-Point Detection using Semi-Markov Model')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# Calculate and plot the posterior distribution of change points
posterior_distributions = []

for i in range(1, len(change_points)):
    segment_data = synthetic_data[change_points[i-1]:change_points[i]]
    posterior_mean, posterior_std = norm.fit(segment_data)
    posterior_distributions.append((change_points[i], posterior_mean, posterior_std))

# Plot posterior distributions at change points
plt.figure(figsize=(12, 6))
for cp, mean, std in posterior_distributions:
    x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
    y = norm.pdf(x, loc=mean, scale=std)
    plt.plot(x, y, label=f'Posterior at Change Point {cp}')

plt.title('Posterior Distributions at Change Points')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load your dataset from a CSV file
# Assuming the CSV file has columns named 'DATE' and 'Value'
file_path = 'AAPL.csv'
df = pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)  # Parse 'DATE' column as datetime
df = df.sort_values(by='Date')  # Ensure the data is sorted by date
data = df['Open'].values

# Function to detect change-points using a Semi-Markov Model
def detect_change_points(data, num_regimes=3, num_samples=1000):
    # Initialize regime lengths and emission parameters (mean and std)
    regime_lengths = np.random.randint(low=50, high=200, size=num_regimes)
    regime_params = []
    for _ in range(num_regimes):
        regime_params.append((np.random.uniform(low=-5, high=5), np.random.uniform(low=1, high=3)))

    # Sampling regime lengths using a prior distribution
    sampled_lengths = np.random.choice(regime_lengths, size=num_samples)

    # Initialize variables for change-points and regime assignments
    change_points = [0]
    regime_assignments = [0]

    # Generate change-points based on sampled regime lengths
    for length in sampled_lengths:
        next_change_point = change_points[-1] + length
        if next_change_point < len(data):
            change_points.append(next_change_point)
            regime_assignments.extend([i % num_regimes for i in range(length)])

    # Generate synthetic data based on regime assignments and emission parameters
    synthetic_data = np.array([np.random.normal(loc=regime_params[i][0], scale=regime_params[i][1]) for i in regime_assignments])

    return synthetic_data, change_points, regime_assignments, regime_params

# Detect change-points using the Semi-Markov Model
synthetic_data, change_points, regime_assignments, regime_params = detect_change_points(data, num_regimes=3)

# Plot the original data and the synthetic data with change-points
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], data, label='Original Data', color='blue')
plt.scatter(df['Date'].iloc[change_points[:-1]], synthetic_data[change_points[:-1]], color='red', marker='x', label='Change Points')
plt.title('Change-Point Detection using Semi-Markov Model')
plt.xlabel('Date')
plt.ylabel('Open')
plt.legend()
plt.show()

# Collect posterior distributions at change points
posterior_distributions = []
for i, cp in enumerate(change_points[1:]):
    segment_data = synthetic_data[change_points[i]:cp]
    posterior_distributions.append((cp, *norm.fit(segment_data)))

# Plot posterior distributions at change points
plt.figure(figsize=(12, 6))
for cp, mean, std in posterior_distributions:
    x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
    y = norm.pdf(x, loc=mean, scale=std)
    plt.plot(x, y, label=f'Posterior at Change Point {cp}')

plt.title('Posterior Distributions at Change Points')
plt.xlabel('Open')
plt.ylabel('Density')
plt.legend()
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load your dataset from a CSV file
# Assuming the CSV file has columns named 'DATE' and 'Value'
file_path = 'DailyDelhiClimateTrain.csv'
df = pd.read_csv(file_path, parse_dates=['date'], dayfirst=True)  # Parse 'DATE' column as datetime
df = df.sort_values(by='date')  # Ensure the data is sorted by date
data = df['meantemp'].values

# Function to detect change-points using a Semi-Markov Model
def detect_change_points(data, num_regimes=3, num_samples=1000):
    # Initialize regime lengths and emission parameters (mean and std)
    regime_lengths = np.random.randint(low=50, high=200, size=num_regimes)
    regime_params = []
    for _ in range(num_regimes):
        regime_params.append((np.random.uniform(low=-5, high=5), np.random.uniform(low=1, high=3)))

    # Sampling regime lengths using a prior distribution
    sampled_lengths = np.random.choice(regime_lengths, size=num_samples)

    # Initialize variables for change-points and regime assignments
    change_points = [0]
    regime_assignments = [0]

    # Generate change-points based on sampled regime lengths
    for length in sampled_lengths:
        next_change_point = change_points[-1] + length
        if next_change_point < len(data):
            change_points.append(next_change_point)
            regime_assignments.extend([i % num_regimes for i in range(length)])

    # Generate synthetic data based on regime assignments and emission parameters
    synthetic_data = np.array([np.random.normal(loc=regime_params[i][0], scale=regime_params[i][1]) for i in regime_assignments])

    return synthetic_data, change_points, regime_assignments, regime_params

# Detect change-points using the Semi-Markov Model
synthetic_data, change_points, regime_assignments, regime_params = detect_change_points(data, num_regimes=3)

# Plot the original data and the synthetic data with change-points
plt.figure(figsize=(12, 6))
plt.plot(df['date'], data, label='Original Data', color='blue')
plt.scatter(df['date'].iloc[change_points[:-1]], synthetic_data[change_points[:-1]], color='red', marker='x', label='Change Points')
plt.title('Change-Point Detection using Semi-Markov Model')
plt.xlabel('date')
plt.ylabel('meantemp')
plt.legend()
plt.show()

# Collect posterior distributions at change points
posterior_distributions = []
for i, cp in enumerate(change_points[1:]):
    segment_data = synthetic_data[change_points[i]:cp]
    posterior_distributions.append((cp, *norm.fit(segment_data)))

# Plot posterior distributions at change points
plt.figure(figsize=(12, 6))
for cp, mean, std in posterior_distributions:
    x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
    y = norm.pdf(x, loc=mean, scale=std)
    plt.plot(x, y, label=f'Posterior at Change Point {cp}')

plt.title('Posterior Distributions at Change Points')
plt.xlabel('Open')
plt.ylabel('Density')
plt.legend()
plt.show()