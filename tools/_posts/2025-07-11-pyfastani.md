---
layout: tools
title: "PyFastANI"
contributors: [mlarralde,carroll]
handle: pyfastani
status: complete
type: software

# Optional
website: "https://pyfastani.readthedocs.io/"
publications: "https://academic.oup.com/nargab/article/7/3/lqaf095/8196481"
doi: "10.1093/nargab/lqaf095"
image: /assets/images/tools/2025-07-11-pyfastani-icon.png
tagline: Cython bindings and Python interface to FastANI, a method for fast whole-genome similarity estimation..
tags: [bioinformatics, ANI]

# Data and code
github: ["https://github.com/althonos/pyfastani"]
---
{% include JB/setup %}


## Abstract

FastANI is a method developed by [Chirag Jain *et al.*](https://www.nature.com/articles/s41467-018-07641-9) 
for high-throughput computation of whole-genome average nucleotide identity (ANI). It uses 
[MashMap](https://pubmed.ncbi.nlm.nih.gov/29708767/), a min-hashing technique, to compute orthologous mappings 
without the need for expensive alignments.

PyFastANI is a [Python](https://python.org) module, implemented using the [Cython](https://cython.org) language, 
that provides bindings to FastANI. It improves on FastANI by enabling per-query multithreading to speed-up 
individual sequence searches, where originally FastANI only supports across-query multithreading in the case
of many-to-may searches.

PyFastANI was developed as part of our Python ANI suite, in collaboration with [The CompMicroLab at Umeå University](https://www.microbe.dev/):
[PyOrthoANI, PyFastANI, and Pyskani: a suite of Python libraries for computation of average nucleotide identity](https://doi.org/10.1093/nargab/lqaf095).


### PyFastANI has been used in the following publications:

- [Machine learning inference of natural product chemistry across biosynthetic gene cluster types](https://www.biorxiv.org/content/10.1101/2025.03.13.642868v1).
- [No Assembly Required: Using BTyper3 to Assess the Congruency of a Proposed Taxonomic Framework for the Bacillus cereus Group With Historical Typing Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC7536271/).
