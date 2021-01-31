from numpy import mean, std, sum, zeros, arange
from .butter_bandpass_filter import butter_bandpass_filter

def z_corr(iseries, jseries):
    zi = (iseries - mean(iseries))/std(iseries)
    zj = (jseries - mean(jseries))/std(jseries)

    return sum(zi*zj)/(zi.size - 1)

def cofluct(RSsig):
    r"""Run cofluctuation analysis for BOLD signal.

    Parameters
    ----------
    RSsig : ndarray
        BOLD signal array for all parcels/voxels in the format [N, Tmax, Subs].

    Returns
    -------
    cofl : ndarray
        Cofluctuation matrix for all parcels/voxels in the format [N, N, Tmax, Subs].

    References
    ----------

    .. [1] 
    Esfahlani, F. Z. et al. (2019) ‘High-amplitude co-fluctuations in cortical activity drive 
    functional connectivity’, bioRxiv. Cold Spring Harbor Laboratory, p. 800045. 
    doi: 10.1101/800045.

    .. [2]
    Faskowitz, J. et al. (2020) ‘Edge-centric functional network representations of human 
    cerebral cortex reveal overlapping system-level architecture’, Nature Neuroscience. 
    Springer US, 23(12), pp. 1644–1654. doi: 10.1038/s41593-020-00719-y.

    .. [3]
    Esfahlani, F. Z. et al. (2020) ‘High-amplitude cofluctuations in cortical activity drive 
    functional connectivity’, Proceedings of the National Academy of Sciences of the United 
    States of America, 117(45), pp. 28393–28401. doi: 10.1073/pnas.2005531117.

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