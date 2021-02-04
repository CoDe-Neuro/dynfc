from numpy import zeros, corrcoef

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

    for w in range(4):      
        corr_mats[:,:,w] = corrcoef(series[:, 0 + w*size : size + w*size])
        
    
    return corr_mats
