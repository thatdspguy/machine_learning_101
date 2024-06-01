## Dealing with Violations of Assumptions

When the assumptions of linear regression are violated, the model's estimates may become biased, inefficient, or invalid. There are various techniques to address these violations and improve the model's performance.

### Transformations

Transformations are often used to address non-linearity, non-normality, and heteroscedasticity in the data.

#### Log Transformation

Log transformation can help stabilize the variance and make the data more normally distributed. It is particularly useful when dealing with positively skewed data. By applying the log transformation to the dependent variable or independent variables, the relationship can become more linear, and heteroscedasticity can be reduced.

For example, if the dependent variable $y$ is skewed, you can transform it as follows:

$$ y' = \log(y) $$

Similarly, if an independent variable $x$ is skewed, you can transform it as follows:

$$ x' = \log(x) $$

#### Polynomial Features

When the relationship between the dependent variable and independent variables is non-linear, adding polynomial features can help capture the non-linearity. Polynomial regression involves adding higher-degree terms of the independent variables to the model. For example, to model a quadratic relationship, you can add a squared term:

$$ y = \beta_0 + \beta_1 x + \beta_2 x^2 + \epsilon $$

Higher-degree polynomial features can be added to capture more complex relationships. However, it's important to be cautious of overfitting when adding many polynomial terms.

### Regularization Techniques

Regularization techniques are used to address multicollinearity and overfitting by adding a penalty to the regression coefficients. These techniques help improve the model's generalizability and interpretability.

#### Ridge Regression

Ridge regression, also known as L2 regularization, adds a penalty equal to the sum of the squared coefficients to the cost function. This penalty term discourages large coefficients, thus reducing the impact of multicollinearity and overfitting. The cost function for ridge regression is:

$$ J(\theta) = \text{MSE} + \lambda \sum_{j=1}^{n} \theta_j^2 $$

where:
- $\lambda$ is the regularization parameter that controls the strength of the penalty,
- $\theta_j$ are the regression coefficients.

By tuning $\lambda$, you can find a balance between fitting the training data and keeping the model simple.

#### Lasso Regression

Lasso regression, also known as L1 regularization, adds a penalty equal to the sum of the absolute values of the coefficients to the cost function. This penalty term can shrink some coefficients to exactly zero, effectively performing variable selection and improving model interpretability. The cost function for lasso regression is:

$$ J(\theta) = \text{MSE} + \lambda \sum_{j=1}^{n} |\theta_j| $$

Lasso regression is particularly useful when you suspect that only a subset of the predictors are actually relevant to the model. By tuning $\lambda$, you can control the number of predictors included in the model.

### Summary

Dealing with violations of linear regression assumptions involves using techniques such as transformations and regularization. Log transformation and polynomial features can address issues related to non-linearity, non-normality, and heteroscedasticity. Regularization techniques like ridge regression and lasso regression help mitigate multicollinearity and overfitting, leading to more robust and interpretable models. Understanding and applying these techniques is essential for improving the performance and reliability of linear regression models.