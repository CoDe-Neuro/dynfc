import dynfc as dyn
from numpy import pi, zeros
from numpy.random import rand, seed
import scipy as sc
from scipy.io import loadmat

def test_phDiff1():
    assert round(dyn.phDiff(pi, pi),1) == 1

def test_phDiff2():
    assert round(dyn.phDiff(pi, pi/2), 1) == 0

def test_phDiff3():
    assert round(dyn.phDiff(pi, 0),1) == - 1

def test_cofluct():

    ts = loadmat('data/ts.mat')['ts']
    ts = ts.transpose()
    cofl = dyn.cofluct(ts)
    fc = loadmat('data/fc.mat')['fc']

    assert round(sum(sum(fc - cofl))) == 0
