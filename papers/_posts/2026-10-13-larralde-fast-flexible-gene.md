---
layout: paper
title: "Fast, flexible gene cluster family delineation with IGUA"
nickname: 2026-10-13-larralde-fast-flexible-gene
authors: "Larralde M, Blom J, Gourle H, Carroll LM, Zeller G"
year: "2026"
journal: "Nucleic Acids Res"
volume: 54
issue: 19
pages:
is_published: true
image: /assets/images/papers/nucleic-acids-res.png
projects: [secmet]
tools: [igua]
tags: []

# Text
fulltext: https://academic.oup.com/nar/article/54/19/gkag975/8913153
pdf: https://academic.oup.com/nar/article-pdf/54/19/gkag975/71897619/gkag975.pdf
pdflink:
pmcid: PMC13659240 
preprint: https://doi.org/10.1101/2025.05.15.654203
supplement: https://academic.oup.com/nar/article/54/19/gkag975/8913153#supplementary-data

# Links
doi: "10.1093/nar/gkag975"
pmid: 42866952

# Data and code
github: [https://github.com/zellerlab/IGUA]
neurovault:
openneuro:
figshare:
figshare_names:
osf:
---
{% include JB/setup %}

# Abstract

Prokaryotic genomes harbor a variety of functional elements encoded as contiguous multi-gene clusters. To identify homologous gene clusters, computational tools that account for multi-gene architectures are needed to group gene clusters into Gene Cluster Families (GCFs). However, existing GCF delineation methods do not scale well to large datasets and are often limited to certain subclasses of gene clusters. Here, we present IGUA (Iterative Gene clUster Analysis; [https://github.com/zellerlab/IGUA](https://github.com/zellerlab/IGUA)), a scalable, flexible GCF delineation method for genomic segments with multi-gene architectures. On a biosynthetic gene cluster (BGC) clustering task, IGUA is 29× and 10× faster than the state-of-the-art (BiG-SCAPE v2 and BiG-SLiCE v2, respectively; 28 CPUs), without sacrificing accuracy. To highlight its scalability, we use IGUA to cluster >2.8 million BGCs from ≈1 million prokaryotic genomes in <18 h (n = 2 829 071 BGCs to 56 960 GCFs). To showcase its utility beyond BGC clustering, we use IGUA to cluster five additional prokaryotic gene cluster types (secretion systems, prophages, genomic islands, phage-plasmids, and carbohydrate active enzyme [CAZyme] gene clusters). Overall, IGUA represents a versatile GCF delineation tool with unmatched computational efficiency and flexibility, enabling (meta)genomic mining applications at unprecedented scales.
