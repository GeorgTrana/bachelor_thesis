import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys
import os

# DEFINE PROJECT ROOT
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import DIRP_DATA

# filp_z = f"{dirp_metrics}/metrics-comb-z4.csv"
FILP_Z_VAL = f"{DIRP_DATA}/metrics-comb-z-val.csv"

if __name__ == '__main__':
	df_z = pd.read_csv(FILP_Z_VAL, sep=',')

	coh_18 = df_z.loc[df_z['group'] == 2018, 'coh_score']
	coh_19 = df_z.loc[df_z['group'] == 2019, 'coh_score']
	coh_23 = df_z.loc[df_z['group'] == 2023, 'coh_score']
	coh_24 = df_z.loc[df_z['group'] == 2024, 'coh_score']

	coh_before = pd.concat([coh_18, coh_19])
	coh_after = pd.concat([coh_23, coh_24])

	mean_18 = coh_18.mean()
	mean_19 = coh_19.mean()
	mean_23 = coh_23.mean()
	mean_24 = coh_24.mean()

	mean_before = coh_before.mean()
	mean_after  = coh_after.mean()

	std_18 = coh_18.std()
	std_19 = coh_19.std()
	std_23 = coh_23.std()
	std_24 = coh_24.std()

	std_before = coh_before.std()
	std_after  = coh_after.std()

	data = [coh_before, coh_after]
	labels = ['before', 'after']
	means  = [mean_before, mean_after]
	stds   = [std_before, std_after]
	x = np.arange(len(labels))
	# y = np.arange(coh_24.max())

# 	plt.boxplot(data, labels, showmeans=True, meanprops= {
# 		"marker" : "o",
# 		"markerfacecolor" : "red",
# 		"markeredgecolor" : "black"
# 	})
#
# 	plt.xticks(x+1, labels)
# 	plt.ylabel('Cohesion Score')
# 	plt.grid(True)
# 	plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(1))

	# FIG 9
	plt.stem(x, means)
	plt.xticks(x, labels)
	plt.ylabel('Cohesion Score')
	plt.grid(True)

	plt.show()


