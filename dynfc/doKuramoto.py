from dynfc import getEntropy
from numpy import zeros, sin, cos, std, arange



def doKuramoto(N, Tmax, phases, base = 2, nBits = 8):
    """Dynamic Phase-Locking.

    This fuction returns the dynamic Phase-Locking for all parcels/voxels
    of the input.

    Args:
        N (int): Number of parcels/voxels of the input array.
        Tmax (int): BOLD signal samples count.
        phases (ndarray): Phases signal array for all parcels/voxels in the format [N, Tmax].
        base (double, optional): Base for obtaining Shannon entropy.
        nBits (int, optional): n

    Return:
        tuple:
            syncAux : Synchronicity matrix for all parcels/voxels in the format [N, N], 
            metastabAux : Metastability index - Standard deviation of Kuramoto Parameter

    References
    ----------

    .. [1] 
    

    """

    T = arange(10, Tmax - 10)

    syncAux = zeros([len(T), 1])

    for t in range(0, len(T)):

        ku = sum(cos(phases[:, T[t]]) + 1j * sin(phases[:, T[t]])) / N
        syncAux[t] = abs(ku)

    metastabAux = std(syncAux)
    shEntropy = getEntropy(syncAux, base, nBits)

    return metastabAux, syncAux, shEntropy
