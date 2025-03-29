
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv("/home/ameilioso/simulation_results.csv")
ap = df["active-percentage"]
ticks=df["tick"]
diff = np.diff(ap)

#removes chance of log(0)
log_diff = np.log(np.abs(diff) + 1e-10)

slope, intercept, rvalue, pvalue, std_err = linregress(ticks[1:], log_diff)

#a positive Lyapunov Exponent implies a chaotic system
lyapunov_exponent = slope
print(f"Lyapunov Exponent: {lyapunov_exponent}")




