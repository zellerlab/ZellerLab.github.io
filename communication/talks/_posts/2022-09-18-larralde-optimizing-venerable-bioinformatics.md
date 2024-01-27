---
layout: talk
title: "Optimizing venerable bioinformatics software: A profile-guided approach"
nickname: 2022-09-18-larralde-optimizing-venerable-bioinformatics
authors: "Larralde M"
year: "2022"
image: /assets/images/talks/2022-09-18-larralde-optimizing-venerable-bioinformatics.png
conference: "European Student Council Symposium"
tags: [bioinformatics, performance, optimization, profiler, green computing, Python, Cython]

# Content
slides: https://f1000research.com/slides/11-1252
video:

# Links
doi: 10.7490/f1000research.1119176.1

# Data and code
f1000: https://f1000research.com/slides/11-1252
---
{% include JB/setup %}

# Abstract

With an ever-increasing amount of available data, scalability problems are much 
more of a concern than they were 20 years ago, and climate change issues urges 
for greener computing. In bioinformatics, a few methods have become de-facto 
standards to approach specific issues such as gene-calling, multiple sequence 
alignment, or protein domain annotation. These tools are now the basis of numerous 
annotation pipelines that are executed thousands of time daily. Academia however 
favors scientific novelty over efficiency, and C or C++ code is more than 
enough to be categorized as high-performance software.

In this work, we use profiling to identify critical parts of established 
bioinformatics methods. We then employ several optimization techniques to 
make these tools more efficient. We show how inlining a few functions halve 
the runtime of the [PRANK](https://ariloytynoja.github.io/prank-msa/) aligner; 
how caching alignment matrices used by [trimAl](http://trimal.cgenomics.org/) 
reduce the runtime 10-fold; how SIMD speeds up the gene scoring step of 
[Prodigal](https://github.com/hyattpd/Prodigal); and how parallel hashing in 
[FastANI](https://github.com/ParBLiSS/FastANI) increases the efficiency on 
multi-core machines.

The goal of this software engineering experiment is to introduce some efficient 
programming habits to the community, and to change the perspective about 
ubiquitous software we use brainlessly in our pipelines. More practically, we 
provide several of these patches as [Python](https://python.org) packages to 
be used as drop-in replacements for the originals. As a perspective, we 
present some general figures about the energetic cost of computing, and 
how much CO2 can be saved with the aforementioned optimizations.
