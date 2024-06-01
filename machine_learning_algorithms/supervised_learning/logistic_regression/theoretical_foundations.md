# Theoretical Foundations

## Basic Concepts

### Dependent and Independent Variables

In logistic regression, the goal is to model the relationship between one or more independent variables (predictors) and a dependent variable (response) that is binary. The dependent variable, $y$, takes on only two possible values, typically coded as 0 or 1. The independent variables, $X$, can be continuous or categorical and are used to predict the probability of the dependent variable being 1.

### Binary Outcomes

Binary outcomes are those where there are only two possible states or classes. Examples include:
- Disease presence (1) vs. absence (0)
- Default on a loan (1) vs. no default (0)
- Success (1) vs. failure (0)

### Odds and Odds Ratios

The odds represent the ratio of the probability of an event occurring to the probability of it not occurring. If $p$ is the probability of an event occurring, then the odds are calculated as:

$$ \text{Odds} = \frac{p}{1 - p} $$

The odds ratio compares the odds of an event occurring in one group to the odds of it occurring in another group. It is a measure of association between an exposure and an outcome.

## Mathematical Formulation

### Logistic Function

The logistic function, also known as the sigmoid function, is used to model the probability of the binary outcome. It maps any real-valued number into the (0, 1) interval, making it suitable for representing probabilities. The logistic function is defined as:

$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$

where $z$ is a linear combination of the input features.

### Logit Function

The logit function is the natural logarithm of the odds. It is the inverse of the logistic function and is used to model the relationship between the predictors and the log-odds of the binary outcome. The logit function is defined as:

$$ \text{logit}(p) = \log\left(\frac{p}{1 - p}\right) $$

### Hypothesis Function

In logistic regression, the hypothesis function represents the probability that the dependent variable is 1 given the independent variables. The hypothesis function is defined as:

$$ h_\theta(x) = \sigma(\theta^T x) = \frac{1}{1 + e^{-\theta^T x}} $$

where:
- $h_\theta(x)$ is the predicted probability,
- $\theta$ is the vector of model parameters,
- $x$ is the vector of input features.

The goal of logistic regression is to find the optimal parameters $\theta$ that best fit the data, typically using maximum likelihood estimation.

### Summary

The theoretical foundations of logistic regression involve understanding the relationship between dependent and independent variables, binary outcomes, and the mathematical formulation using the logistic and logit functions. By grasping these concepts, you can effectively apply logistic regression to classify binary outcomes and make informed predictions.
