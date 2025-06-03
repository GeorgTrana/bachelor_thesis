# COHERENCE SCORE COMPARISON

import pandas as pd
import numpy as np
import sys
import os

# DEFINE PROJECT ROOT
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import DIRP_DATA, DIRP_DATA_DUMP

if __name__ == '__main__':
	filp = f"{DIRP_DATA}/metrics-comb-z-val.csv"

	df_comb = pd.read_csv(filp, sep=',')
	coh_18 = df_comb.loc[df_comb['group'] == 2018, 'coh_score']
	coh_19 = df_comb.loc[df_comb['group'] == 2019, 'coh_score']
	coh_23 = df_comb.loc[df_comb['group'] == 2023, 'coh_score']
	coh_24 = df_comb.loc[df_comb['group'] == 2024, 'coh_score']

	coh_before = np.concatenate([coh_18, coh_19])
	coh_after = np.concatenate([coh_23, coh_24])

	mean_18 = coh_18.mean( )
	mean_19 = coh_19.mean( )
	mean_23 = coh_23.mean( )
	mean_24 = coh_24.mean( )

	mean_before = coh_before.mean()
	mean_after = coh_after.mean()
	T_obs = coh_after.mean() - coh_before.mean()

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

	coh_comb = df_comb['coh_score'].to_numpy()
	len_before = len(coh_before)
	len_after = len(coh_after)
	nr_permutations = 10000

	print("Permutations:", nr_permutations)

	# GET AND STORE PERM DIFFS
	perm_diffs = []
	np.random.seed(360)
	for i in range(nr_permutations):
		coh_comb_copy = coh_comb.copy()
		np.random.shuffle(coh_comb_copy)
		perm_before = coh_comb_copy[:len_before]
		perm_after = coh_comb_copy[len_before:]

		T_perm = perm_after.mean() - perm_before.mean()
		perm_diffs.append(T_perm)

		assert len(perm_before) == len_before, f"WRONG COUNT before : {len(perm_before)}"
		assert len(perm_after)  == len_after, f"WRONG COUNT after : {len(perm_after)} vs {len_after}"

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
	csv_path = f"{DIRP_DATA_DUMP}/perm_diffs_coh.csv"
	df_perm_diffs = pd.DataFrame(perm_diffs, columns=["diffs"])
	df_perm_diffs.to_csv(csv_path, sep=',', index=False)

	# CHECKING IF CSV RESULTS ARE THE SAME AS ABOVE
	print("CHECKING CSV RESULTS")

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

