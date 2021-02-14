import dynfc as dyn
from numpy import pi, load, hstack

def test_phDiff1():
    assert round(dyn.phDiff(pi, pi),1) == 1

def test_phDiff2():
    assert round(dyn.phDiff(pi, pi/2), 1) == 0

def test_phDiff3():
    assert round(dyn.phDiff(pi, 0),1) == - 1


def test_corr_slide():

    ts = load('data/ts.npy')
    corr_mats, idx = dyn.corr_slide(ts, ts.shape[1])
    fc = load('data/fc.npy')

    assert round(sum(sum(fc - corr_mats[:,:,0]))) == 0


def test_corr_slide2():

    ts = load('data/ts.npy')
    ts2 = hstack((ts, ts))
    corr_mats, idx = dyn.corr_slide(ts2, ts.shape[1])
    fc = load('data/fc.npy')

    assert round(
        sum(sum(fc - corr_mats[:, :, 0])) + 
        sum(sum(fc - corr_mats[:, :, 1]))) == 0


def test_cofluct():
    size = 12
    ts = load('data/ts.npy')
    ets = load('data/ets.npy')

    edges_series, corr_mats, rss = dyn.cofluct(ts, size)

    assert round(sum(sum(edges_series - ets))) == 0


def test_cofluct2():
    size = 600
    ts = load('data/ts.npy')
    fc = load('data/fc.npy')

    edges_series, corr_mats, rss = dyn.cofluct(ts, size)

    assert round(sum(sum(corr_mats[:,:,0] - fc))) == 0

def test_cofluct3():
    size = 12
    ts = load('data/ts.npy')

    edges_series, corr_mats, rss = dyn.cofluct(ts, size)

    assert rss.shape[0] == ts.shape[1]
