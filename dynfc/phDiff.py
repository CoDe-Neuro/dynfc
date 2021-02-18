from numpy import cos

def phDiff(a, b):
    """Cosine of phase difference.

    This function estimates the phase difference of the two entries and its cosine.

    $$PL = \cos{(a - b)}$$

    Args:
        a (double): Phase 1 in pi rad.
        b (double): Phase 2 in pi rad.

    Returns:
        out (double): Cosine of phase difference.

    Example:
            >>> import numpy as np
            >>> a = np.pi
            >>> b = - np.pi
            >>> print(phDiff(a,b))
            1.0

    References
    ----------

    .. [1] 
    Lord et al,. (2019). Dynamical exploration of the 
    repertoire of brain networks at rest is 
    modulated by psilocybin. NeuroImage, 199(April), 127–142. 
    https://doi.org/10.1016/j.neuroimage.2019.05.060

    """

    c = cos(a - b)
    return c
