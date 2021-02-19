from numpy import zeros
from .butter_bandpass_filter import butter_bandpass_filter
from .doKuramoto import doKuramoto
from .doHilbert import doHilbert
from .dPL import dPL



def run_multiPat(RSsig):
    """Run LEiDA Routine for BOLD signal.

    Args:
        RSsig (ndarray): BOLD signal array for all parcels/voxels in the format [N, Tmax, Subs].

    Returns:
        tuple:
            phase: Phases array for all parcels/voxels in the format,
            syncConn: Synchronicity matrix for all parcels/voxels in the format,
            leidaArray: Leading eigenvector of synchornicity matrix

    References
    ----------

    .. [1] 
    Cabral, J. et al. (2017) ‘Cognitive performance in healthy 
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

    Tmax = RSsig.shape[0]
    N = RSsig.shape[1]
    nSub = RSsig.shape[2]

    leidaArray = zeros([Tmax - 20, N, nSub])
    syncConn = zeros([N, N, Tmax - 20, nSub])
    phases = zeros([N, Tmax, nSub])

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
        phases[:, :, pat] = doHilbert(N, Tmax, timeserie)

        print('Phases obtained.')
        syncConnAux, leidaArrayAux = dPL(N, Tmax, phases[:, :, pat])
        syncConn[:, :, :, pat] = syncConnAux
        leidaArray[:, :, pat] = leidaArrayAux

        print('Matrices obtained.')
        print('Routine finished for patient no. ' + str(pat + 1) + '.')
    
    return phases, syncConn, leidaArray


def run_multiPatKuramoto(RSsig):
    """Run LEiDA Routine for BOLD signal.

    Args:
        RSsig (ndarray): BOLD signal array for all parcels/voxels in the format [N, Tmax, Subs].

    Returns:
        tuple:
            phases : Phases array for all parcels/voxels in the format [N, Tmax, Subs].
            sync : Synchronicity matrix for all parcels/voxels in the format [Tmax, Subs].
            metastab : Leading eigenvector of synchornicity matrix [Subs].
    
    
    References
    ----------

    .. [1] 
    

    """

    Tmax = RSsig.shape[0]
    N = RSsig.shape[1]
    nSub = RSsig.shape[2]

    metastab = zeros([nSub])
    phases = zeros([N, Tmax, nSub])
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
        phases[:, :, pat] = doHilbert(N, Tmax, timeserie)

        print('Phases obtained.')
        metastabAux, syncAux = doKuramoto(N, Tmax, phases[:, :, pat])
        sync[:, pat] = syncAux[:,0]
        metastab[pat] = metastabAux

        print('Matrices obtained.')
        print('Routine finished for patient no. ' + str(pat + 1) + '.')

    return phases, sync, metastab
