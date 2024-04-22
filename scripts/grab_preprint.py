#!/usr/bin/env python
# coding: utf-8
"""Download new lab publication information from biorXiv.
"""
import argparse
import datetime
import json
import re
import subprocess
import pathlib
import urllib.request
from glob import glob

import pandas
import dateutil.parser
from Bio import Entrez, Medline

PROJECT_FOLDER = pathlib.Path(__file__).absolute().parent.parent

parser = argparse.ArgumentParser()
parser.add_argument("-o",  "--output", type=pathlib.Path, default=PROJECT_FOLDER.joinpath("papers", "_posts"))
parser.add_argument("--template", type=pathlib.Path, default=PROJECT_FOLDER.joinpath("papers", "_posts", "preprint.md.in"))
parser.add_argument("--doi", required=True)
args = parser.parse_args()

# load template
with args.template.open() as f:
    template = f.read()

# prepare DOI
if args.doi.startswith("http"):
    args.doi = "/".join(args.doi.split("/")[-2:])
args.doi = re.sub(r'v[0-9]+$', '', args.doi)

# load preprint metadata
url = f"https://api.biorxiv.org/details/biorxiv/{args.doi}"
with urllib.request.urlopen(url) as res:
    data = json.load(res)
if data["messages"][0]["status"] != "ok":
    raise ValueError(f"failed to get metadata: {data['messages'][0]['status']}")

# find latest version of preprint
latest = max(data["collection"], key=lambda item: int(item['version']))

# extract metadata
title = latest["title"]
image = f"/assets/images/papers/biorxiv.png"
tags = ["preprint"]
journal = "biorxiv"
date = datetime.datetime.strptime(latest['date'], '%Y-%m-%d').date()
doi = f"https://doi.org/{latest['doi']}"

# reformat author list
authors = []
for author in latest['authors'].split('; '):
    last_name, initials = author.split(", ")
    initials = ''.join(filter(lambda x: x not in ' :.', initials))
    authors.append(f"{last_name} {initials}")

# build nickname
nick = [re.sub(r"\W+", "", w) for w in latest["title"].replace(":", "").lower().split(" ")[:3]]
nickname = (
    f"{date.year}-{date.month:02d}-{date.day:02d}-"
    f"{latest['authors'].split(', ')[0].replace(' ', '-').lower()}"
    f"-{'-'.join(nick)}"
)

# format template
completed = template.format(
    title=title,
    nickname=nickname,
    authors=", ".join(authors),
    year=date.year,
    journal=journal,
    image=image,
    doi=latest["doi"],
    abstract=latest["abstract"],
)

# write template
with args.output.joinpath(f"{nickname}.md").open("w") as dst:
    dst.write(completed)
print(f"New file created for {args.doi}: {nickname}.md")


# for _, row in df.iterrows():
#     pmid = row["pmid"]
#     if str(pmid) not in old_pmids:
#         # This appears broken. 'authors' is now a list of strings.
#         # authors = ast.literal_eval(row['authors'])
#         authors = row["authors"]
#         nick = [re.sub(r"\W+", "", w) for w in row["title"].lower().split(" ")[:3]]
#         nickname = (
#             f"{row['year']}-{int(row['month']):02d}-{int(row['day']):02d}-"
#             f"{authors[0].split(' ')[0].lower()}-{'-'.join(nick)}"
#         )
#         nickname = nickname.replace(":", "")
#         journal = row["journal"]
#         image = f"/assets/images/papers/{'-'.join(journal.lower().split(' '))}.png"
#         title = row["title"].replace('"', "'")
#         completed = template.format(
#             title=title,
#             nickname=nickname,
#             authors=", ".join(authors),
#             year=int(row["year"]),
#             journal=journal,
#             volume=row["volume"],
#             image=image,
#             issue=row["issue"],
#             pages=row["pages"],
#             pmcid=row["pmcid"],
#             doi=row["doi"],
#             pmid=row["pmid"],
#             abstract=row["abstract"],
#         )
#         with args.output.joinpath(f"{nickname}.md").open("w") as dst:
#             dst.write(completed)

#         print(f"New file created for {pmid}")



# # Papers indexed on PubMed, but not captured by the searches.
# other_pmids = []
# pmid_search = "[PMID] OR ".join(other_pmids) + "[PMID]"
# searches.append(pmid_search)

# # Add PMIDs of papers that should be ignored
# skip_pmids = []

# # Extract all publications matching term.
# rows = []
# for TERM in searches:
#     h = Entrez.esearch(db="pubmed", retmax="2", term=TERM)
#     result = Entrez.read(h)
#     print(f"Total number of publications containing {TERM}: {result['Count']}")
#     h_all = Entrez.esearch(db="pubmed", term=TERM, retmax=result["Count"])
#     result_all = Entrez.read(h_all)
#     ids_all = result_all["IdList"]
#     h = Entrez.efetch(db="pubmed", id=ids_all, rettype="medline", retmode="text")
#     records = Medline.parse(h)

#     acceptable_formats = [
#         "journal article",
#         "comparative study",
#         "editorial",
#         "introductory journal article",
#     ]
#     for record in records:
#         if any([type_.lower() in acceptable_formats for type_ in record.get("PT", ())]):
#             pmid = record.get("PMID")
#             pmcid = record.get("PMC", "")

#             doi = [aid for aid in record.get("AID", []) if aid.endswith(" [doi]")]
#             if doi:
#                 doi = doi[0].replace(" [doi]", "")
#             else:
#                 doi = ""

#             title = record.get("TI").rstrip(".")
#             authors = record.get("AU")

#             try:
#                 pub_date = dateutil.parser.parse(record.get("DP"))
#                 year = pub_date.year
#                 month = pub_date.month
#                 day = pub_date.day
#             except dateutil.parser.ParserError:
#                 print(f"Failed to get year for paper {pmid}")
#                 continue

#             journal = record.get("TA")
#             volume = record.get("VI", "")
#             issue = record.get("IP", "")
#             pages = record.get("PG", "")

#             abstract = record.get("AB", "")

#             row = [
#                 pmid,
#                 pmcid,
#                 doi,
#                 title,
#                 authors,
#                 year,
#                 month,
#                 day,
#                 journal,
#                 volume,
#                 issue,
#                 pages,
#                 abstract,
#             ]
#             rows += [row]

# # Save all relevant info from articles to a csv.
# df = pandas.DataFrame(
#     columns=[
#         "pmid",
#         "pmcid",
#         "doi",
#         "title",
#         "authors",
#         "year",
#         "month",
#         "day",
#         "journal",
#         "volume",
#         "issue",
#         "pages",
#         "abstract",
#     ],
#     data=rows,
# )
# df = df.sort_values(by=["pmid"])
# # df.to_csv("articles.tsv", sep="\t", lineterminator="\n", index=False)
# df = df.fillna("")

# # Grab our markdown file template
# with args.template.open("r") as src:
#     template = src.read()

# old_papers = sorted(args.output.glob("20*.md"))

# # Add papers we already have pages for.
# old_pmids = skip_pmids
# for pap in old_papers:
#     # Grab each existing article's PMID
#     with open(pap, "r") as fo:
#         dat = fo.readlines()

#     line = [lin for lin in dat if lin.startswith("pmid:")][0]
#     pmid = line.replace("pmid:", "").strip()
#     old_pmids.append(pmid)
#     old_pmids = [pmid for pmid in old_pmids if pmid]

# print(f"{len(old_papers)} existing articles found.")
# print(f"{len(old_pmids)} existing articles with PubMed IDs found.")

# # Just a small check. Unnecessary for the notebook.
# # journals = df["journal"].str.lower().unique()
# # print(journals)

# Create files for new articles
# for _, row in df.iterrows():
#     pmid = row["pmid"]
#     if str(pmid) not in old_pmids:
#         # This appears broken. 'authors' is now a list of strings.
#         # authors = ast.literal_eval(row['authors'])
#         authors = row["authors"]
#         nick = [re.sub(r"\W+", "", w) for w in row["title"].lower().split(" ")[:3]]
#         nickname = (
#             f"{row['year']}-{int(row['month']):02d}-{int(row['day']):02d}-"
#             f"{authors[0].split(' ')[0].lower()}-{'-'.join(nick)}"
#         )
#         nickname = nickname.replace(":", "")
#         journal = row["journal"]
#         image = f"/assets/images/papers/{'-'.join(journal.lower().split(' '))}.png"
#         title = row["title"].replace('"', "'")
#         completed = template.format(
#             title=title,
#             nickname=nickname,
#             authors=", ".join(authors),
#             year=int(row["year"]),
#             journal=journal,
#             volume=row["volume"],
#             image=image,
#             issue=row["issue"],
#             pages=row["pages"],
#             pmcid=row["pmcid"],
#             doi=row["doi"],
#             pmid=row["pmid"],
#             abstract=row["abstract"],
#         )
#         with args.output.joinpath(f"{nickname}.md").open("w") as dst:
#             dst.write(completed)

#         print(f"New file created for {pmid}")
