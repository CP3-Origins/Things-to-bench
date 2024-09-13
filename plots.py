import glob
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

algorithms = ['AI-Feynman', 'DSO', 'DSR', 'FFX', 'Genetic Engine', 'GPG', 'GPZGD', 'ITEA', 'Operon', 'PySR', 'QLattice', 'uDSR']
plt.rc('font', **{'family':'serif','serif': ['Computer Modern']})
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.rcParams['mathtext.fontset'] = 'stix'

# Evaluation of results

weight_counts = {
    "Correct": np.array([3, 2, 1, 1, 1, 1, 0, 1, 0, 6, 2, 4]),
    "Almost": np.array([0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 2, 0]),
    "Wrong": np.array([25, 26, 27, 27, 27, 26, 27, 27, 28, 22, 24, 24]),
}

colors = ["green", "orange", "orangered"]

width = 0.5

fig, ax = plt.subplots(figsize=(12, 6))
bottom = np.zeros(len(algorithms))

for boolean, weight_count in weight_counts.items():
    color = colors.pop(0)
    p = ax.bar(algorithms, weight_count, width, label=boolean, bottom=bottom, color=color)
    bottom += weight_count

ax.set_title("Summary of algorithm accuracy", fontsize=20)
ax.set_ylim([0, 28])
ax.legend(loc="upper right", fontsize=14)
plt.xlabel('Algorithm', fontsize=14)
plt.ylabel('Number of correct, almost correct, and wrong results', fontsize=14)
plt.yticks([0, 7, 14, 21, 28])
plt.grid(True, axis="y")
ax.set_axisbelow(True)

plt.savefig('results.pdf')
plt.show()

# Runtime of algorithms
all_files = glob.glob(os.path.join("results", "*.txt"))
result_files = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    result_files.append(df)

results = pd.concat(result_files, axis=1)
n = len(results.iloc[:, 0].values.tolist()) # Number of algorithms

run_times = [[sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":"))) for time in i] for i in results["run_time"].values.tolist()]

fig, ax = plt.subplots(figsize=(12, 6))
plt.violinplot(run_times, widths=0.7, showmeans=True, showmedians=False, showextrema=True)
ax.set_title("Runtime distributions for the different algorithms", fontsize=20)
plt.xticks(np.arange(1, n+1), algorithms)
plt.xticks(rotation=0)
plt.xlabel('Algorithm', fontsize=14)
plt.ylabel('Time', fontsize=14)
plt.yscale("log", base=60)
plt.yticks([10, 60, 10*60, 3600, 3600*10], ["10 seconds", "1 minute", "10 minutes", "1 hour", "10 hours"])
plt.grid(True)
plt.savefig('runtime.pdf')
plt.show()