## Correlation and Covariance with an Example

**Example:**

This example explores the relationship between "Height" and "Weight" using covariance and correlation in Python.

**Data:**

* **Height:** Height (in inches) of individuals. (Sample data: `[65, 68, 70, 61, 72]`)
* **Weight:** Weight (in pounds) of individuals. (Sample data: `[150, 170, 175, 140, 180]`)

**Calculations:**

* **Covariance:**  Measures how "Height" and "Weight" change together (calculated using `np.cov`).
    * Positive covariance: Taller individuals tend to have higher weights.
    * Negative covariance: Taller individuals tend to have lower weights.

* **Correlation:**  Standardized relationship between "Height" and "Weight" (calculated using `np.corrcoef`).
    * Closer to +1: Strong positive linear relationship (taller = heavier).
    * Closer to -1: Strong negative linear relationship (taller = lighter).
    * Around 0: No linear relationship.

**Code:**

```python
import numpy as np

# ... (data definition)

# Calculate covariance
covariance = np.cov(height, weight)[0][1]

# Calculate correlation
correlation = np.corrcoef(height, weight)[0][1]

print("Covariance between Height and Weight:", covariance)
print("Correlation between Height and Weight:", correlation)
```

**Conclusion:**

By calculating covariance and correlation, we can quantify the relationship between "Height" and "Weight", aiding data analysis and modeling decisions.
