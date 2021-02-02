from numpy import zeros
from .butter_bandpass_filter import butter_bandpass_filter
from .doKuramoto import doKuramoto
from .doHilbert import doHilbert
from .dPL import dPL
from .cofluct import cofluct



def run_multiPat(RSsig):
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

    leidaArray = zeros([Tmax - 20, N, nSub])
    syncConn = zeros([N, N, Tmax - 20, nSub])
    Phases = zeros([N, Tmax, nSub])

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
        Phases[:, :, pat] = doHilbert(N, Tmax, timeserie)

        print('Phases obtained.')
        syncConnAux, leidaArrayAux = dPL(N, Tmax, Phases[:, :, pat])
        syncConn[:, :, :, pat] = syncConnAux
        leidaArray[:, :, pat] = leidaArrayAux

        print('Matrices obtained.')
        print('Routine finished for patient no. ' + str(pat + 1) + '.')
    
    return Phases, syncConn, leidaArray


def run_multiPatKuramoto(RSsig):
    r"""Run LEiDA Routine for BOLD signal.

    Parameters
    ----------
    RSsig : ndarray
        BOLD signal array for all parcels/voxels in the format [N, Tmax, Subs].

    Returns
    -------
    Phases : ndarray
        Phases array for all parcels/voxels in the format [N, Tmax, Subs].
    sync : ndarray
        Synchronicity matrix for all parcels/voxels in the format [Tmax, Subs].
    metastab : ndarray
        Leading eigenvector of synchornicity matrix [Subs].

    References
    ----------

    .. [1] 
    

    """

    Tmax = RSsig.shape[0]
    N = RSsig.shape[1]
    nSub = RSsig.shape[2]

    metastab = zeros([nSub])
    Phases = zeros([N, Tmax, nSub])
    sync = zeros([Tmax - 20, nSub])

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
        Phases[:, :, pat] = doHilbert(N, Tmax, timeserie)

        print('Phases obtained.')
        metastabAux, syncAux = doKuramoto(N, Tmax, Phases[:, :, pat])
        sync[:, pat] = syncAux[:,0]
        metastab[pat] = metastabAux

        print('Matrices obtained.')
        print('Routine finished for patient no. ' + str(pat + 1) + '.')

    return Phases, sync, metastab


def run_multiPatcofluct(RSsig):
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
    Esfahlani, F. Z. et al. (2020) ‘High-amplitude cofluctuations in cortical activity drive 
    functional connectivity’, Proceedings of the National Academy of Sciences of the United 
    States of America, 117(45), pp. 28393–28401. doi: 10.1073/pnas.2005531117.

    .. [2]
    Faskowitz, J. et al. (2020) ‘Edge-centric functional network representations of human 
    cerebral cortex reveal overlapping system-level architecture’, Nature Neuroscience. 
    Springer US, 23(12), pp. 1644–1654. doi: 10.1038/s41593-020-00719-y.
    

    """

    Tmax = RSsig.shape[0]
    N = RSsig.shape[1]
    nSub = RSsig.shape[2]

    T = arange(10, Tmax - 10)

    cofl = zeros([N, N, Tmax - 20, nSub])

    flp = .04              # lowpass frequency of filter
    fhi = .07              # highpass
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

                cofl[j, k, pat] = cofluct(timeserie[j, T], timeserie[k, T])
                cofl[k, j, pat] = cofl[j, k, pat]

        print('Matrices obtained.')
        print('Routine finished for patient no. ' + str(pat + 1) + '.')

    return cofl
