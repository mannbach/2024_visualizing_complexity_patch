from typing import Union, List, Any, Tuple

import numpy as np

def compute_cdf(a_vals: Union[List[Any], np.ndarray]) -> Tuple[np.ndarray, np.ndarray]:
    a_sort = np.sort(a_vals)
    return a_sort, (np.arange(len(a_sort)) / len(a_sort))
