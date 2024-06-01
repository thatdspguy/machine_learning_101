# Assumptions of Logistic Regression

Logistic regression, like any statistical model, relies on several key assumptions to ensure that the estimates it produces are accurate and reliable. Violating these assumptions can lead to biased estimates, inefficiency, and invalid inferences. Below are the main assumptions of logistic regression:

## Linearity of the Logit

### Definition

The relationship between the independent variables and the logit (log-odds) of the dependent variable should be linear. This means that the log-odds of the probability of the outcome should be a linear combination of the independent variables. Mathematically, this can be expressed as:

$$ \log\left(\frac{p}{1 - p}\right) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \ldots + \beta_n x_n $$

### Implications

If this assumption is violated, the model may not adequately fit the data, leading to biased coefficients. One way to check this assumption is to examine plots of the logit versus each predictor.

## Independence of Errors

### Definition

The error terms (residuals) should be independent of each other. This assumption implies that the observations in the dataset are independent. It means that the value of the residual for one observation does not depend on the value of the residual for another observation.

### Implications

Violating this assumption can lead to underestimated standard errors and inflated type I error rates (false positives). This assumption is especially important in time series data or clustered data, where observations may be correlated.

## Absence of Multicollinearity

### Definition

The independent variables should not be highly correlated with each other. Multicollinearity occurs when two or more predictors in the model are correlated, meaning that one predictor can be linearly predicted from the others with a substantial degree of accuracy.

### Implications

High multicollinearity can make it difficult to determine the individual effect of each predictor on the dependent variable. It can lead to unstable estimates of coefficients and inflated standard errors. Variance Inflation Factor (VIF) and tolerance are common metrics used to detect multicollinearity.

## Adequate Sample Size

### Definition

Logistic regression requires an adequate sample size to provide reliable and stable estimates. A common rule of thumb is to have at least 10 events per predictor variable. For binary logistic regression, this means having at least 10 cases of the less frequent outcome for each predictor variable in the model.

### Implications

If the sample size is too small, the model may not converge, or the estimates may be biased and unstable. Adequate sample size helps ensure that the model has enough power to detect meaningful effects and provides more precise estimates of the coefficients.

### Summary

Understanding and checking the assumptions of logistic regression is crucial for building reliable models. The assumptions include the linearity of the logit, independence of errors, absence of multicollinearity, and adequate sample size. Ensuring that these assumptions hold true helps in making accurate predictions and valid inferences from the logistic regression model. If any of these assumptions are violated, steps can be taken to address the issues, such as transforming variables, adding interaction terms, or using alternative modeling techniques.
