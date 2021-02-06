import dynfc as dyn
from numpy import pi, load, hstack

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


def test_corr_slide():

    ts = load('data/ts.npy')
    corr_mats = dyn.corr_slide(ts, ts.shape[1])
    fc = load('data/fc.npy')

    assert round(sum(sum(fc - corr_mats[:,:,0]))) == 0


def test_corr_slide2():

    ts = load('data/ts.npy')
    ts2 = hstack((ts, ts))
    corr_mats = dyn.corr_slide(ts2, ts.shape[1])
    fc = load('data/fc.npy')

    assert round(
        sum(sum(fc - corr_mats[:, :, 0])) + 
        sum(sum(fc - corr_mats[:, :, 1]))) == 0


def test_get_edgests():
    size = 12
    ts = load('data/ts.npy')
    edges_series, rss = dyn.get_edgests(ts, size)

    num = int(ts.shape[1]/size)

    assert rss.shape[0] == num
