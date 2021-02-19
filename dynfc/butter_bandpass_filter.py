from scipy.signal import filtfilt
from .butter_design import butter_design

def butter_bandpass_filter(x, flp, fhi, delt, order):
    """Butterworth filter design.

    Args:
        x (array_like): Signal to be filtered.
        flp (float): Low-pass frequency.
        fhi (float): High-pass frequency.
        delt (int): Sampling interval.
        order (int): Filter order.

    Returns:
        double: Filtered signal.
    """

    b, a = butter_design(flp, fhi, delt, order)
    y = filtfilt(b, a, x)

    return y