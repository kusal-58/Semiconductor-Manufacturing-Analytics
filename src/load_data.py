import pandas as pd

# Load the sensor data
sensor_data = pd.read_csv(
    "../data/secom.data",
    sep=r"\s+",
    header=None
)

# Load the labels
labels = pd.read_csv(
    "../data/secom_labels.data",
    sep=r"\s+",
    header=None
)

print("Sensor Data Shape:", sensor_data.shape)
print("Labels Shape:", labels.shape)
print(labels.head())
print(labels.info())




print("\n--- SENSOR DATA ---")

print("Shape:", sensor_data.shape)

print("\nFirst five rows:")
print(sensor_data.head())

print("\nData information:")
sensor_data.info()

print("\n--- LABEL DATA ---")

print("Shape:", labels.shape)

print("\nFirst five rows:")
print(labels.head())

print("\nLabel distribution:")
print(labels.iloc[:, 0].value_counts())

# Missing value analysis

missing_values = sensor_data.isnull().sum()

print("\nTotal missing values:", missing_values.sum())

print("\nColumns with missing values:",
      (missing_values > 0).sum())

print("\nPercentage of missing values:",
      (missing_values.sum().sum() /
       (sensor_data.shape[0] * sensor_data.shape[1])) * 100)


# Missing values per sensor

missing_summary = sensor_data.isnull().sum()

missing_summary = missing_summary.sort_values(
    ascending=False
)

print("\nTop 20 sensors with missing measurements:")
print(missing_summary.head(20))

# Calculate missing percentage per sensor

missing_percentage = (
    sensor_data.isnull().mean() * 100
)

# Count sensors in different missing-data categories

print("\nSensors with more than 50% missing:")
print((missing_percentage > 50).sum())

print("\nSensors with more than 80% missing:")
print((missing_percentage > 80).sum())

print("\nSensors with 100% missing:")
print((missing_percentage == 100).sum())

import matplotlib.pyplot as plt

# Plot missing data percentage

plt.figure(figsize=(14, 5))

plt.bar(
    missing_percentage.index,
    missing_percentage.values
)

plt.axhline(
    y=50,
    linestyle="--",
    label="50% missing threshold"
)

plt.xlabel("Sensor Index")
plt.ylabel("Missing Values (%)")
plt.title("Missing Measurement Distribution Across SECOM Sensors")

plt.legend()
plt.tight_layout()

plt.savefig("../figures/missing_data_distribution.png", dpi=300)

plt.show()