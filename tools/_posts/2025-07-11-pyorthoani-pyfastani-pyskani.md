---
layout: tools
title: "PyOrthoANI, PyFastANI, PySkANI"
contributors: [mlarralde,carroll]
handle: pyorthoani-pyfastani-pyskani
status: complete
type: software

# Optional
website: 
publications: "https://academic.oup.com/nargab/article/7/3/lqaf095/8196481"
doi: "10.1093/nargab/lqaf095"
image: /assets/images/tools/2025-07-11-ani-icon.png
tagline: Python interface to OrthoANI, FastANI, and skani; methods for computing average nucleotide identity.
tags: [bioinformatics, ANI]

# Data and code
github: ["https://github.com/althonos/pyorthoani", "https://github.com/althonos/pyfastani", "https://github.com/althonos/pyskani"]
---
{% include JB/setup %}


## Abstract

The average nucleotide identity (ANI) metric has become the gold standard for prokaryotic species delineation in the genomics era. The 
most popular ANI algorithms are available as command-line tools and/or web applications, making it inconvenient or impossible to incorporate them
into bioinformatic workflows, which utilize the popular Python programming language. Here, we present PyOrthoANI, PyFastANI, and Pyskani, Python
libraries for three popular ANI computation methods. ANI values produced by PyOrthoANI, PyFastANI, and Pyskani are virtually identical to those
produced by OrthoANI, FastANI, and skani, respectively. All three libraries integrate seamlessly with BioPython, making it easy and convenient to
use, compare, and benchmark popular ANI algorithms within Python-based workflows. Availability and Implementation: Source code is open-source and
available via GitHub (PyOrthoANI, https://github.com/althonos/orthoani; PyFastANI, https://github.com/althonos/pyfastani; Pyskani,
https://github.com/althonos/pyskani). Supplementary Information: Supplementary data are available on bioRxiv.

PyFastANI, PyOrthoANI and PySkANI were developed in collaboration with [The CompMicroLab at Umeå University](https://www.microbe.dev/).

### PyOrthoANI has been used in the following publications

- [Accurate de novo identification of biosynthetic gene clusters with GECCO](https://doi.org/10.1101/2021.05.03.442509).

### PyFastANI has been used in the following publications:

- [Machine learning inference of natural product chemistry across biosynthetic gene cluster types](https://www.biorxiv.org/content/10.1101/2025.03.13.642868v1).
- [No Assembly Required: Using BTyper3 to Assess the Congruency of a Proposed Taxonomic Framework for the Bacillus cereus Group With Historical Typing Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC7536271/).
