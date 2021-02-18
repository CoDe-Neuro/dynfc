from scipy.spatial import distance
from numpy import zeros



def doEuclid(PCs):
    """Obtain Euclidean distance to the previous points.

    Args: 
    PCs (ndarray): PCs array in the format [Subs * Tmax, n PCs].

    Returns: 
    d (ndarray): Euclidean distances in the format [1, Subs * Tmax].

    """

    d = zeros(PCs.shape[0])

    for i in range(1, PCs.shape[0]):

        d[i] = distance.euclidean(PCs[i - 1, ], PCs[i, ])

    return d