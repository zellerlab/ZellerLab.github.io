---
layout: paper
title: "Machine learning inference of natural product chemistry across biosynthetic gene cluster types"
nickname: 2025-03-15-larralde-machine-learning-inference
authors: "Larralde M, Zeller G"
year: "2025"
journal: "biorxiv"
volume:
issue:
pages:
is_published: false
image: /assets/images/papers/biorxiv.png
projects: ["secmet", "function"]
tags: ["preprint"]

# Text
fulltext:
pdf:
pdflink:
pmcid:
preprint: https://doi.org/10.1101/2025.03.13.642868
supplement:

# Links
doi: "10.1101/2025.03.13.642868"
pmid:

# Data and code
github: https://github.com/zellerlab/CHAMOIS
neurovault:
openneuro:
figshare:
figshare_names:
osf:
zenodo: 15009032
---
{% include JB/setup %}

# Abstract

With ever-increasing volumes of sequencing data for biosynthetic gene clusters (BGCs), computational methods to accurately predict which secondary metabolites result from these are critically lacking. Here, we present CHAMOIS, a machine learning-based tool for predicting chemical properties of secondary metabolites from protein domains annotated in the input BGCs. CHAMOIS infers 485 chemical properties from the ChemOnt ontology using logistic regression. It accurately predicts 111 such properties (AUPRC > 0.5) in cross-validation against known instances. Although CHAMOIS is not explicitly trained on biosynthetic knowledge, many of the inferred links between protein domains and metabolite properties are consistent with scientific literature, others suggest new biochemical functions of uncharacterized biosynthetic domains. Finally, CHAMOIS can pinpoint which BGC within a given genome produces a pre-specified metabolite (correct BGC in 69% of cases ranked among the top 5), which holds great potential for prioritising experimental BGC characterisation and discovery of novel biosynthetic enzymes.
