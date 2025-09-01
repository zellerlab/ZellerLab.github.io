---
layout: tools
title: "PyOrthoANI"
contributors: [mlarralde,carroll]
handle: pyorthoani
status: complete
type: software

# Optional
website: "https://github.com/althonos/pyorthoani"
publications: "https://academic.oup.com/nargab/article/7/3/lqaf095/8196481"
doi: "10.1093/nargab/lqaf095"
image: /assets/images/tools/2025-07-11-pyorthoani-icon.png
tagline: Python re-implementation of OrthoANI.
tags: [bioinformatics, ANI]

# Data and code
github: ["https://github.com/althonos/pyorthoani"]
---
{% include JB/setup %}


## Abstract

ANI by Orthology (OrthoANI) is a method developed by [Lee *et al.* (2016)](https://pubmed.ncbi.nlm.nih.gov/26585518/)
to compute high-fidelity ANI values over divergent genomes using BLASTn to compute ortholog blocks, and 
then computing ANI values only for reciprocical blocks, therefore being less sensitive to genome rearrangements
or tandem repeats.

PyOrthoANI is a Python package which re-implements the OrthoANI algorithm, originally written in Java as part of 
the [Orthologous ANI Tool (OTA)](https://www.ezbiocloud.net/tools/orthoani). It uses the BLASTn binary of the 
local system to run all-vs-all alignments before computing the statistics using the Python standard library,
and produces values almost identical to the Java code (floating-point precision differences aside).

PyOrthoANI was developed as part of our Python ANI suite, in collaboration with [The CompMicroLab at Umeå University](https://www.microbe.dev/):
[PyOrthoANI, PyFastANI, and Pyskani: a suite of Python libraries for computation of average nucleotide identity](https://doi.org/10.1093/nargab/lqaf095).
