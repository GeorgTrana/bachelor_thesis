# GRAPHS - WORD COUNT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys
import os

# DEFINE PROJECT ROOT
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

	df_before = pd.concat([df_18, df_19])
	df_after = pd.concat([df_23, df_24])

	data_before = df_before['id_wc']
	data_after = df_after['id_wc']

	mean_before = data_before.mean()
	mean_after = data_after.mean()

	std_before = df_before['id_wc'].std()
	std_after = df_after['id_wc'].std()

	data2   = [data_before, data_after]
	labels2 = ['Before', 'After']
	means2  = [mean_before, mean_after]
	stds2   = [std_before, std_after]
	x2 = np.arange(len(labels2))
	y2 = np.arange(data_after.max())

	# FIG 4
	plt.stem(x2, means2)
	plt.xticks(x2, labels2)
	plt.ylabel('Excess Words Found')
	plt.grid(True)

	plt.show()




