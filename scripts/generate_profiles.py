import pandas as pd
import os

df = pd.read_excel("../assets/files/members/group_members.xlsx", sheet_name="Members")
group_df = df.groupby("NAME")

file_header = """---
layout: member
title: {name}
position: {position}
handle: {handle}
science_names:
image: placeholder.png
alumni: true
linkedin:
country: {countries}

# social
email:
orcid:
researchgate:
scholar:
---

"""

already_there = ["-".join(reversed(fl.split("-")[3:])).replace(".md", "") for fl in os.listdir("../team/_posts")]

for name, content in group_df:
    # check if already there
    if name.lower().replace(" ", "-") in already_there:
        pass
    else:
        handle = name.split(" ")[-1].lower()
        file_content = "%s was " % name
        for index, row in content.iterrows():
            countries = str([i for i in row["NATIONALITY"].lower().split("/")]).replace("'", "").replace(" ", "")
            position = row["POSITION"]
            start, end = str(row["START DATE"]).split(" ")[0], str(row["END DATE"]).split(" ")[0]
            file_content += """a {position} in the lab from {start} to {end},""".format(position=row["POSITION"], start=start, end=end)
        file_content = file_content[:-1] + "."
        # file content ready
        file_string = file_header.format(name=name, position=position, handle=handle, countries=countries)+file_content
        f = open("../team/alumni/2024-02-21-%s.md" % namelisanna-paladin.replace(" ", "-").lower(), "w")
        f.write(file_string)
        f.close()

# print(file_header.format(name=name, position=row["POSITION"], handle=handle, countries=countries))
