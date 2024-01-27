---
layout: talk
title: "Accurate de novo identification of biosynthetic gene clusters with GECCO"
nickname: 2022-06-13-larralde-accurate-de-novo-identification
authors: "Carroll LM, Larralde M, Fleck JS, Ponnudurai R, Milanese A, Cappio E, Zeller G"
year: "2022"
conference: Microbial Secondary Metabolites in Microbiomes
image: /assets/images/talks/2022-06-13-larralde-accurate-de-novo-identification.png
projects: [secmet]
tags: []

---
{% include JB/setup %}

Biosynthetic gene clusters (BGCs) are enticing targets for (meta)genomic mining efforts, as they may encode novel, specialized metabolites with potential uses in medicine and biotechnology. We developed [GECCO](https://gecco.embl.de) (GEne Cluster prediction with COnditional random fields), a high-precision, scalable method for identifying novel BGCs in (meta)genomic data, which is both more accurate and over 4x faster than the state-of-the-art. We applied GECCO to >300,000 genomes and metagenomes derived from human gut-associated microbes, representing the most extensive characterization of the human gut microbiome biosynthetic potential to date. In the process, we identified 616,045 BGCs, which encompass previously unexplored regions of the human gut microbiome biosynthetic landscape. Using a high-throughput clustering method, we then identified 107,856 Gene Cluster families, half of which can be found in micro-organisms highly prevalent in the human gut. The method developed here represents a scalable, interpretable machine learning approach, which can identify BGCs de novo with high precision and provide unprecedented insight into microbial biosynthetic potential.
