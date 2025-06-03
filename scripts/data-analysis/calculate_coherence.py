import pandas as pd

from config import DIRP_DATA, DIRP_DATA_DUMP


def z_calc(x_val, mean, std):
	z_val = (x_val - mean) / std
	return z_val

if __name__ == '__main__':

	'''
		Z-VAL FORMULA:
			z_val = (x_value - mean_for_col)/std_for_col

	'''

	file_18 = "metrics-2018.csv"
	file_19 = "metrics-2019.csv"
	file_23 = "metrics-2023.csv"
	file_24 = "metrics-2024.csv"

	filp_18 = f"{DIRP_DATA}/{file_18}"
	filp_19 = f"{DIRP_DATA}/{file_19}"
	filp_23 = f"{DIRP_DATA}/{file_23}"
	filp_24 = f"{DIRP_DATA}/{file_24}"

	df_18 = pd.read_csv(filp_18, sep=',')
	df_19 = pd.read_csv(filp_19, sep=',')
	df_23 = pd.read_csv(filp_23, sep=',')
	df_24 = pd.read_csv(filp_24, sep=',')

	df_comb = pd.concat([df_18, df_19, df_23, df_24], ignore_index=True)

	col_stats = {
		col : {
			'mean' : df_comb[col].mean(),
			'std'  : df_comb[col].std()
		} for col in df_comb.columns
	}

	df_18['group'] = '2018'
	df_19['group'] = '2019'
	df_23['group'] = '2023'
	df_24['group'] = '2024'

	df_comb = pd.concat([df_18, df_19, df_23, df_24], ignore_index=True)
	list_df = [df_18, df_19, df_23, df_24]

	real_counter = 0
	is_counter = 0
	z_score_dfs = []

	for df in list_df:
		z_list = []
		z_group = []
		row_count = len(df)
		for row_nr in range(row_count):
			stat_group = df['group'].iloc[row_nr]
			row_vals = []
			z_temp = []
			for i in range(len(df.columns)-1):
				col = df.columns[i]
				stat_nr = df[col].iloc[row_nr]
				stat_group = df['group'].iloc[row_nr]
				z_mean  = col_stats[col]['mean']
				z_std   = col_stats[col]['std']

				z_val = z_calc(stat_nr, z_mean, z_std)
				z_temp.append(z_val)
			z_sum = 0
			for e in z_temp:
				z_sum += e
			z_avg = z_sum/7
			z_list.append(z_avg)
			z_group.append(stat_group)

		assert len(z_list) == len(z_group), "WRONG LENGTH"
		print(len(z_list))
		print(len(z_group))
		df_coh = pd.DataFrame({
			'coh_score' : z_list,
			'group' : z_group
		})
		z_score_dfs.append(df_coh)

	df_z_scores = pd.concat(z_score_dfs, ignore_index=True)
	df_z_scores.to_csv(f"{DIRP_DATA}/metrics-comb-z4.csv", index=False)
	print(df_z_scores)




