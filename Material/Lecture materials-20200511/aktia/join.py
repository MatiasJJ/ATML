import numpy as np
import pandas as pd
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("races",nargs="+",help="race numbers",default="1 2 3 4 5")
args = parser.parse_args()
races = args.races

a = pd.read_csv("%s.race.csv" % (races[0]))
for r in races[1:]:
    a = a.append(pd.read_csv("%s.race.csv" % (r)),ignore_index=True)

a.to_csv("aktia.csv",index=False)
