import sys
import os

'''
The GUPEA abstract scraping script will automatically generate four folders (2018, 2019, 2023, 2024) in the DIRP_DATA_DUMP directory specified below. The other data extraction scripts will generate only CSV files. When generating figures using matplotlib they will be opened automatically and you can manually save a newly generated figure wherever you wish.
'''
# PROJECT ROOT
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DIRP_BASE = os.path.abspath(os.path.join(THIS_DIR, '..', '..'))

# PATHS TO DATA, without a "/" at the end!!!
DIRP_DATA = f"{DIRP_BASE}/stored-data"
DIRP_DATA_DUMP = f"{DIRP_BASE}/data-dump"
