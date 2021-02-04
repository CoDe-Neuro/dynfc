from .dynfc import run_multiPat
from .dynfc import run_multiPatKuramoto
from .doKuramoto import doKuramoto
from .get_LEiDA import get_LEiDA
from .butter_bandpass_filter import butter_bandpass_filter
from .butter_design import butter_design
from .doEuclid import doEuclid
from .doHilbert import doHilbert
from .dPL import dPL
from .phDiff import phDiff
from .cofluct import cofluct
from .cc import corr_slide

__all__ = [
    'run_multiPat', 
    'doKuramoto', 
    'get_LEiDA', 
    'dPL', 
    'doHilbert', 
    'phDiff', 
    'butter_design', 
    'doEuclid', 
    'cofluct', 
    'phDiff', 
    'z_corr']