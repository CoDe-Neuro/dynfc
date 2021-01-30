from numpy import cos

def phDiff(a, b):
    r"""Cosine of phase difference.

    This function estimates the phase difference of the two entries and its cosine.

    Parameters
    ----------
    a : double
        Phase 1.
    b : double
        Phase 2.

    Returns
    -------
    out : double
        Cosine of phase difference.

    References
    ----------

    .. [1] 
    Lord et al,. (2019). Dynamical exploration of the 
    repertoire of brain networks at rest is 
    modulated by psilocybin. NeuroImage, 199(April), 127–142. 
    https://doi.org/10.1016/j.neuroimage.2019.05.060

    Examples
    --------

    >>> import numpy as np
    >>> a = np.pi
    >>> b = - np.pi
    >>> print(phDiff(a,b))
    1.0
    """

    c = cos(a - b)
    return c