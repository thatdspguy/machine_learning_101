# Assumptions of Linear Regression

Linear regression relies on several key assumptions to ensure that the model provides accurate and reliable predictions. Violating these assumptions can lead to biased estimates, inefficiency, and incorrect inferences. Here are the main assumptions of linear regression:

## Linearity

The linearity assumption states that there is a linear relationship between the independent variables and the dependent variable. This means that the change in the dependent variable is proportional to the change in the independent variables. The relationship can be expressed as:

$$ y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \ldots + \beta_n x_n + \epsilon $$

where:
- $y$ is the dependent variable,
- $\beta_0, \beta_1, \ldots, \beta_n$ are the coefficients,
- $x_1, x_2, \ldots, x_n$ are the independent variables,
- $\epsilon$ is the error term.

## Independence

The independence assumption states that the observations in the dataset are independent of each other. This means that the error terms ($\epsilon$) are uncorrelated. If the observations are not independent, it can lead to biased estimates and incorrect conclusions. This assumption is particularly important in time series data, where autocorrelation can be present.

## Homoscedasticity

Homoscedasticity means that the variance of the error terms is constant across all levels of the independent variables. In other words, the spread of the residuals (differences between observed and predicted values) should be roughly the same for all predicted values. If the variance of the error terms is not constant (heteroscedasticity), it can lead to inefficient estimates and affect the validity of statistical tests.

## Normality

The normality assumption states that the error terms ($\epsilon$) are normally distributed. This assumption is important for hypothesis testing and constructing confidence intervals. Normality is particularly crucial when the sample size is small. For large sample sizes, the central limit theorem ensures that the sampling distribution of the coefficients will be approximately normal, even if the error terms are not perfectly normal.

## No Multicollinearity

Multicollinearity occurs when two or more independent variables are highly correlated with each other. This can make it difficult to determine the individual effect of each independent variable on the dependent variable. Multicollinearity can lead to unstable estimates and inflate the standard errors of the coefficients. Detecting multicollinearity can be done using metrics such as the Variance Inflation Factor (VIF).

## Summary

Understanding and checking these assumptions is crucial for building reliable linear regression models. If any of these assumptions are violated, steps can be taken to address the issues, such as transforming variables, adding interaction terms, or using alternative modeling techniques. Ensuring that these assumptions hold true helps in making accurate predictions and valid inferences from the model.
