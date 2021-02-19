from scipy.signal import hilbert
from numpy import zeros, angle


def doHilbert(N, Tmax, timeseries):
    """Hilbert transform of BOLD signal form all parcels/voxels.

    This fuction returns the phase time series for all parcels/voxels
    of the input.

    Args:
        N (int): Number of parcels/voxels of the input array.
        Tmax (int): BOLD signal samples count.
        timeseries (double): Bold signal array for all parcels/voxels in the format [N, Tmax].

    Returns:
        PhasesAux : Phases array for all parcels/voxels in the format [N, Tmax].
    
    """

    PhasesAux = zeros([N, Tmax])

    for seed in range(0, N):
        Xanalytic = hilbert(timeseries[seed, :] - timeseries[seed, :].mean())
        PhasesAux[seed, :] = angle(Xanalytic)
    
    
    return PhasesAux