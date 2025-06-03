# GU Students LLM Use and Its Impact on Writing Cohesion

This repository contains analysis code used for the bachelor thesis [link to bachelor thesis on GUPEA].

## Materials

All CSV files used in the data analysis are located in the stored-data/ folder.

The 244 marker words used in the data analysis are located in stored-data/marker_words.txt file.

All used figures are located in the figures/ folder.

## Dependencies

To run the necessary code the following dependencies will be needed:

* beautifulsoup4     4.13.4
* requests           2.32.3
* pandas             2.2.3
* numpy              2.2.5
* matplotlib         3.10.3

Should you only want to run the data analysis scripts, the following dependencies are needed:

* pandas             2.2.3
* numpy              2.2.5

Should you only want to generate the figures, the following dependencies are needed:

* pandas             2.2.3
* numpy              2.2.5
* matplotlib         3.10.3

Should you only want to run the scraping script, the following dependencies are needed:

* beautifulsoup4     4.13.4
* requests           2.32.3

## Reproducability instructions

1. The abstracts used in the study are scraped using the scripts/scraping/data_collection.py file. It connects to GUPEA and scrapes articles from all departements in the specified time periods. Should you run the scripts the produced CSV files will be located in the data-dump/ folder as to not be confused with previously generated data.
2. The data analysis scripts are located in the scripts/data-analysis folder. To recreate the data analysis steps from the thesis: (1) run identify_marker_words.py, (2) run permutation_test_words.py (3) run calculate_coherence.py, and (4) run permutation_test_coh.py.
3. All figures used in the thesis were created using the scripts located in the scripts/figure-creation/ folder.
