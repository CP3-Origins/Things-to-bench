import glob
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

all_files = glob.glob(os.path.join("results", "*.txt"))
result_files = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    result_files.append(df)

results = pd.concat(result_files, axis=1)
n = len(results.iloc[:, 0].values.tolist()) # Number of algorithms

run_times = [[sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":"))) for time in i] for i in results["run_time"].values.tolist()]

plt.violinplot(run_times, showmeans=True, showmedians=False)
plt.title("Runtime distributions for the different algorithms")
plt.xticks(np.arange(1, n+1), results.iloc[:, 0].values.tolist())
plt.xticks(rotation=45)
#plt.ylabel('Seconds[s]')
plt.yscale("log", base=60)
plt.yticks([60, 3600], ["minute", "hour"])
plt.rc('font', **{'family':'serif','serif': ['Computer Modern']})
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.show()