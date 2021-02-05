import dynfc as dyn
from numpy import pi, load

def test_phDiff1():
    assert round(dyn.phDiff(pi, pi),1) == 1

def test_phDiff2():
    assert round(dyn.phDiff(pi, pi/2), 1) == 0

def test_phDiff3():
    assert round(dyn.phDiff(pi, 0),1) == - 1

def test_cofluct():

    ts = load('data/ts.npy')
    cofl = dyn.cofluct(ts)
    fc = load('data/fc.npy')

    assert round(sum(sum(fc - cofl))) == 0
