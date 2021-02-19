# CoDe-Neuro's Dynamic Functional Connectivity Tools
[![Python package](https://github.com/CoDe-Neuro/dynfc/actions/workflows/python-package.yml/badge.svg)](https://github.com/CoDe-Neuro/dynfc/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/CoDe-Neuro/dynfc/branch/main/graph/badge.svg?token=EB7Z9AWZVN)](https://codecov.io/gh/CoDe-Neuro/dynfc)
![GitHub](https://img.shields.io/github/license/CoDe-Neuro/dynfc)
[![Website](https://img.shields.io/badge/visit-website-E91E63)](https://code-neuro.github.io/dynfc/)
[![DOI](https://zenodo.org/badge/334302177.svg)](https://zenodo.org/badge/latestdoi/334302177)



This repository contains a Python module consisting of a set of tools developed to infer connectivity from fMRI (BOLD) signals. The module contains both phase-lock and correlation (+ cofluctuation) methods. Please be aware that this is still a develepment version and so may contain bugs and limited functionalities.

If you have any questions or suggestions, please [open an issue in the relevant tab](https://github.com/CoDe-Neuro/dynfc/issues). 

Please do not hesitate to suggest improvements to this module.


## Built on

[Numpy](https://numpy.org)            |  [Scipy](https://www.scipy.org)
:-------------------------:|:-------------------------:
<img src="https://www.scipy.org/_static/images/numpylogoicon.png" width="100">  |  <img src=https://docs.scipy.org/doc/scipy-0.11.0/reference/_static/scipyshiny_small.png width="100">


The data used for testing was obtained from the repository [brain-networks/edge-ts](https://github.com/brain-networks/edge-ts). [no license]

Please find references for the methods available here in the relevant [docs](https://code-neuro.github.io/dynfc/) for each function.


## Funding

<img src="https://upload.wikimedia.org/wikipedia/commons/5/58/Wellcome_Trust_logo.svg" width="300">

This project is funded by a Wellcome Trust Seed Award in Science [[217316/Z/19/Z]](https://europepmc.org/grantfinder/grantdetails?query=pi%3A%22Batalle%2BD%22%2Bgid%3A%22217316%22%2Bga%3A%22Wellcome%20Trust%22).

## License

MIT License

Copyright (c) 2021 Lucas G. S. França and Dafnis Batallé

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
