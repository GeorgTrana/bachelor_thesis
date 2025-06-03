# import pandas as pd

import os
import sys
import string

from config import DIRP_DATA

# CSV_DIRP = "/full/path/to/folder/w/abstract-folders"
FILP    = f"{DIRP_DATA}/marker_words.txt"
PATH_TO  = f"{DIRP_DATA_DUMP}/AI_TEST_{year}"
YEARS    = [2018, 2019, 2023, 2024]

if __name__ == '__main__':
	# CREATE AI WORD LIST
	ai_words = []
	with open(FILP, "r", encoding="utf-8") as f:
		content = f.readlines()
		for word in content:
			clean_word = ' '.join(word.split())
			ai_words.append(clean_word)

	for year in YEARS:
		results = []
		abs_dirp = f"{DIRP_DATA}/{year}"

		for file in os.listdir(abs_dirp):
			ai_wc = 0

			abs_file = os.fsdecode(file)
			abs_filep = f"{abs_dirp}/{abs_file}"
			with open(abs_filep, "r", encoding="utf-8") as f:
				abstract = f.readline()
				no_punct_abs = abstract.translate(str.maketrans('', '', string.punctuation))
				clean_abs = ' '.join(no_punct_abs.split())
				abs_word_list = clean_abs.split(' ')
				for word in abs_word_list:
					if word in ai_words:
						ai_wc += 1

			res_str = f"{abs_file},{ai_wc}"
			results.append(res_str)

		with open(PATH_TO, "a", encoding="utf-8") as f:
			f.write("filename,wc_id\n")
			for res in results:
				f.write(res+"\n")


