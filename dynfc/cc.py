from numpy import corrcoef
import dynfc as dyn

def cc(series, size, k = 1):
    """Run cofluctuation analysis for BOLD signal.

    Args:
        series (double): BOLD signal array for all parcels/voxels in the format [N, Tmax].
        size (int): Size of window.
        k (int, optional): Standard value k = 1.

    Returns:
        double: Correlation of correlation matrix for all timepoints [timepoints/size, timepoints/size].

    References
    ----------

    .. [1] 
    Hansen, E. C. A. et al. (2015) ‘Functional connectivity dynamics: 
    Modeling the switching behavior of the resting state’, NeuroImage. 
    105, pp. 525–535. 
    doi: 10.1016/j.neuroimage.2014.11.001.
    
    """

    edges_series, rss = dyn.get_edgests(series, size, k)
    corrcorr = corrcoef(edges_series, rowvar = False)

    return corrcorr
