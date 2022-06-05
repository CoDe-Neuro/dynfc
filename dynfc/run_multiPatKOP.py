from numpy import zeros
from .butter_bandpass_filter import butter_bandpass_filter
from .doKuramoto import doKuramoto
from .doHilbert import doHilbert


def run_multiPatKOP(RSsig, base=2, nBits=8, delt, flp=.04, fhi=.07, k=2):
    """Run KOP Routine for BOLD signal.

    Args:
        RSsig (ndarray): BOLD signal array for all parcels/voxels in the format [N, Tmax, Subs].
        delt: TR sample.
        flp: low threshold frequency of filter
        fhi: high threshold frequency of filter
        k: filter order

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
    shEntropy = zeros([nSub])
    phases = zeros([N, Tmax, nSub])
    sync = zeros([Tmax - 20, nSub])

    #flp = .04              # lowpass frequency of filter
    #fhi = .07              # highpass
    npts = Tmax            # total nb of points
    #delt = 2               # sampling interval
    #k = 2                  # 2nd order butterworth filter

    for pat in range(nSub):

        timeserie = zeros([N, Tmax])
        signal = RSsig[:, :, pat].transpose()

        for seed in range(N):
            timeserie[seed, :] = butter_bandpass_filter(signal[seed, :],
                                                        flp, fhi, delt, k)
        print('Signal filtered.')
        phases[:, :, pat] = doHilbert(N, Tmax, timeserie)

        print('Phases obtained.')
        metastabAux, syncAux, shEntropyAux = doKuramoto(
            N, Tmax, phases[:, :, pat], base, nBits)
        sync[:, pat] = syncAux[:,0]
        metastab[pat] = metastabAux
        shEntropy[pat] = shEntropyAux

        print('Matrices obtained.')
        print('Routine finished for patient no. ' + str(pat + 1) + '.')

    return metastab, sync, shEntropy
