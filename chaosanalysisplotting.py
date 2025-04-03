import pynetlogo as nl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress
import time
import csv

#this doesnt change any parameters and just measures the same exponent for several runs
#the resulting values will differ since the sim usually needs to be run for about 1500 ticks before the results are somewhat stable
#however netlogo takes its sweet time so that takes a while

#links to netlogo
netl = nl.NetLogoLink(
    gui=False,
    jvm_path="/usr/lib/jvm/java-24-openjdk/lib/server/libjvm.so",
    netlogo_home="/opt/netlogo/lib",
)

#loads the model
netl.load_model("/home/ameilioso/Downloads/EpSimWithCounters.nlogo")
lylist=[]
#num of data points you want
num=10

for i in range(num):
    #clear csv and rewrite headers each time since file is no longer deleted
    with open('/home/ameilioso/Downloads/simulation_results.csv', 'w+') as f:
      writer = csv.writer(f)
      writer.writerow(["tick","active-percentage"])
      f.close()

    #running the sim
    netl.command("setup")
    netl.command("repeat 50 [go]")
    #can add this pause if issues/glitches with slow netlogo 
    #time.sleep(10)

    df = pd.read_csv("/home/ameilioso/Downloads/simulation_results.csv")
    #print(df.head())
    ap = df["active-percentage"]
    ticks=df["tick"]
    diff = np.diff(ap)

    log_diff = np.log(np.abs(diff) + 1e-10)
    slope, intercept, rvalue, pvalue, std_err = linregress(ticks[1:], log_diff)

    #a positive Lyapunov Exponent implies a chaotic system
    lyapunov_exponent = slope
    lylist.append(lyapunov_exponent)

print(f"Lyapunov Exponents: {lylist}")
plt.plot(range(num), lylist, "o")
plt.show()
