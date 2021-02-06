import dynfc as dyn
from numpy import zeros, corrcoef, triu_indices, sqrt, sum, square
import numpy as np


def cofluct(RSsig):
    r"""Run cofluctuation analysis for BOLD signal.

    Parameters
    ----------
    RSsig : ndarray
        BOLD signal array for all parcels/voxels in the format [N, Tmax].

    Returns
    -------
    cofl : ndarray
        Cofluctuation matrix for all parcels/voxels in the format [N, N].

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

    N = RSsig.shape[0]

    cofl = zeros([N, N])
    cofl = corrcoef(RSsig)

    print('Matrices obtained.')

    return cofl

def get_edgests(RSsig, size):
    corr_mats = dyn.corr_slide(RSsig, size)
    edges_series = zeros((corr_mats.shape[0]*(corr_mats.shape[0] - 1)//2 + 
    corr_mats.shape[0], corr_mats.shape[2]))

    for i in range(corr_mats.shape[2]):
        mat = corr_mats[:, :, i]
        upt = triu_indices(mat.shape[0])
        vec_mat = mat[upt]

        edges_series[:, i] = vec_mat
    
    rss = sqrt(np.sum(square(corr_mats), axis = 0))

    return edges_series, rss
