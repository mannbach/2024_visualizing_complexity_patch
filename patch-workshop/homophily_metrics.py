from typing import Set, Tuple

import networkx as nx

def compute_ei_index(net: nx.Graph, nodes_min: Set[int]) -> Tuple[float, float]:
    cnt_mM, cnt_mm, cnt_MM = 0, 0, 0

    for u,v in net.edges():
        u_min, v_min = u in nodes_min, v in nodes_min
        if u_min and v_min:
            cnt_mm += 1
        elif u_min != v_min: # XOR
            cnt_mM += 1
        elif not (u_min or v_min): # both maj
            cnt_MM += 1
    cnt_h = cnt_mm + cnt_MM
    return (cnt_mM - cnt_mm) / (cnt_mM + cnt_mm),\
        (cnt_mM - cnt_MM) / (cnt_mM + cnt_MM),\
        (cnt_mM - cnt_h) / (cnt_mM + cnt_h)
