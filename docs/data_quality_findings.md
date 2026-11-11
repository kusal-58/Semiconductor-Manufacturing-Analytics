# SECOM Dataset – Initial Data Quality Analysis

## 1\. Dataset Overview

* Total observations: 1567
* Total sensor variables: 590
* Total missing measurements: 41951
* Overall missing data: 4.54%

## 2\. Missing Data Distribution

* Sensors with more than 50% missing data: 28
* Sensors with more than 80% missing data: 8
* Sensors with 100% missing data: 0

## 3\. Key Findings

Missing measurements are unevenly distributed across
the sensor variables.

Although the overall missing data percentage is
relatively low, several individual sensor variables
have substantial missing measurements.

The highest missing data percentage is approximately
91.19%.

## 4\. Initial Engineering Interpretation

Variables with high missing data percentages require
further investigation before deciding whether to
retain, remove or impute them.

Missing measurements should not automatically be
replaced with zero because missing data does not
necessarily represent a zero measurement.

## 5\. Next Steps

* Investigate missing data patterns.
* Examine relationships between missingness and
pass/fail outcomes.
* Develop an appropriate data-cleaning strategy.



\## 6. Missing Data Visualisation



!\[Missing Data Distribution](../figures/missing\_data\_distribution.png)

