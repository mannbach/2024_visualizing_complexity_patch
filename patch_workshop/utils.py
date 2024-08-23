from typing import Tuple, Optional

from netin import PATCH, TCH, ERPATCH, Graph
from netin.utils.constants import ERPATCH_MODEL_NAME, TCH_MODEL_NAME

from .constants import MAP_MODEL_NAME_TO_GLOBAL, MAP_GLOBAL_TO_MODEL_NAME, LFM_RANDOM

def create_graph(
        N: int, m: int, f_m: float,
        h: float, tc: float,
        lfm_global: str, lfm_local: str,
        seed: Optional[int]=None) -> Graph:
    """Generates a single graph based on the given parameters.

    Parameters
    ----------
    N : int
        Number of nodes
    m : int
        Number of new edges per node
    f_m : float
        Fraction of minority nodes
    h : float
        Homophily
    tc : float
        The triadic closure probability
    lfm_global : str
        The global link formation mechanism
    lfm_local : str
        The local link formation mechanism
    seed : Optional[int], optional
        The random seed, by default None

    Returns
    -------
    Graph
        A simulated graph object
    """
    tcu, model_name = translate_local_global_to_model(
        lfm_global=lfm_global, lfm_local=lfm_local)

    Model = PATCH
    if model_name == ERPATCH_MODEL_NAME:
        Model = ERPATCH
    elif model_name == TCH_MODEL_NAME:
        Model = TCH

    model = Model(n=N,k=m,f_m=f_m,h_mm=h, h_MM=h, tc=tc, tc_uniform=tcu, seed=seed)
    model.generate()
    return model

def translate_model_to_global_local(
        tcu: bool,
        model_name: str) -> Tuple[str, str]:
    """Translate the model name and the triadic closure uniformity to the local/global terminology."""
    assert tcu or (model_name != ERPATCH),\
        "ERPATCH requires triadic closure uniformity."
    lfm_global = MAP_MODEL_NAME_TO_GLOBAL[model_name]
    lfm_local = LFM_RANDOM if tcu else MAP_MODEL_NAME_TO_GLOBAL[model_name]
    return lfm_global, lfm_local

def translate_local_global_to_model(
        lfm_local: str, lfm_global: str) -> Tuple[bool, str]:
    """Translate the local and global terminology to the model name and the triadic closure uniformity."""
    assert lfm_local in (LFM_RANDOM, lfm_global),\
        f"Local must be `{LFM_RANDOM}` or the same as global=`{lfm_global}`."

    model_name = MAP_GLOBAL_TO_MODEL_NAME[lfm_global]
    tcu = lfm_local == LFM_RANDOM
    return tcu, model_name

def create_file_name(
        N: int,
        m: int,
        minority_fraction: float,
        homophily: float,
        triadic_closure: float,
        lfm_local: str,
        lfm_global: str,
        realization: int,
        prefix: str = "",
        suffix: str = "",
        file_ending: str = ".json") -> str:
    """Creates and returns a filename string describing the configuration given by the parameters.
    This is useful for centralizing I/O operations under a unified terminology.

    Args:
        N (int): Number of nodes
        m (int): Number of new edges per node
        minority_fraction (float): Minority fraction f in the network
        homophily (float): Homophily h
        triadic_closure (float): Probability to draw triadic closure edges
        lfm_global (str): Global link formation mechanism
        lfm_local (str): Local link formation mechanism
        realization (int): Simulation realization
        prefix (str, optional): Set if a prefix should be added to the string. Defaults to "".
        suffix (str, optional): Set if a suffix should be added to the string. Defaults to "".
        file_ending (str, optional): The file ending. Defaults to ".json".

    Returns:
        str: The filename string.
    """
    return (
        f"{prefix}"
        f"N-{N}_m-{m}_f-{minority_fraction}_"
        f"h-{homophily}_tc-{triadic_closure}_"
        f"lfm-l-{lfm_local}_lfm-g-{lfm_global}_"
        f"r-{realization}{suffix}{file_ending}"
    )
