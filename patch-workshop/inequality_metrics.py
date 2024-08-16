from typing import Set, Tuple

from scipy import stats
import numpy as np
import networkx as nx

def CL_delta_groups_1v1(x_lst):
    """
    Pairwise differences
    """
    CL_delta_ij = np.zeros((len(x_lst), len(x_lst))) + np.nan
    for i, xi in enumerate(x_lst):
        for j, xj in enumerate(x_lst):
            CL_delta_ij[i,j] = common_language_delta(xi,xj)
    return CL_delta_ij

def CL_delta_groups_1vRest(x_lst):
    """
    Stochastic homogeneity (p.22 of doi:10.2307/1165329)
    Statistical disparity measure for N groups with each group represented by
    a list of elements containing the wealth of each individual.

    Paramteres
    ----------
    x_lst: list
        List of lists, where each list contains the wealth of the individuals
        of a group.

    Returns
    -------
    result: numpy.ndarray
        Each element i of this array is the difference A-B computed as follows:
        Take two random individuals, one from group i and another from any of the
        other groups. A is the probability that the individual from i is wealthier
        than the individual from any of the other groups, and B is the probability
        that the individual from any of the other groups is welathier.
        So a positive value indicates that a given group is on average wealthier
        than any of the other groups and vice-versa.
    """
    CL_delta_i = np.zeros(len(x_lst)) + np.nan
    for i, xi in enumerate(x_lst):
        x_rest = []
        for j, xj in enumerate(x_lst):
            if i!=j:
                x_rest.extend(xj)
        CL_delta_i[i] = common_language_delta(xi,x_rest)
    return CL_delta_i

def common_language_delta(x,y):
    """
    doi: 10.2307/1165329
    """
    A12 = common_language_A12(x,y)
    return 2*A12 - 1

def common_language_A12(x,y):
    """
    doi: 10.2307/1165329
    See [1] for getting R1 from U1
    [1] https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test#Calculations
    """
    m = len(x)
    n = len(y)
    if m==0 or n==0:
        return np.nan
    res = stats.mannwhitneyu(x, y)
    U1 = res[0]
    R1 = U1 + 0.5*m*(m+1)
    A12 = (R1/m - (m+1)/2)/n
    return A12

#############################################################################
#############################################################################
## TESTS
#############################################################################
#############################################################################

#############################################################################
## A12
#############################################################################

def test_A12_p106_VarDel(size1=1000,size2=200):
    x_dom = [1,2,3]
    x1_p = [.1,.6,.3]
    x2_p = [.3,.6,.1]

    smpl1 = np.random.choice(x_dom,p=x1_p,size=size1)
    smpl2 = np.random.choice(x_dom,p=x2_p,size=size2)

    print("Should be ~.66: ", common_language_A12(smpl1,smpl2))
    print("Should be ~.32: ", common_language_delta(smpl1,smpl2))

def test_A12_p106_VarDel_randomized(size1=1000,size2=200):
    x_dom = [1,2,3]
    x1_p = np.random.random(size=3)
    x1_p = x1_p / np.sum(x1_p)
    x2_p = np.random.random(size=3)
    x2_p = x2_p / np.sum(x2_p)

    smpl1 = np.random.choice(x_dom,p=x1_p,size=size1)
    smpl2 = np.random.choice(x_dom,p=x2_p,size=size2)

    p_gr = x1_p[1]*x2_p[0] + x1_p[2]*x2_p[0] + x1_p[2]*x2_p[1]
    p_less = x2_p[1]*x1_p[0] + x2_p[2]*x1_p[0] + x2_p[2]*x1_p[1]
    p_eq = x2_p[0]*x1_p[0] + x2_p[1]*x1_p[1] + x2_p[2]*x1_p[2]

    print(f"Should be ~{p_gr+0.5*p_eq:.03f}: ", common_language_A12(smpl1,smpl2))
    print(f"Should be ~{p_gr-p_less:.03f}: ", common_language_delta(smpl1,smpl2))

def _get_degree_arrays(net: nx.Graph, minority_nodes: Set[int]) -> Tuple[np.ndarray, np.ndarray]:
    k_min, k_maj = [], []
    for node, deg in net.degree():
        if node in minority_nodes:
            k_min.append(deg)
        else:
            k_maj.append(deg)
    return (np.asarray(l_k) for l_k in (k_min, k_maj))

def compute_stoch_dom(net: nx.Graph, minority_nodes: Set[int]) -> float:
    k_min, k_maj = _get_degree_arrays(net, minority_nodes)
    s_dom = CL_delta_groups_1vRest([k_min, k_maj])
    return s_dom[0]

def compute_gini(net: nx.Graph):
    l_k = np.asarray([deg for _, deg in net.degree()])
    # The rest of the code requires numpy arrays.

    sorted_x = np.sort(l_k)
    n = len(l_k)
    cumx = np.cumsum(sorted_x, dtype=float)
    # The above formula, with all weights equal to 1 simplifies to:
    return (n + 1 - 2 * np.sum(cumx) / cumx[-1]) / n
