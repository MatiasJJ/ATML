import numpy as np
import pandas as pd

x = pd.read_csv("fmi.csv")

x.columns = ["race","cloud","airpressure","humidity","precipitation","snowdepth","temp","cond","visibility","wd","gust","ws"]

x.to_csv("weather.csv",index=False)
