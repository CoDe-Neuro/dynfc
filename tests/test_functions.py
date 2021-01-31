import dynfc as dyn
from numpy import pi

def test_phDiff():
    assert dyn.phDiff(pi, pi) == 1
    #assert dyn.phDiff(pi, pi/2) == 0 
    #assert dyn.phDiff(pi, 0) == - 1
