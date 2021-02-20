# CoDe-Neuro's Dynamic Functional Connectivity Tools
[![Python package](https://github.com/CoDe-Neuro/dynfc/actions/workflows/python-package.yml/badge.svg)](https://github.com/CoDe-Neuro/dynfc/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/CoDe-Neuro/dynfc/branch/main/graph/badge.svg?token=EB7Z9AWZVN)](https://codecov.io/gh/CoDe-Neuro/dynfc) 
![GitHub](https://img.shields.io/github/license/CoDe-Neuro/dynfc)
[![Website](https://img.shields.io/badge/repo-Readme-2196F3)](https://github.com/CoDe-Neuro/dynfc)
[![DOI](https://zenodo.org/badge/334302177.svg)](https://zenodo.org/badge/latestdoi/334302177)
![PyPI](https://img.shields.io/pypi/v/dynfc?color=purple)

This is the documentation page for 'dynfc', a Python module consisting of a set of tools developed to infer connectivity from fMRI (BOLD) signals. The module contains both phase-lock and correlation (+ cofluctuation) methods. Please be aware that this is still a develepment version and so may contain bugs and limited functionalities.

If you have any questions or suggestions, please [open an issue](https://github.com/CoDe-Neuro/dynfc/issues). 

Please do not hesitate to suggest improvements to this module.


## Built on

[Numpy](https://numpy.org)            |  [Scipy](https://www.scipy.org)
:-------------------------:|:-------------------------:
<img src="https://www.scipy.org/_static/images/numpylogoicon.png" width="100">  |  <img src=https://docs.scipy.org/doc/scipy-0.11.0/reference/_static/scipyshiny_small.png width="100">

## Project layout

    setup.py    
    dynfc/
        __init__.py
        ...       # Python script files  
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
    tests/        # Tests folder
        __init__.py
        test_functions.py


## Funding

<img src="https://upload.wikimedia.org/wikipedia/commons/5/58/Wellcome_Trust_logo.svg" width="300">

This project is funded by a Wellcome Trust Seed Award in Science [[217316/Z/19/Z]](https://europepmc.org/grantfinder/grantdetails?query=pi%3A%22Batalle%2BD%22%2Bgid%3A%22217316%22%2Bga%3A%22Wellcome%20Trust%22).