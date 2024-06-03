# Gradients

Gradients are a fundamental concept in calculus and are crucial for optimization in machine learning. The gradient of a function measures the rate of change of the function with respect to its input variables. In a multivariable context, the gradient generalizes the derivative and provides a vector of partial derivatives.

## Definition

The gradient of a scalar-valued function $f(x_1, x_2, \ldots, x_n)$ with respect to its input variables is a vector of partial derivatives. It is denoted by $\nabla f$ and is defined as:

$$ \nabla f = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix} $$

The gradient points in the direction of the steepest ascent of the function.

## Notation

The gradient can be denoted in several ways:
- $\nabla f$
- $\text{grad } f$
- $\frac{\partial f}{\partial x}$ (vector notation)

## Gradient Vector

The gradient vector consists of the partial derivatives of the function with respect to each of its input variables. For a function $f(x, y)$, the gradient is:

$$ \nabla f = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix} $$

## Basic Properties of Gradients

1. **Direction of Steepest Ascent:** The gradient points in the direction of the steepest ascent of the function.
2. **Magnitude:** The magnitude of the gradient vector indicates the rate of increase in that direction.
3. **Zero Gradient:** At a local maximum, minimum, or saddle point, the gradient is zero.

## Example of Gradient Calculation

### Example 1: Gradient of a Function

Consider the function:

$$ f(x, y) = 3x^2 + 4y^2 $$

The partial derivatives are:

$$ \frac{\partial f}{\partial x} = 6x $$
$$ \frac{\partial f}{\partial y} = 8y $$

So, the gradient is:

$$ \nabla f = \begin{bmatrix} 6x \\ 8y \end{bmatrix} $$

### Example 2: Gradient of a More Complex Function

Consider the function:

$$ f(x, y, z) = x^2y + yz^3 $$

The partial derivatives are:

$$ \frac{\partial f}{\partial x} = 2xy $$
$$ \frac{\partial f}{\partial y} = x^2 + z^3 $$
$$ \frac{\partial f}{\partial z} = 3yz^2 $$

So, the gradient is:

$$ \nabla f = \begin{bmatrix} 2xy \\ x^2 + z^3 \\ 3yz^2 \end{bmatrix} $$

## Applications in Machine Learning

Gradients are extensively used in optimization algorithms to train machine learning models. One of the most common applications is in the gradient descent algorithm, which is used to minimize loss functions. More information about 

### Gradient Descent

Gradient descent is an iterative optimization algorithm used to find the minimum of a function. The algorithm updates the parameters in the opposite direction of the gradient of the loss function with respect to the parameters. More information about gradient descent can be found [here](../../machine_learning_algorithms/supervised_learning/linear_regression/model_training.md#gradient-descent).
