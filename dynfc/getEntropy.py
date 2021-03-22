# Based on solution at https://gist.github.com/jaradc/eeddf20932c0347928d0da5a09298147

from numpy import unique, multiply
from numpy.core.fromnumeric import round_ 
from scipy.stats import entropy

def getEntropy(series, base = 2, nBits = None):
    """Obtain Shannon Entropy estimate from a vector values/time series.

    Args:
        series (ndarray): Phases signal array for all parcels/voxels in the format [N, Tmax].
        base (double, optional): Base of logarithm for Shannon entropy expression. Standard value is 2.

    Return:
        double: Shannon entropy.

    References
    ----------

    .. [1] 
    

    """

    if nBits != None:
        series = round_(multiply(series, 2 ** nBits))

    mags, probs = unique(series, 
                         return_counts=True)
    entr = entropy(probs, base=base)

    return entr

