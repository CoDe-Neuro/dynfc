from numpy import mean, std, sum, zeros, arange
from .butter_bandpass_filter import butter_bandpass_filter
from .doHilbert import doHilbert
from .dPL import dPL

def z_corr(iseries, jseries):
    zi = (iseries - mean(iseries))/std(iseries)
    zj = (jseries - mean(jseries))/std(jseries)

    return sum(zi*zj)/(zi.size - 1)

def cofluct(RSsig):
    r"""Run LEiDA Routine for BOLD signal.

    Parameters
    ----------
    RSsig : ndarray
        BOLD signal array for all parcels/voxels in the format [N, Tmax, Subs].

    Returns
    -------
    Phases : ndarray
        Phases array for all parcels/voxels in the format [N, Tmax, Subs].
    syncConn : ndarray
        Synchronicity matrix for all parcels/voxels in the format [N, N, Tmax, Subs].
    leidaArray : ndarray
        Leading eigenvector of synchornicity matrix [Tmax, N, Subs].

    References
    ----------

    .. [1] 
    Lord et al,. (2019). Dynamical exploration of the 
    repertoire of brain networks at rest is 
    modulated by psilocybin. NeuroImage, 199(April), 127–142. 
    https://doi.org/10.1016/j.neuroimage.2019.05.060

    """

    Tmax = RSsig.shape[0]
    N = RSsig.shape[1]
    nSub = RSsig.shape[2]

    T = arange(10, Tmax - 10)

    cofl = zeros([N, N, Tmax - 20, nSub])

    flp = .04              # lowpass frequency of filter
    fhi = .07              # highpass
    npts = Tmax            # total nb of points
    delt = 2               # sampling interval
    k = 2                  # 2nd order butterworth filter

    for pat in range(nSub):

        timeserie = zeros([N, Tmax])
        signal = RSsig[:, :, pat].transpose()

        for seed in range(N):
            timeserie[seed, :] = butter_bandpass_filter(signal[seed, :],
                                                    flp, fhi, delt, k)
        print('Signal filtered.')

        for j in range(0, N):
            
            for k in range(0, j + 1):

                cofl[j, k, pat] = z_corr(timeserie[j, T], timeserie[k, T])
                cofl[k, j, pat] = cofl[j, k, pat]

        print('Matrices obtained.')
        print('Routine finished for patient no. ' + str(pat + 1) + '.')
    
    return cofl