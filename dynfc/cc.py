from numpy import zeros, corrcoef, arange
import dynfc as dyn

def corr_slide(series, size, slide = None):
    r"""Run cofluctuation analysis for BOLD signal.

    Parameters
    ----------
    series : ndarray
        BOLD signal array for all parcels/voxels in the format [N, Tmax].

    Returns
    -------
    corr_mats : ndarray
        Cofluctuation matrix for all parcels/voxels in the format [N, N, window].

    References
    ----------

    .. [1] 
    Hansen, E. C. A. et al. (2015) ‘Functional connectivity dynamics: Modeling the switching 
    behavior of the resting state’, NeuroImage. The Authors, 105, pp. 525–535. 
    doi: 10.1016/j.neuroimage.2014.11.001.
    

    """
    if slide == None:
        slide = size

    idx = arange(0, series.shape[1], slide)
    corr_mats = zeros((series.shape[0], series.shape[0], idx.shape[0]))

    for w in range(idx.shape[0]):
        corr_mats[:, :, w] = corrcoef(series[:, 0 + idx[w]: size + idx[w]])
        
    return corr_mats, idx

def cc(series, size, k = 1):

    edges_series, rss = dyn.get_edgests(series, size, k)
    corrcorr = corrcoef(edges_series, rowvar = False)

    return corrcorr
