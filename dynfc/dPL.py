from numpy import zeros, arange


def dPL(N, Tmax, Phases):
    r"""Dynamic Phase-Locking.

    This fuction returns the dynamic Phase-Locking for all parcels/voxels
    of the input.

    Parameters
    ----------
    N : int
        Number of parcels/voxels of the input array.
    Tmax : int
        BOLD signal samples count.
    Phases: ndarray
        Phases signal array for all parcels/voxels in the format [N, Tmax].

    Returns
    -------
    syncConnAux : ndarray
        Synchronicity matrix for all parcels/voxels in the format [N, N].
    leidaArrayAux : ndarray
        Leading eigenvector of synchornicity matrix [Tmax, N].

    References
    ----------

    .. [1] 
    Lord et al,. (2019). Dynamical exploration of the 
    repertoire of brain networks at rest is 
    modulated by psilocybin. NeuroImage, 199(April), 127–142. 
    https://doi.org/10.1016/j.neuroimage.2019.05.060

    """

    T = arange(10, Tmax - 10)

    syncConnAux = zeros([N, N, Tmax-20])
    syncAux = zeros([len(T), 1])

    for t in range(0, len(T)):

        for j in range(0, N):
            
            for k in range(0, j + 1):

                syncConnAux[j, k, t] = phDiff(Phases[j, T[t]],
                                                       Phases[k, T[t]])
                syncConnAux[k, j, t] = syncConnAux[j, k, t]
    
    leidaArrayAux = get_LEiDA(syncConnAux)

    return syncConnAux, leidaArrayAux