# Model Training

Training a logistic regression model involves finding the optimal parameters that minimize the difference between the predicted probabilities and the actual outcomes. This is typically done by minimizing a cost function using various optimization techniques.

## Cost Function

### Log-Loss (Binary Cross-Entropy)

The cost function for logistic regression is called log-loss, also known as binary cross-entropy. It measures the performance of a classification model whose output is a probability value between 0 and 1. The log-loss function is defined as:

$$ J(\theta) = - \frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log(h_\theta(x^{(i)})) + (1 - y^{(i)}) \log(1 - h_\theta(x^{(i)})) \right] $$

where:
- $m$ is the number of training examples,
- $y^{(i)}$ is the actual label of the $i$-th training example,
- $h_\theta(x^{(i)})$ is the predicted probability for the $i$-th training example,
- $\theta$ is the vector of model parameters.

The log-loss function penalizes incorrect predictions more strongly, encouraging the model to produce probabilities that are as close to the actual binary labels as possible.

## Optimization Techniques

### Gradient Descent

Gradient Descent is an iterative optimization algorithm used to minimize the cost function. It works by iteratively adjusting the model parameters in the direction of the steepest descent of the cost function. The update rule for gradient descent in logistic regression is:

$$ \theta_j := \theta_j - \alpha \frac{\partial J(\theta)}{\partial \theta_j} $$

where:
- $\theta_j$ is the $j$-th parameter,
- $\alpha$ is the learning rate,
- $\frac{\partial J(\theta)}{\partial \theta_j}$ is the partial derivative of the cost function with respect to $\theta_j$.

The partial derivative of the log-loss function with respect to $\theta_j$ is:

$$ \frac{\partial J(\theta)}{\partial \theta_j} = \frac{1}{m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right) x_j^{(i)} $$

Gradient Descent continues to update the parameters until the cost function converges to a minimum value.

### Newton-Raphson Method

The Newton-Raphson method is an iterative optimization algorithm that uses second-order derivatives to find the minimum of the cost function more quickly. It uses the Hessian matrix (a matrix of second-order partial derivatives) to adjust the parameters. The update rule for the Newton-Raphson method is:

$$ \theta := \theta - H^{-1} \nabla J(\theta) $$

where:
- $H$ is the Hessian matrix of second-order partial derivatives,
- $\nabla J(\theta)$ is the gradient vector of first-order partial derivatives.

The Hessian matrix for logistic regression is given by:

$$ H = \frac{1}{m} \sum_{i=1}^{m} h_\theta(x^{(i)})(1 - h_\theta(x^{(i)})) x^{(i)} {x^{(i)}}^T $$

The Newton-Raphson method converges faster than gradient descent but requires the computation of the Hessian matrix, making it computationally expensive for large datasets.

### Stochastic Gradient Descent (SGD)

Stochastic Gradient Descent (SGD) is a variant of gradient descent that updates the model parameters using only one training example at a time. This makes it faster and more suitable for large datasets. The update rule for SGD is:

$$ \theta_j := \theta_j - \alpha \left( h_\theta(x^{(i)}) - y^{(i)} \right) x_j^{(i)} $$

where:
- $x^{(i)}$ and $y^{(i)}$ are the $i$-th training example and its corresponding label.

SGD introduces more noise into the optimization process, which can help the model escape local minima but may also lead to a less smooth convergence.

### Summary

Model training in logistic regression involves minimizing the log-loss cost function using optimization techniques such as Gradient Descent, the Newton-Raphson method, and Stochastic Gradient Descent (SGD). Each technique has its advantages and trade-offs, with gradient descent being the most commonly used due to its simplicity and effectiveness for large-scale problems.
