from numpy import corrcoef
import dynfc as dyn

def cc(series, size, k = 1):

    edges_series, rss = dyn.get_edgests(series, size, k)
    corrcorr = corrcoef(edges_series, rowvar = False)

    return corrcorr
