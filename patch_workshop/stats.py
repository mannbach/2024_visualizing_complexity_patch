from typing import Union, List, Any, Tuple

import numpy as np

def compute_cdf(a_vals: Union[List[Any], np.ndarray]) -> Tuple[np.ndarray, np.ndarray]:
    """Computes the cumulative distribution function of the given values.

    Parameters
    ----------
    a_vals : Union[List[Any], np.ndarray]
        A list of values to compute the CDF for.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        A tuple of two equal-length arrays, the first containing the sorted values and the second the CDF.
    """
    a_sort = np.sort(a_vals)
    return a_sort, (np.arange(len(a_sort)) / len(a_sort))
