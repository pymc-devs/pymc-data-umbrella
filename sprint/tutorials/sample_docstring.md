---
orphan: true
---

(sample_docstring)=
# Sample docstring
Sample docstring used to illustrate the steps in {ref}`docstring_tutorial`

```python
class Uniform(BoundedContinuous):
    r"""
    Continuous uniform log-likelihood.

    The pdf of this distribution is

    .. math::

       f(x \mid lower, upper) = \frac{1}{upper-lower}

    .. plot::

        import matplotlib.pyplot as plt
        import numpy as np
        import arviz as az
        plt.style.use('arviz-darkgrid')
        x = np.linspace(-3, 3, 500)
        ls = [0., -2]
        us = [2., 1]
        for l, u in zip(ls, us):
            y = np.zeros(500)
            y[(x<u) & (x>l)] = 1.0/(u-l)
            plt.plot(x, y, label='lower = {}, upper = {}'.format(l, u))
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.ylim(0, 1)
        plt.legend(loc=1)
        plt.show()

    ========  =====================================
    Support   :math:`x \in [lower, upper]`
    Mean      :math:`\dfrac{lower + upper}{2}`
    Variance  :math:`\dfrac{(upper - lower)^2}{12}`
    ========  =====================================

    Parameters
    ----------
    lower: float
        Lower limit.
    upper: float
        Upper limit.
    """
    rv_op = uniform
    bound_args_indices = (3, 4)  # Lower, Upper

    @classmethod
    def dist(cls, lower=0, upper=1, **kwargs):
        lower = at.as_tensor_variable(floatX(lower))
        upper = at.as_tensor_variable(floatX(upper))
        return super().dist([lower, upper], **kwargs)

    def get_moment(rv, size, lower, upper):
        lower, upper = at.broadcast_arrays(lower, upper)
        moment = (lower + upper) / 2
        if not rv_size_is_none(size):
            moment = at.full(size, moment)
        return moment

    def logcdf(value, lower, upper):
        """
        Compute the log of the cumulative distribution function for Uniform distribution
        at the specified value.

        Parameters
        ----------
        value: numeric or np.ndarray or `TensorVariable`
            Value(s) for which log CDF is calculated. If the log CDF for multiple
            values are desired the values must be provided in a numpy array or `TensorVariable`.

        Returns
        -------
        TensorVariable
        """
        return at.switch(
            at.lt(value, lower) | at.lt(upper, lower),
            -np.inf,
            at.switch(
                at.lt(value, upper),
                at.log(value - lower) - at.log(upper - lower),
                0,
            ),
        )
```
