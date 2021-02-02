from numpy import mean, std, sum, zeros, arange
from .butter_bandpass_filter import butter_bandpass_filter

def cofluct(iseries, jseries):
    zi = (iseries - mean(iseries))/std(iseries)
    zj = (jseries - mean(jseries))/std(jseries)

    return sum(zi*zj)/(zi.size - 1)