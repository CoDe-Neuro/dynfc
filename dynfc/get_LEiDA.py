from scipy.linalg import eigh
from numpy import zeros


def get_LEiDA(syncConnAux):
    """Obtain leading eigenvector for synchronicity matrices.

    Args:
        syncConnAux (ndarray): Synchronicty matrices for all parcels/voxels in the format [N, N, Tmax].

    Returns:
        leidaArrayAux : Leading eigenvector of synchornicity matrix [Tmax, N].

    References
    ----------

    .. [1] 
    Cabral, J. et al. (2017). ‘Cognitive performance in healthy 
    older adults relates to spontaneous switching between states 
    of functional connectivity during rest’, Scientific Reports. 
    Nature Publishing Group, 7(1), p. 5135. 
    doi: 10.1038/s41598-017-05425-7.

    .. [2] 
    Lord et al,. (2019). Dynamical exploration of the 
    repertoire of brain networks at rest is 
    modulated by psilocybin. NeuroImage, 199(April), 127–142. 
    https://doi.org/10.1016/j.neuroimage.2019.05.060

    """

    tPoints = syncConnAux.shape[2]

    leidaArrayAux = zeros([tPoints,  syncConnAux.shape[0]])

    for i in range(tPoints):

        matrix = syncConnAux[:, :, i]
        D, V = eigh(matrix)
        V1 = V[:, -1]
            
        if sum(V1) > 0:
            V1 = -V1

        leidaArrayAux[i, :] = V1

    return leidaArrayAux
