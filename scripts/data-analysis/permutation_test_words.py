# MARKER WORDS COMPARISON

import pandas as pd
import numpy as np
import sys
import os

# DEFINE PROJECT ROOT
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import DIRP_DATA, DIRP_DATA_DUMP

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

	data_18 = df_18['id_wc']
	data_19 = df_19['id_wc']
	data_23 = df_23['id_wc']
	data_24 = df_24['id_wc']

	data_before = df_before['id_wc']
	data_after = df_after['id_wc']

	mean_18 = df_18['id_wc'].mean()
	mean_19 = df_19['id_wc'].mean()
	mean_23 = df_23['id_wc'].mean()
	mean_24 = df_24['id_wc'].mean()

	mean_before = data_before.mean()
	mean_after = data_after.mean()
	T_obs = mean_after - mean_before

	print("-"*80)
	print("MEAN FOR EACH YEAR")
	print("Mean 2018:", mean_18)
	print("Mean 2019:", mean_19)
	print("Mean 2023:", mean_23)
	print("Mean 2024:", mean_24)

	print("-"*80)
	print("BEFORE AND AFTER")
	print("Mean before:       ", mean_before)
	print("Mean after:        ", mean_after)
	print("T_obs / Mean diff: ", T_obs)

	data_comb = np.concat([data_before, data_after])
	len_before = len(data_before)
	len_after = len(data_after)
	nr_permutations = 10000

	print("Permutations:", nr_permutations)

	# GET AND STORE PERM DIFFS
	perm_diffs = []
	np.random.seed(360)
	for i in range(nr_permutations):
		data_comb_copy = data_comb.copy()
		np.random.shuffle(data_comb_copy)
		perm_before = data_comb_copy[:len_before]
		perm_after = data_comb_copy[len_before:]

		T_perm = perm_after.mean() - perm_before.mean()
		perm_diffs.append(T_perm)

		assert len(perm_before) == len_before, f"WRONG COUNT before : {len(perm_before)}"
		assert len(perm_after)  == len_after, f"WRONG COUNT after : {len(perm_after)}"

	np_perm_diffs = np.array(perm_diffs)
	extremval = 0
	for diff in np_perm_diffs:
		if abs(diff) >= abs(T_obs):
			extremval += 1

	print("-"*80)
	print("Elements in list:", len(np_perm_diffs))
	print("Extremval:", extremval)
	print("P-val estimation:", extremval/nr_permutations)
	print("-"*80)

	# PUTTING RESULTS IN CSV FOR POTENTIAL FUTURE USE..
	csv_path = f"{DIRP_DATA_DUMP}/perm_diffs_wc.csv"
	df_perm_diffs = pd.DataFrame(perm_diffs, columns=["diffs"])
	df_perm_diffs.to_csv(csv_path, sep=',', index=False)

	# CHECKING IF CSV RESULTS ARE THE SAME AS ABOVE
	print("CONFIRMING CSV RESULTS")

	df_csv = pd.read_csv(csv_path, sep=',')
	csv_diffs = df_csv.to_numpy()
	print(len(csv_diffs))

	extremval = 0
	for diff in csv_diffs:
		if abs(diff) >= abs(T_obs):
			extremval += 1

	print("Extremval:", extremval)
	print("Div:", extremval/nr_permutations)
	print("Len perm_diffs:", len(perm_diffs))
	print("Len csv_diffs:", len(csv_diffs))
	print("-"*80)

