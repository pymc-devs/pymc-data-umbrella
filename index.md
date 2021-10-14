# Sprint

Welcome!

:::{warning} Sprint website and material in construction
:::

An example code cell with auto links:

```python
import numpy as np
import pymc as pm

rng = np.random.default_rng(10)
X = rng.normal(size=100)
y = rng.normal(X) * 1.2

with pm.Model() as linear_model:
    weights = pm.Normal("weights", mu=0, sigma=1)
    noise = pm.Gamma("noise", alpha=2, beta=1)
    pm.Normal(
        "y_observed",
        mu=X @ weights,
        sigma=noise,
        observed=y,
    )

    prior = pm.sample_prior_predictive()
    posterior = pm.sample()
    posterior_pred = pm.sample_posterior_predictive(posterior)
```
