---
layout: paper
title: "Investigating Enzyme Function by Geometric Matching of Catalytic Motifs"
nickname: 2026-08-06-hackett-investigating-enzyme-function
authors: "Hackett RE, Riziotis IG, Larralde M, Ribeiro AJM, Zeller G, Thornton J"
year: "2026"
journal: "Protein Science"
volume: 35
issue: 9
pages:
is_published: true
image: /assets/images/papers/the_protein_society.png
projects:
tags: ["function"]

# Text
fulltext: https://onlinelibrary.wiley.com/doi/10.1002/pro.70744
pdf: 
pdflink: https://onlinelibrary.wiley.com/doi/pdf/10.1002/pro.70744
pmcid: PMC13448135
preprint: https://doi.org/10.64898/2026.02.10.705182
supplement: https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fpro.70744&file=pro70744-sup-0001-Supinfo1.docx

# Links
doi: "10.1002/pro.70744"
pmid:  42563495

# Data and code
github: https://github.com/RayHackett/enzymm
neurovault:
openneuro:
figshare:
figshare_names:
osf:
---
{% include JB/setup %}

# Abstract

The rapidly growing universe of predicted protein structures offers opportunities for data driven exploration but requires computationally scalable and interpretable tools. We developed a method to detect catalytic features in protein structures, providing insights into enzyme function and mechanism. A library of 6780 3D coordinate sets describing enzyme catalytic sites, referred to as templates, has been collected from manually curated examples of 762 enzyme catalytic mechanisms described in the Mechanism and Catalytic Site Atlas. For template searching we optimized the geometric-matching algorithm Jess. We implemented RMSD and residue orientation filters to differentiate catalytically informative matches from spurious ones. We validated this approach on a non-redundant set of high quality experimental (n = 3751, <40% amino acid identity) enzyme structures with well annotated catalytic sites as well as predicted structures of the human proteome. We show matching catalytic templates solely on structure is more sensitive than sequence- and 3D-structure-based approaches in identifying homology between distantly related enzymes. Since geometric matching does not depend on conserved sequence motifs or even common evolutionary history, we are able to identify examples of structural active site similarity in highly divergent and possibly convergent enzymes. Such examples make interesting case studies into the evolution of enzyme function. Though not intended for characterizing substrate-specific binding pockets, the speed and knowledge-driven interpretability of our method make it well suited for expanding enzyme active-site annotation across large predicted proteomes. We provide the method and template library as a Python module, Enzyme Motif Miner, at https://github.com/rayhackett/enzymm and as a webserver at https://www.ebi.ac.uk/thornton-srv/m-csa/enzymm.
