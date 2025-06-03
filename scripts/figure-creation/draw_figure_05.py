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

# FILP_PERM = f"{DIRP_DATA}/perm_diffs_comb3.csv"
FILP18 = f"{DIRP_DATA}/wc_2018.csv"
FILP19 = f"{DIRP_DATA}/wc_2019.csv"
FILP23 = f"{DIRP_DATA}/wc_2023.csv"
FILP24 = f"{DIRP_DATA}/wc_2024.csv"
FILP_PERM = f"{DIRP_DATA}/perm_diffs_wc.csv"

if __name__ == '__main__':
	df_18 = pd.read_csv(FILP18, sep=',')
	df_19 = pd.read_csv(FILP19, sep=',')
	df_23 = pd.read_csv(FILP23, sep=',')
	df_24 = pd.read_csv(FILP24, sep=',')

	df_before = pd.concat([df_18, df_19])
	df_after = pd.concat([df_23, df_24])
	df_perm = pd.read_csv(FILP_PERM, sep=',')

	data_before = df_before['id_wc']
	data_after = df_after['id_wc']

	mean_before = data_before.mean()
	mean_after = data_after.mean()

	# FIG 5
	mean_diff = mean_after - mean_before
	data_perm = df_perm['diffs']

	plt.hist(data_perm)
	plt.axvline(mean_diff, color='red', linestyle='--', linewidth=2, label='Observed Mean Difference')
	plt.show()





