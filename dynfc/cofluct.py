import dynfc as dyn
from numpy import zeros, triu_indices, sqrt, sum, square, multiply
from scipy.stats import zscore
import numpy as np


def cofluct(series, size, k=1):
    """Run cofluctuation analysis for BOLD signal.

    Args: 
        RSsig (ndarray): BOLD signal array for all parcels/voxels in the format [N, Tmax].

    Returns:
        cofl (ndarray): Cofluctuation matrix for all parcels/voxels in the format [N, N].

    References
    ----------

    .. [1] 
    Esfahlani, F. Z. et al. (2020) ‘High-amplitude cofluctuations in cortical activity drive 
    functional connectivity’, Proceedings of the National Academy of Sciences of the United 
    States of America, 117(45), pp. 28393–28401. doi: 10.1073/pnas.2005531117.

    .. [2]
    Faskowitz, J. et al. (2020) ‘Edge-centric functional network representations of human 
    cerebral cortex reveal overlapping system-level architecture’, Nature Neuroscience. 
    Springer US, 23(12), pp. 1644–1654. doi: 10.1038/s41593-020-00719-y.
    
    """
    corr_mats, idx = dyn.corr_slide(series, size)
    edges_series = zeros((len(triu_indices(corr_mats.shape[0], k)[0]),
    corr_mats.shape[2]))

    ts_z = zscore(series, axis=1, ddof=1)
    upt = np.triu_indices(ts_z.shape[0], k)

    edges_series = multiply(ts_z[upt[0], ], ts_z[upt[1], ])

    rss = sqrt(np.sum(square(edges_series), axis=0))

    return edges_series, corr_mats, rss
