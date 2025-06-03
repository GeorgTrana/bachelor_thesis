# GRAPHS - WORD COUNT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys
import os

# DEFINE PROJECT ROOT
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

exit(420)

from config import DIRP_DATA

FILP_PERM = f"{DIRP_DATA}/perm_diffs_comb3.csv"
FILP18 = f"{DIRP_DATA}/wc_2018.csv"
FILP19 = f"{DIRP_DATA}/wc_2019.csv"
FILP23 = f"{DIRP_DATA}/wc_2023.csv"
FILP24 = f"{DIRP_DATA}/wc_2024.csv"


if __name__ == '__main__':
	df_18 = pd.read_csv(FILP18, sep=',')
	df_19 = pd.read_csv(FILP19, sep=',')
	df_23 = pd.read_csv(FILP23, sep=',')
	df_24 = pd.read_csv(FILP24, sep=',')

	data_18 = df_18['id_wc']
	data_19 = df_19['id_wc']
	data_23 = df_23['id_wc']
	data_24 = df_24['id_wc']

	mean_18 = df_18['id_wc'].mean()
	mean_19 = df_19['id_wc'].mean()
	mean_23 = df_23['id_wc'].mean()
	mean_24 = df_24['id_wc'].mean()

	std_18 = df_18['id_wc'].std()
	std_19 = df_19['id_wc'].std()
	std_23 = df_23['id_wc'].std()
	std_24 = df_24['id_wc'].std()

	data = [data_18, data_19, data_23, data_24]
	labels = ['2018', '2019', '2023', '2024']
	means  = [mean_18, mean_19, mean_23, mean_24]
	stds   = [std_18, std_19, std_23, std_24]
	x = np.arange(len(labels))
	y = np.arange(data_24.max())

	# FIG 1
	plt.boxplot(data, labels=labels, showmeans=True, meanprops= {
		"marker" : "o",
		"markerfacecolor" : "red",
		"markeredgecolor" : "black"
	})

	plt.show()




