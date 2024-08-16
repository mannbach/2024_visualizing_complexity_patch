from typing import Tuple, Optional

from netin import PATCH, TCH, ERPATCH, Graph
from netin.utils.constants import ERPATCH_MODEL_NAME, TCH_MODEL_NAME

from .constants import MAP_MODEL_NAME_TO_GLOBAL, MAP_GLOBAL_TO_MODEL_NAME, LFM_RANDOM

def create_graph(
        N: int, m: int, f_m: float,
        h: float, tc: float,
        lfm_global: str, lfm_local: str,
        seed: Optional[int]=None) -> Graph:
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

def translate_model_to_local_global(
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
    assert lfm_local in (LFM_RANDOM, lfm_global),\
        f"Local must be `{LFM_RANDOM}` or the same as global=`{lfm_global}`."

    model_name = MAP_GLOBAL_TO_MODEL_NAME[lfm_global]
    tcu = lfm_local == LFM_RANDOM
    return tcu, model_name
