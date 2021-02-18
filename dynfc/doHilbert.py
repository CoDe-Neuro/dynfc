from scipy.signal import hilbert
from numpy import zeros, angle


def doHilbert(N, Tmax, timeserie):
    """Hilbert transform of BOLD signal form all parcels/voxels.

    This fuction returns the phase time series for all parcels/voxels
    of the input.

    Args: 
        N (int): Number of parcels/voxels of the input array.
        Tmax (int): BOLD signal samples count.
        timeseries (ndarray): Bold signal array for all parcels/voxels in the format [N, Tmax].

    Returns:
        PhasesAux (ndarray): Phases array for all parcels/voxels in the format [N, Tmax].
    """

    PhasesAux = zeros([N, Tmax])

    for seed in range(0, N):
        Xanalytic = hilbert(timeserie[seed, :] - timeserie[seed, :].mean())
        PhasesAux[seed, :] = angle(Xanalytic)
    
    
    return PhasesAux