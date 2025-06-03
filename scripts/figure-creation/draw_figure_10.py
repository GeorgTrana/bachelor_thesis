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
FILP_PERM = f"{DIRP_DATA}/perm_diffs_coh.csv"
FILP_Z_VAL = f"{DIRP_DATA}/metrics-comb-z-val.csv"

if __name__ == '__main__':
	df_z = pd.read_csv(FILP_Z_VAL, sep=',')
	df_perm = pd.read_csv(FILP_PERM, sep=',')

	coh_18 = df_z.loc[df_z['group'] == 2018, 'coh_score']
	coh_19 = df_z.loc[df_z['group'] == 2019, 'coh_score']
	coh_23 = df_z.loc[df_z['group'] == 2023, 'coh_score']
	coh_24 = df_z.loc[df_z['group'] == 2024, 'coh_score']

	coh_before = pd.concat([coh_18, coh_19])
	coh_after = pd.concat([coh_23, coh_24])

	mean_before = coh_before.mean()
	mean_after  = coh_after.mean()

	std_before = coh_before.std()
	std_after  = coh_after.std()

	data = [coh_before, coh_after]
	labels = ['before', 'after']
	means  = [mean_before, mean_after]
	stds   = [std_before, std_after]
	x = np.arange(len(labels))

	# FIG 9
	mean_diff = mean_after - mean_before
	data_perm = df_perm['diffs']

	plt.hist(data_perm)
	plt.axvline(mean_diff, color='red', linestyle='--', linewidth=2, label='Observed Mean Difference')
	plt.show()




