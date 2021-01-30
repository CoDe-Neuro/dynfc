from scipy.signal import filtfilt


def butter_bandpass_filter(x, flp, fhi, delt, order):
    r"""Butterworth filter design.

    Parameters
    ----------
    x : array_like
        Signal to be filtered.
    flp : float
        Low-pass frequency.
    fhi : float
        High-pass frequency.
    delt: int
        Sampling interval.
    order: int
        Filter order.

    Returns
    -------
    y : array_like
        Filtered signal.
    """

    b, a = butter_design(flp, fhi, delt, order)
    y = filtfilt(b, a, x)

    return y