---
layout: paper
title: "A realistic benchmark for differential abundance testing and confounder adjustment in human microbiome studies"
nickname: 2024-09-25-wirbel-a-realistic-benchmark
authors: "Wirbel J, Essex M, Forslund SK, Zeller G"
year: "2024"
journal: "Genome Biol"
volume: 25
issue: 1
pages: 247
is_published: true
image: /assets/images/papers/genome-biol.png
projects: [stats]
tags: []

# Text
fulltext:
pdf:
pdflink:
pmcid: PMC11423519
preprint: https://doi.org/10.1101/2022.05.09.491139
supplement:

# Links
doi: "10.1186/s13059-024-03390-9"
pmid: 39322959

# Data and code
github:
neurovault:
openneuro:
figshare:
figshare_names:
osf:
---
{% include JB/setup %}

# Abstract

BACKGROUND: In microbiome disease association studies, it is a fundamental task to test which microbes differ in their abundance between groups. Yet, consensus on suitable or optimal statistical methods for differential abundance testing is lacking, and it remains unexplored how these cope with confounding. Previous differential abundance benchmarks relying on simulated datasets did not quantitatively evaluate the similarity to real data, which undermines their recommendations. RESULTS: Our simulation framework implants calibrated signals into real taxonomic profiles, including signals mimicking confounders. Using several whole meta-genome and 16S rRNA gene amplicon datasets, we validate that our simulated data resembles real data from disease association studies much more than in previous benchmarks. With extensively parametrized simulations, we benchmark the performance of nineteen differential abundance methods and further evaluate the best ones on confounded simulations. Only classic statistical methods (linear models, the Wilcoxon test, t-test), limma, and fastANCOM properly control false discoveries at relatively high sensitivity. When additionally considering confounders, these issues are exacerbated, but we find that adjusted differential abundance testing can effectively mitigate them. In a large cardiometabolic disease dataset, we showcase that failure to account for covariates such as medication causes spurious association in real-world applications. CONCLUSIONS: Tight error control is critical for microbiome association studies. The unsatisfactory performance of many differential abundance methods and the persistent danger of unchecked confounding suggest these contribute to a lack of reproducibility among such studies. We have open-sourced our simulation and benchmarking software to foster a much-needed consolidation of statistical methodology for microbiome research.
