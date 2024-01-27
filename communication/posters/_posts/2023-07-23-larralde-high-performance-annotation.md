---
layout: poster
title: "High-performance annotation of biological sequence profiles"
nickname: 2023-07-23-larralde-high-performance-annotation
authors: "Larralde M, Zeller G"
year: "2023"
conference: ISCB Student Council Symposium
image: /assets/images/posters/2023-07-23-larralde-high-performance-annotation.png
tools: [pyhmmer]
tags: []

# Data and code
github: [https://github.com/althonos/pyhmmer, https://github.com/althonos/lightmotif]

---
{% include JB/setup %}

# Background 

Sequence analysis has been a prevalent field of bioinformatics growing with each new advance in DNA sequencing. Methods for sequence-profile comparison which were developed in the 20st century are still in use today, processing an ever-expanding amount of sequencing data.

Position Specific Scoring Matrices (PSSMs) were first introduced to represent sequence motifs. PSSMs take into account the occurrence of individuals letters in a motif against background probabilities. The MEME suite is commonly used for discovery and search of motifs. Expanding on PSSMs, profile Hidden Markov Models (pHMMs) were proposed to better capture protein families by additionally modelling insertions and deletions. HMMER is a de-facto standard for pHMMs, powering workflows such as the NCBI Prokaryotic Genome Annotation Pipeline.


# Description 

To support our sequence learning model, which uses pHMM features, we developed [PyHMMER](/tools/pyhmmer), a Python library binding to [HMMER](https://hmmer.org). PyHMMER offers more flexibility than the HMMER command line, as it can process inputs directly from memory. The reworked threading model results in substantial time gains for smaller target databases. On a six-core machine, PyHMMER can annotate a bacterial proteome in roughly a quarter of the time needed by HMMER. 

While HMMER offers high performance, thanks to a platform-accelerated compute kernel, there is no high-speed equivalent for PSSMs. Existing implementations motif scanning all rely on sequential scoring. Inspired by the matrix striping technique of HMMER, we developed Lightmotif, a Rust library implementing striped PSSM scanning. This technique allows for the vectorized computation of motif scores using modern CPU extensions. The AVX2 version can search a human chromosome for a binding site in a mere second, a 30x to 50x speed-up over sequential implementations. Lightmotif also provides a [Python](https://python.org) interface similar to [Biopython](https://biopython.org) to allow for drop-in replacement. 


# Conclusions

We developed two libraries for efficiently scanning sequence features using HMMs and PSSMs respectively. They leverage modern processor technologies like SIMD and multithreading to accelerate ubiquitous sequence analysis tasks. The efficiency improvements help scaling these methods to larger datasets, but also lead to a reduction in resource usage, which translates to reduced energy consumption and contributes to green computing.
