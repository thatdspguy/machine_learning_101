# Model Training

## Cost Function

In linear regression, the cost function measures how well the model's predictions match the actual data. It quantifies the error between predicted values and actual values, guiding the optimization process to find the best-fitting line.

### Mean Squared Error (MSE)

Mean Squared Error (MSE) is the most commonly used cost function for linear regression. It calculates the average of the squared differences between the predicted values ($\hat{y}$) and the actual values ($y$):

$$ \text{MSE} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i)^2 $$

where:
- $m$ is the number of data points,
- $\hat{y}_i$ is the predicted value for the $i$-th data point,
- $y_i$ is the actual value for the $i$-th data point.

MSE is sensitive to outliers because it squares the errors, giving more weight to larger errors. Minimizing the MSE helps the model achieve a closer fit to the data.

### Mean Absolute Error (MAE)

Mean Absolute Error (MAE) is another cost function that measures the average of the absolute differences between the predicted values ($\hat{y}$) and the actual values ($y$):

$$ \text{MAE} = \frac{1}{m} \sum_{i=1}^{m} |\hat{y}_i - y_i| $$

MAE is less sensitive to outliers compared to MSE because it does not square the errors. However, it may result in a less smooth optimization landscape, making it less preferred for gradient-based optimization methods.

## Optimization Techniques

The goal of optimization in linear regression is to find the parameters ($\theta$) that minimize the cost function. Two common optimization techniques are Gradient Descent and the Normal Equation.

### Gradient Descent

Gradient Descent is an iterative optimization algorithm used to minimize the cost function. It updates the model parameters in the direction of the negative gradient of the cost function. The update rule for Gradient Descent is:

$$ \theta_j := \theta_j - \alpha \frac{\partial J(\theta)}{\partial \theta_j} $$

where:
- $\theta_j$ is the $j$-th parameter,
- $\alpha$ is the learning rate,
- $J(\theta)$ is the cost function.

The partial derivative of the cost function with respect to $\theta_j$ for MSE is:

$$ \frac{\partial J(\theta)}{\partial \theta_j} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i) x_{ij} $$

where $x_{ij}$ is the $j$-th feature of the $i$-th data point.

Gradient Descent can be performed using different variants:
- **Batch Gradient Descent:** Uses the entire dataset to compute the gradients and update the parameters.
- **Stochastic Gradient Descent (SGD):** Uses a single data point to compute the gradients and update the parameters, making it faster but noisier.
- **Mini-batch Gradient Descent:** Uses a small batch of data points to compute the gradients and update the parameters, balancing the speed and noise trade-off.

### Normal Equation

The Normal Equation is a closed-form solution for finding the optimal parameters in linear regression without requiring iterative optimization. It directly computes the parameters that minimize the cost function. The Normal Equation for linear regression is:

$$ \theta = (X^T X)^{-1} X^T y $$

where:
- $X$ is the matrix of input features,
- $y$ is the vector of output values.

The Normal Equation is computationally efficient for small to medium-sized datasets but becomes impractical for very large datasets due to the matrix inversion step, which has a time complexity of $O(n^3)$.

## Summary

Both Gradient Descent and the Normal Equation have their advantages and limitations. Gradient Descent is versatile and scalable to large datasets but requires careful tuning of the learning rate and can be slow to converge. The Normal Equation provides a direct solution but is limited by its computational complexity for large datasets. Understanding these optimization techniques is crucial for effectively training linear regression models and achieving accurate predictions.
