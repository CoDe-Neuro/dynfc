from scipy.signal import butter

def butter_design(flp, fhi, delt, order):
    """Butterworth filter design.

    Args:
        flp (float): Low-pass frequency.
        fhi (float): High-pass frequency.
        delt (int): Sampling interval.
        order (int): Filter order.

    Returns:
        b,a (ndarray): Filter design.
    """

    fnq = 1 / (2 * delt)       # Nyquist frequency
    low = flp / fnq
    high = fhi / fnq
    b, a = butter(order, [low, high], btype='bandpass')
    return b, a