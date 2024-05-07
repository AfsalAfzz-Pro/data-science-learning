## Evaluating Regression Models
  

There are three types of metrics used to evaluate the performance of regression models.

  

*  **Mean Squared Error (MSE):**
	* MSE measures the average **squared** difference between the predicted values (`y_pred`) and the actual target values (`y_actual`) in your data.
    * **Calculation**
	    * `MSE = (1/n) * Σ (y_pred_i - y_true_i)^2`

* **Root Mean Squared Error (RMSE)**
	* It is similar to MSE but is the square root version of it.
	* **Calculation**
		* `RMSE = sqrt( (1/n) * Σ (y_pred_i - y_true_i)^2 )`

* **Mean Absolute Error (MAE)**
	* MAE measures the average **absolute** difference between the predicted values (`y_pred`) and the actual target values (`y_actual`) in your data.
	* **Calculation**
		* `MAE = (1/n) * Σ |y_pred_i - y_true_i|`
* **R-squared (R²)**
	*  R² values range from 0 to 1.
	-   A value of 1 indicates a perfect fit (the model explains all the variance in the data).
	- **Calculation**
		- `R² = 1 - (Σ (y_true_i - y_pred_i)^2) / (Σ (y_true_i - y_me