import numpy as np
import pandas as pd
import argparse
import urllib.request
import urllib.parse
import re

def time_to_seconds(s):
    m = re.match(r'^(?P<h>[0-9]*):(?P<m>[0-9]+):(?P<s>[0-9]+)$',s)
    if m:
        sec = 3600*int(m.group("h"))+60*int(m.group("m"))+int(m.group("s"))
    else:
        m = re.match(r'^(?P<m>[0-9]+):(?P<s>[0-9]+)$',s)
        sec = 60*int(m.group("m"))+int(m.group("s"))
    return sec

parser = argparse.ArgumentParser()
parser.add_argument("--url",help="url",default="none")
parser.add_argument("--race",help="race number",default="1")
args = parser.parse_args()

race = args.race

if args.url=="none":
    full_url = "https://www.kokkens.fi/kilpailut/2018/aktia/index.php?action=show&sarja=%s10KM" % (race)
else:
    full_url = args.url

# full_url = "https://www.kokkens.fi/kilpailut/2018/aktia/index.php?action=show&sarja=110KM"



with urllib.request.urlopen(full_url) as response:
    thepage = response.read().decode(encoding="iso-8859-1")

# find table rows    
rows = list(filter(lambda x: x[:8]=="<tr><td>",thepage.split("\r\n")))

result = []

for row in rows:
    m = re.match(r"<tr><td>(?P<rank>[0-9]+)\.</td><td>(?P<bib>[0-9]+)</td><td>(?P<name>.+)</td><td>(?P<club>.*)</td><td>(?P<time>[0-9: ]*)</td><td>.*</td></tr>",
        row)
    if m:
        result.append(m.groups())

x = pd.DataFrame(result,columns=["rank","bib","name","club","time"])
x["race"] = race

x["seconds"] = x["time"].apply(time_to_seconds)

x.to_csv("%s.race.csv" % (race),index=False)

