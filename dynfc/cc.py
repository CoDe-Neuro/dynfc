from numpy import zeros, corrcoef
import dynfc as dyn

def corr_slide(series, size):
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
    dim = series.shape
    windowCount = dim[1]//size
    corr_mats = zeros((dim[0],dim[0],windowCount))

    for w in range(windowCount):
        corr_mats[:,:,w] = corrcoef(series[:, 0 + w*size : size + w*size])
        
    
    return corr_mats

def cc(series, size, k = 1):

    edges_series, rss = dyn.get_edgests(series, size, k)
    corrcorr = corrcoef(edges_series, rowvar = False)

    return corrcorr
