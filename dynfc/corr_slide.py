from numpy import zeros, corrcoef, arange

def corr_slide(series, size, slide = None):
    """Run cofluctuation analysis for BOLD signal.

    Args:
        series (double): BOLD signal array for all parcels/voxels in the format [N, Tmax].
        size (int): Size of sliding window.
        slide (int, optional): Shift between windows. The standard value is the window size.
            Non-overlapping.

    Returns:
        double: Cofluctuation matrix for all parcels/voxels in the format [N, N, window].

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
