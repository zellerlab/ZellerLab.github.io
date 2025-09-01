---
layout: tools
title: "Pyrodigal"
contributors: [mlarralde]
handle: pyrodigal
status: complete
type: software

# Optional
website: "https://pyrodigal.readthedocs.io/"
publications: "https://joss.theoj.org/papers/10.21105/joss.04296"
doi: "10.21105/joss.04296"
image: /assets/images/tools/2022-04-25-pyrodigal-icon.png
tagline: Python bindings and interface to Prodigal, an efficient method for gene prediction in prokaryotes.
tags: [bioinformatics, gene_finding]

# Data and code
github: ["https://github.com/althonos/pyrodigal"]
---
{% include JB/setup %}


## Abstract

Improvements in sequencing technologies have seen the amount of available genomic data
expand considerably over the last twenty years. One of the key steps for analysing is the
prediction of protein-coding regions in genomic sequences, known as Open Reading Frames
(ORFs), which span between a start and a stop codon. A recent comparison of several ORF
prediction methods ([Korandla et al., 2019](https://doi.org/10.1093/bioinformatics/btz714)) 
has shown that Prodigal ([Hyatt et al., 2010](https://doi.org/10.1186/1471-2105-11-119)), a
prokaryotic gene finder that uses dynamic programming, is one of the highest performing 
*ab-initio* ORF finders. Pyrodigal is a [Python](https://python.org) package 
that provides [Cython](https://cython.org) bindings and an interface to 
Prodigal to make it easier to use in Python applications.

### Pyrodigal has been used in the following publications:

1. [Accurate de novo identification of biosynthetic gene clusters with GECCO (preprint)](https://www.biorxiv.org/content/10.1101/2021.05.03.442509v1).
2. [Protein Structure Informed Bacteriophage Genome Annotation with Phold (preprint)](https://www.biorxiv.org/content/10.1101/2025.08.05.668817v1).
3. [skDER and CiDDER: two scalable approaches for microbial genome dereplication](https://doi.org/10.1099/mgen.0.001438).
4. [FastAAI: efficient estimation of genome average amino acid identity and phylum-level relationships using tetramers of universal proteins](https://doi.org/10.1093/nar/gkaf348).
5. [`zol` and `fai`: large-scale targeted detection and evolutionary investigation of gene clusters](https://doi.org/10.1093/nar/gkaf045).
