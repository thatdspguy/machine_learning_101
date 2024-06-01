# Types of Logistic Regression

Logistic regression can be extended to handle more complex scenarios beyond simple binary classification. In this section, we will explore three main types of logistic regression: binary logistic regression, multinomial logistic regression, and ordinal logistic regression.

## Binary Logistic Regression

### Definition

Binary logistic regression is the most basic form of logistic regression. It models the relationship between one or more independent variables and a binary dependent variable, which has only two possible outcomes (e.g., success/failure, yes/no, 1/0). The goal is to estimate the probability that the dependent variable belongs to a particular category.

### Assumptions

1. **Binary Outcome:** The dependent variable must be binary.
2. **Independence:** Observations are assumed to be independent of each other.
3. **Linearity of Logit:** The logit (log-odds) of the outcome should be a linear combination of the independent variables.
4. **No Multicollinearity:** Independent variables should not be highly correlated with each other.
5. **Large Sample Size:** A sufficiently large sample size is required to provide reliable estimates.

## Multinomial Logistic Regression

### Definition

Multinomial logistic regression is an extension of binary logistic regression that allows for more than two categories of the dependent variable. It is used when the dependent variable is nominal and can take on three or more possible outcomes. Multinomial logistic regression models the probability of each category relative to a reference category.

### Assumptions

1. **Nominal Outcome:** The dependent variable must be nominal with three or more categories.
2. **Independence:** Observations are assumed to be independent of each other.
3. **Linearity of Logit:** The logit of each outcome category relative to the reference category should be a linear combination of the independent variables.
4. **No Multicollinearity:** Independent variables should not be highly correlated with each other.
5. **Large Sample Size:** A sufficiently large sample size is required to provide reliable estimates.

## Ordinal Logistic Regression

### Definition

Ordinal logistic regression is used when the dependent variable is ordinal, meaning it has a natural order but the intervals between categories are not necessarily equal. This type of regression models the relationship between the independent variables and the cumulative probabilities of the ordinal categories.

### Assumptions

1. **Ordinal Outcome:** The dependent variable must be ordinal with a natural ordering of categories.
2. **Proportional Odds:** The relationship between each pair of outcome groups is assumed to be the same (i.e., proportional odds assumption).
3. **Independence:** Observations are assumed to be independent of each other.
4. **Linearity of Logit:** The logit of the cumulative probabilities should be a linear combination of the independent variables.
5. **No Multicollinearity:** Independent variables should not be highly correlated with each other.
6. **Large Sample Size:** A sufficiently large sample size is required to provide reliable estimates.

### Summary

Understanding the different types of logistic regression allows for more flexibility in modeling various types of categorical outcomes. Binary logistic regression handles binary outcomes, multinomial logistic regression handles nominal outcomes with more than two categories, and ordinal logistic regression handles ordinal outcomes with ordered categories. Each type has specific assumptions that must be met to ensure accurate and reliable results.
