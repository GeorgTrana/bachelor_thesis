#COLLECTING DATA FROM GUPEA

from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import sys
from sys import exception
import os.path
from typing import Any
from map_dep import dep_nicknamer, dep_to_faculty

from config import DIRP_DATA_DUMP

DO_TESTS: bool = True

# GUPEA URLs
URL_RAW: str = "https://gupea.ub.gu.se/"
URL_BASE: str = "https://gupea.ub.gu.se/handle/2077/785"


urls_deps: dict[str, str] = {
	"Academy of Music and Drama" : "https://gupea.ub.gu.se/handle/2077/24945" ,
	"Department of Applied Information Technology" : "https://gupea.ub.gu.se/handle/2077/869" ,
	"Department of Biological and Environmental Sciences" : "https://gupea.ub.gu.se/handle/2077/54323" ,
	"Department of Business Administration" : "https://gupea.ub.gu.se/handle/2077/786",
	"Department of Chemistry and Molecular Biology (2012-)" : "https://gupea.ub.gu.se/handle/2077/34573",
	"Department of Comparative Literature (-2008)" : "https://gupea.ub.gu.se/handle/2077/7198",
	"Department of Computer Science and Engineering" : "https://gupea.ub.gu.se/handle/2077/22009",
	"Department of Conservation" : "https://gupea.ub.gu.se/handle/2077/18655",
	"Department of Cultural Sciences" : "https://gupea.ub.gu.se/handle/2077/21432",
	"Department of Earth Sciences" : "https://gupea.ub.gu.se/handle/2077/59928",
	"Department of Economics" : "https://gupea.ub.gu.se/handle/2077/28037",
	"Department of Economy and Society (2013-)" : "https://gupea.ub.gu.se/handle/2077/31770",
	"Department of Education (-2010)" : "https://gupea.ub.gu.se/handle/2077/19452",
	"Department of Education and Special Education (2010-)" : "https://gupea.ub.gu.se/handle/2077/24912",
	"Department of Education, Communication and Learning" : "https://gupea.ub.gu.se/handle/2077/24913",
	"Department of Food and Nutrition, and Sport Science" : "https://gupea.ub.gu.se/handle/2077/24178",
	"Department of Historical Studies" : "https://gupea.ub.gu.se/handle/2077/35280",
	"Department of Human and Economic Geography (-2012)" : "https://gupea.ub.gu.se/handle/2077/802",
	"Department of Informatics (-2005)" : "https://gupea.ub.gu.se/handle/2077/810",
	"Department of Languages and Literatures (2009-)" : "https://gupea.ub.gu.se/handle/2077/3314",
	"Department of Law" : "https://gupea.ub.gu.se/handle/2077/805",
	"Department of Literature, History of Ideas, and Religion" : "https://gupea.ub.gu.se/handle/2077/21110",
	"Department of Marine Sciences" : "https://gupea.ub.gu.se/handle/2077/52331",
	"Department of Mathematical Sciences" : "https://gupea.ub.gu.se/handle/2077/28886",
	"Department of Pedagogical, Curricular and Professional Studies" : "https://gupea.ub.gu.se/handle/2077/24914",
	"Department of Philosophy,Lingustics and Theory of Science" : "https://gupea.ub.gu.se/handle/2077/24914",
	"Department of Political Science" : "https://gupea.ub.gu.se/handle/2077/10111",
	"Department of Psychology" : "https://gupea.ub.gu.se/handle/2077/36647",
	"Department of Social Work" : "https://gupea.ub.gu.se/handle/2077/3753",
	"Department of Sociology (-2011)" : "https://gupea.ub.gu.se/handle/2077/4738",
	"Department of Sociology and Work Science" : "https://gupea.ub.gu.se/handle/2077/29677",
	"Department of Swedish, Multilingualism, Language Technology" : "https://gupea.ub.gu.se/handle/2077/18309",
	"Department of Work Science (-2011)" : "https://gupea.ub.gu.se/handle/2077/24915",
	"Graduate School" : "https://gupea.ub.gu.se/handle/2077/830",
	"HDK - School of Design and Crafts (2012-2019)" : "https://gupea.ub.gu.se/handle/2077/31644",
	"HDK - Valand - Academy of Art and Design (2020-)" : "https://gupea.ub.gu.se/handle/2077/62721",
	"Institute of Biomedicine" : "https://gupea.ub.gu.se/handle/2077/23907",
	"Institute of Clinical Sciences" : "https://gupea.ub.gu.se/handle/2077/35823",
	"Institute of Health and Care Sciences" : "https://gupea.ub.gu.se/handle/2077/4427",
	"Institute of Medicine" : "https://gupea.ub.gu.se/handle/2077/3755",
	"Institute of Neuroscience and Physiology" : "https://gupea.ub.gu.se/handle/2077/9914",
	"Department of Physics" : "https://gupea.ub.gu.se/handle/2077/60401",
	"JMG - Department of Journalism, Media and Communication" : "https://gupea.ub.gu.se/handle/2077/3137",
	"Lärarutbildningsnämnden (2010-)" : "https://gupea.ub.gu.se/handle/2077/38531",
	"Pedagogical Development and Interactive Learning" : "https://gupea.ub.gu.se/handle/2077/40526",
	"Programme on Human Resource Development and Labour Relation" : "https://gupea.ub.gu.se/handle/2077/23596",
	"Programmet för personal- och arbetslivsfrågor(-2010)" : "https://gupea.ub.gu.se/handle/2077/63",
	"School of Business, Economics and Law" : "https://gupea.ub.gu.se/handle/2077/45133",
	"School of Global Studies" : "https://gupea.ub.gu.se/handle/2077/28932",
	"Steneby - School of Craft and Design (-jun 2012)" : "https://gupea.ub.gu.se/handle/2077/28239", # swe?
	"The School of Design and Crafts (-jun 2012)" : "https://gupea.ub.gu.se/handle/2077/8442",
	"The School of Film Directing" : "https://gupea.ub.gu.se/handle/2077/22374",
	"The School of Public Administration" : "https://gupea.ub.gu.se/handle/2077/23909",
	"Utbildnings- och forskningsnämnden för lärarutbildning, UFL, (-2010)" : "https://gupea.ub.gu.se/handle/2077/13", # swe?
	"Valand Academy (-2019)" : "https://gupea.ub.gu.se/handle/2077/27320",
}


'''
To make sure that all articles got captured by the regular expression.
'''

def check_article_count(page_info_tag: Any, href_tags: list, curr_url: str ) -> bool:
	page_info_count: int = int(re.findall("(\d+)", str(page_info_tag))[-1])
	href_count:      int = len(href_tags)

	if page_info_count == href_count and href_count:
		return True
	else:
		return False


def is_eng(article_soup: Any) -> bool:
	if article_soup.find('meta', content='eng'):
		return True
	elif article_soup.find('meta', content='swe'): # to make it easier to check if the program missed any english tags
		return False
	elif article_soup.find('meta', content='nor'): # to make it easier to check if the program missed any english tags
		return False
	else:
		print("NO LANG:", article_url) # to check manually if article has english tag, you can speed up the program by removing this I/O statement
		return False


'''
When doing your own analysis it can be important to keep track of what year, faculty, departement, and a shortened version of the article name. No specific abstract name nicknames have been stored in the stored-data folder, but when reproducing or extending the research, it can be useful to keep track of specific abstracts.

'''

def make_uq(name: str) -> str:
	nickname: str = ''.join([word[0] for word in name.split()])
	return nickname


def create_file_name(year: int, dep_name: str, title_nickname: str) -> str:
	dep_nickname:str = dep_nicknamer[dep_name]
	fac_nickname:str = dep_to_faculty[dep_nickname]
	file_name: str = f"{year}-{fac_nickname}-{dep_nickname}-{title_nickname}.txt"
	return file_name


if __name__ == "__main__":
	years: list[int] = [2018, 2019, 2023, 2024]

	tot_deps: int = len(urls_deps.items())
	eng_count: int = 0
	for year in years:
		url_filter = f"/discover?filtertype_1=dateIssued&filter_relational_operator_1=contains&filter_1={year}&submit_apply_filter=&query=&rpp=1000&sort_by=score&order=desc"
		print(f"Year: {year}")

		curr_dep_count: int = 0
		for dep_item in urls_deps.items():
			try:
				dep_name: str = dep_item[0]
				dep_url: str = dep_item[1]
				curr_url = f"{dep_url}{url_filter}"
				curr_dep_count += 1
				print(f"{curr_dep_count}/{tot_deps} : {dep_name}")

				req_dep: str = requests.get(curr_url).text
				assert req_dep is not None, f"NO DEP URL : {curr_url}"

				dep_soup = BeautifulSoup(req_dep, features="html.parser")
				# soup_str: str = str(dep_soup.prettify())
				page_info_tag: Any = dep_soup.find(class_=re.compile("pagination-info"))
				assert page_info_tag, f"NO PAGE INFO TAG : {curr_url}"

				article_links: list = dep_soup.find_all("a",href=re.compile("handle"))
				href_tags: list = [tag for tag in article_links if re.search("h4", str(tag))]

				if DO_TESTS:
					same_article_count = check_article_count(page_info_tag, href_tags, curr_url)
					assert same_article_count is True, f"ARTICLE COUNT NOT EQ : {dep_name}"

			except:
				print("ERROR:", sys.exception())
				# exit(22) # FOR TESTING, when you want errors that crash/exit early
				continue # next dep

			for tags in href_tags:
				try:
					href_str: str = str(tags)
					href: Any = re.search('(handle\/[0-9]+/[0-9]+)', href_str)
					assert href is not None, f"NO HANDLE : {tags}"

					article_url: str = f"{URL_RAW}{href.group(0)}"
					req_article: str = requests.get(article_url).text
					assert req_article is not None, f"NO ARTICLE : {article_url}"

					article_soup = BeautifulSoup(req_article, features="html.parser")
					if is_eng(article_soup):
						eng_count += 1

						title_tag: Any = article_soup.find('title')
						assert title_tag is not None, f"NO TITLE TAG : {title_tag}"

						title: str = title_tag.text
						title_nickname: str = make_uq(title)

						abs_tag: Any = article_soup.find('div', {'class': 'simple-item-view-description'})
						assert abs_tag is not None, f"NO ABSTRACT TAG : {article_url}"

						abstract: str = abs_tag.find('div').text
						clean_abs: str = ' '.join(abstract.split())

						word_count: int = len(clean_abs.split(' '))
						if word_count < 50:
							word_count_str: str = f"{word_count} : {article_url} : {title_nickname}\n"
							with open("word_count_new.txt", "a", encoding="utf-8") as f:
								f.write(word_count_str)

						# Have to store data in a folder for TAACO to do batch processing
						dir_path: str = f"{DIRP_DATA_DUMP}/{year}"
						file_name: str = create_file_name(year, dep_name, title_nickname)
						file_path: str = os.path.join(dir_path, file_name)
						with open(file_path, "w", encoding="utf-8") as f:
							f.write(clean_abs)

				except:
					print("ERROR:", sys.exception())
					# exit(22) # FOR TESTING, when you want errors that crash/exit early (but you have to activate the earlier exit(22) too
					continue # next article

		print(f"{year} | Count: {eng_count}")
		print("ABSOLUTE CODING!! \(O.O)/")

