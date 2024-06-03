# Derivatives

Derivatives are a fundamental concept in calculus that measure the rate of change of a function with respect to its input variables. They provide critical insights into how functions behave and are essential for various applications in mathematics, physics, engineering, and, of course, machine learning.

## Definition

The derivative of a function $f(x)$ with respect to $x$ is defined as the limit of the average rate of change of the function over an interval as the interval approaches zero. Mathematically, the derivative is expressed as:

$$ f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x} $$

If this limit exists, $f$ is said to be differentiable at $x$.

## Notation

Derivatives can be denoted in several ways:
- $f'(x)$
- $\frac{df}{dx}$
- $D_x f(x)$

## Basic Rules of Differentiation

Differentiation is the process of finding the derivative of a function. Several basic rules can simplify this process:

### Power Rule

The derivative of $x^n$ is $nx^{n-1}$.

$$ \frac{d}{dx} x^n = nx^{n-1} $$

### Sum Rule

The derivative of the sum of two functions is the sum of their derivatives.

$$ \frac{d}{dx} [f(x) + g(x)] = f'(x) + g'(x) $$

### Product Rule

The derivative of the product of two functions is given by:

$$ \frac{d}{dx} [f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x) $$

### Quotient Rule

The derivative of the quotient of two functions is given by:

$$ \frac{d}{dx} \left[ \frac{f(x)}{g(x)} \right] = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{[g(x)]^2} $$

### Chain Rule

The derivative of a composite function is given by:

$$ \frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x) $$

## Higher-Order Derivatives

Higher-order derivatives measure the rate of change of the rate of change. The second derivative, denoted as $f''(x)$ or $\frac{d^2 f}{dx^2}$, is the derivative of the first derivative:

$$ f''(x) = \frac{d}{dx} f'(x) $$

Higher-order derivatives provide deeper insights into the behavior of functions, such as concavity and points of inflection.

## Applications of Derivatives

While detailed applications of derivatives in machine learning will be covered later in the book, it is essential to recognize their importance in various fields:

- **Optimization:** Derivatives are used to find the maxima and minima of functions, which is crucial in optimization problems.
- **Physics:** They describe the rate of change of physical quantities, such as velocity and acceleration.
- **Economics:** They help in understanding marginal costs and marginal revenues.

## Examples of Differentiation

### Example 1: Differentiating a Polynomial

Consider the polynomial function:

$$ f(x) = 3x^3 + 5x^2 - 2x + 7 $$

The derivative is found using the power rule:

$$ f'(x) = 9x^2 + 10x - 2 $$

### Example 2: Differentiating a Composite Function

Consider the composite function:

$$ f(x) = \sin(x^2) $$

Using the chain rule:

$$ f'(x) = \cos(x^2) \cdot 2x = 2x \cos(x^2) $$

## Summary

Derivatives measure the rate of change of a function and are a cornerstone of calculus. Understanding the rules of differentiation and how to apply them is crucial for analyzing the behavior of functions. In machine learning, derivatives are foundational for optimization algorithms and other advanced techniques.

In the next section, we will delve deeper into integrals and their applications in machine learning.
