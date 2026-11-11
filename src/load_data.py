import pandas as pd
from scipy.stats import mannwhitneyu

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




# Investigate missing measurements per observation

missing_per_observation = sensor_data.isnull().sum(axis=1)

# Combine missing measurements with manufacturing outcomes

analysis_data = pd.DataFrame({
    "Missing_Count": missing_per_observation,
    "Outcome": labels.iloc[:, 0]
})

# Calculate average missing measurements for each outcome

print("\nAverage missing measurements by outcome:")

print(
    analysis_data.groupby("Outcome")["Missing_Count"].mean()
)



# Detailed comparison of missing measurements

print("\nMissing data statistics by outcome:")

print(
    analysis_data.groupby("Outcome")["Missing_Count"].describe()
)



# Statistical comparison of missing measurements

pass_data = analysis_data[
    analysis_data["Outcome"] == -1
]["Missing_Count"]

fail_data = analysis_data[
    analysis_data["Outcome"] == 1
]["Missing_Count"]

statistic, p_value = mannwhitneyu(
    pass_data,
    fail_data,
    alternative="two-sided"
)

print("\nMann-Whitney U Test")
print("U statistic:", statistic)
print("P-value:", p_value)

if p_value < 0.05:
    print("The distributions differ statistically significantly.")
else:
    print("No statistically significant difference detected.")
    
    
 # Missing-value rate by manufacturing outcome

missing_by_outcome = analysis_data.copy()

missing_by_outcome["Outcome"] = missing_by_outcome["Outcome"]

# Create a binary missing-value matrix
missing_matrix = sensor_data.isnull().astype(int)

# Calculate missing rates separately for PASS and FAIL
missing_matrix["Outcome"] = labels.iloc[:, 0].values

missing_rates = missing_matrix.groupby("Outcome").mean() * 100

print("\nMissing percentage per sensor by outcome:")
print(missing_rates.iloc[:, :10])


# Difference in missing-data rates between FAIL and PASS

missing_difference = (
    missing_rates.loc[1] - missing_rates.loc[-1]
)

# Rank sensors by absolute difference

largest_differences = (
    missing_difference.abs()
    .sort_values(ascending=False)
    .head(15)
)

print("\nTop 15 sensors with largest missing-rate differences:")

print(largest_differences)


interesting_sensors = [73, 72, 346, 345]

print("\nMissing rates for selected sensors:")

print(missing_rates[interesting_sensors])


# Compare missing-data patterns

selected_sensors = [72, 73, 345, 346]

missing_patterns = sensor_data[selected_sensors].isnull()

print("\nAre missing patterns identical?")

for sensor in selected_sensors[1:]:
    identical = missing_patterns[72].equals(
        missing_patterns[sensor]
    )

    print(f"Sensor 72 vs Sensor {sensor}: {identical}")
    
    # Count simultaneous missing measurements

simultaneous_missing = missing_patterns.all(axis=1)

print(
    "\nObservations where all four sensors are missing:",
    simultaneous_missing.sum()
)

print(
    "Percentage of all observations:",
    simultaneous_missing.mean() * 100
)


# Missingness by manufacturing outcome

missing_outcome_analysis = pd.crosstab(
    labels.iloc[:, 0],
    simultaneous_missing
)

missing_outcome_analysis.columns = [
    "Sensors Available",
    "Sensors Missing"
]

print("\nMissingness by manufacturing outcome:")
print(missing_outcome_analysis)

print("\nPercentage within each outcome:")
print(
    pd.crosstab(
        labels.iloc[:, 0],
        simultaneous_missing,
        normalize="index"
    ) * 100
)