from numpy import zeros
from matplotlib.pyplot import figure, savefig, close
from seaborn import heatmap



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

def doFigures(syncConnAux):

    for i in range(0, syncConnAux.shape[2]):
        figure(figsize = (4, 3), dpi = 150)
        corr = syncConnAux[:, :, i]
        ax = heatmap(
            corr,
            vmin = 0, 
            vmax = 1, 
            center = 0.5,
            cmap = "viridis",
            cbar_kws = {"orientation": "vertical"}
        )

        ax.set_xticklabels(
            ax.get_xticklabels(),
            rotation = 45,
            horizontalalignment = 'right'
        )
        savefig("out/output_"+str(i)+".png")
        close()
