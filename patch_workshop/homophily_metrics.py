from typing import Set, Tuple

import networkx as nx

def compute_ei_index(net: nx.Graph, nodes_min: Set[int]) -> Tuple[float, float]:
    """Compute the EI index of the network as a measure of network segregation.

    Parameters
    ----------
    net : nx.Graph
        The simulated network.
    nodes_min : Set[int]
        A set of the minority nodes.

    Returns
    -------
    Tuple[float, float]
        The EI-index where values close to 1 indicate a network in which nodes of one
        group prefer to connect to the other groups.
        Values close to -1 indicate segregation, as nodes prefer to connect their own group.
    """
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
    return (cnt_mM - cnt_h) / (cnt_mM + cnt_h)
