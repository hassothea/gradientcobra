# gradientcobra

This is the `python` package implementation of `Gradient COBRA` method by [S. Has (2023)](https://jdssv.org/index.php/jdssv/article/view/70). 

## Summary

Gradient COBRA is a kernel-based consensual aggregation for regression problem that extends the naive kernel-based of Biau et al. (2016) to a more general regular kernel-based configuration. It is theoretically shown that Gradient COBRA inherits the consistency of the consistent basic estimator in the list, and the same rate of convergence is archived for exponentially tail-delaying kernel functions. On top of that, gradient descent algorithm is proposed to efficiently estimate the bandwidth parameter of the aggregation method. It is shown to be up to hundred times faster than the classical method and `python` package [pycobra](https://arxiv.org/abs/1707.00558).

## Download the package 

`pip install gradientcobra`

## Documentation

For how to use the package, read the [documentation](https://github.com/hassothea/gradientcobra).

## Citations

If you find `gradientcobra` interesting or helpful, please cite the following papers:

- Has, S., 2023. Gradient COBRA: A kernel-based consensual aggregation for regression. Journal of Data Science, Statistics and Visualization. [https://doi.org/10.52933/jdssv.v3i2](https://jdssv.org/index.php/jdssv/article/view/70)




