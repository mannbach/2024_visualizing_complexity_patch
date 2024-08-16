from netin.utils.constants import ERPATCH_MODEL_NAME, TCH_MODEL_NAME, PATCH_MODEL_NAME

# Package specific constants
LFM_RANDOM = "random"
LFM_HOMOPHILY = "homophily"
LFM_PAH = "pah"
TPL_LFM = (LFM_RANDOM, LFM_HOMOPHILY, LFM_PAH)

MAP_LFM_SHORT = {
    LFM_RANDOM: "R",
    LFM_HOMOPHILY: "H",
    LFM_PAH: "PAH",
}

# Translations from netin package
MAP_MODEL_NAME_TO_GLOBAL = {
    ERPATCH_MODEL_NAME: LFM_RANDOM,
    TCH_MODEL_NAME: LFM_HOMOPHILY,
    PATCH_MODEL_NAME: LFM_PAH
}
MAP_GLOBAL_TO_MODEL_NAME = {v: k for k, v in MAP_MODEL_NAME_TO_GLOBAL.items()}
