import dynfc as dyn
from numpy import pi
from numpy.random import rand, seed

def test_phDiff1():
    assert round(dyn.phDiff(pi, pi),1) == 1

def test_phDiff2():
    assert round(dyn.phDiff(pi, pi/2), 1) == 0

def test_phDiff3():
    assert round(dyn.phDiff(pi, 0),1) == - 1

def test_cofluct1():
    seed(42)
    rand_vec = rand(1, 1024)
    assert round(dyn.cofluct(rand_vec, rand_vec)) == 1

def test_cofluct2():
    seed(42)
    rand_vec = rand(1, 1024)
    assert round(dyn.cofluct(rand_vec, -rand_vec)) == -1
