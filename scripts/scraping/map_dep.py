from typing import Any

faculty_translator: dict[str, str] = {
	"FoE"      : "Faculty of Education",
	"FoH"      : "Faculty of Humanities",
	"FoSaT"    : "Faculty of Science and Technology",
	"FoSS"     : "Faculty of Social Science",
	"SA"       : "Sahlgrenska Academy",
	"SoBEaL"   : "School of Business, Economics and Law",
	"GS"       : "Graduate School",
	"UFL"      : "Utbildnings- och forskningsnämnden för lärarutbildning",
	"PIL"      : "Pedagogical Development and Interactive Learning",
	"PoHRDaLR" : "Programme on Human Resource Development and Labour Relation",
	"PfPoA"    : "Programmet för personal- och arbetslivsfrågor",
	"TAF"      : "The Artistic Faculty",
	"UFL"      : "Utbildnings- och forskningsnämnden för lärarutbildning",
	"Pfpoa"    : "Programmet för personal- och arbetslivsfrågor(-2010)"
}


faculty_nicknamer: dict[str, str] = {
	"Faculty of Education"                                        : "FoE",
	"Faculty of Humanities"                                       : "FoH",
	"Faculty of Science and Technology"                           : "FoSaT",
	"Faculty of Social Science"                                   : "FoSS",
	"Sahlgrenska Academy"                                         : "SA",
	"School of Business, Economics and Law"                       : "SoBEaL",
	"Graduate School"                                             : "GS",
	"Utbildnings- och forskningsnämnden för lärarutbildning"      : "UFL",
	"Pedagogical Development and Interactive Learning"            : "PIL",
	"Programme on Human Resource Development and Labour Relation" : "PoHRDaLR",
	"Programmet för personal- och arbetslivsfrågor"               : "PfPoA",
	"The Artistic Faculty"                                        : "TAF",
	"Utbildnings- och forskningsnämnden för lärarutbildning"      : "UFL",
	"Programmet för personal- och arbetslivsfrågor(-2010)"        : "Pfpoa"
}


dep_translator: dict[str, str] = {
	"AoMaD"                      : "Academy of Music and Drama",
	"DoAIT"                      : "Department of Applied Information Technology",
	"DoBaES"                     : "Department of Biological and Environmental Sciences",
	"DoBA"                       : "Department of Business Administration",
	"DoCaMB"                     : "Department of Chemistry and Molecular Biology (2012-)",
	"DoCL"                       : "Department of Comparative Literature (-2008)",
	"DoCSaE"                     : "Department of Computer Science and Engineering",
	"DoC"                        : "Department of Conservation",
	"DoCS"                       : "Department of Cultural Sciences",
	"DoES"                       : "Department of Earth Sciences",
	"DoEc"                       : "Department of Economics",
	"DoEaS"                      : "Department of Economy and Society (2013-)",
	"DoEd"                       : "Department of Education (-2010)",
	"DoEaSE"                     : "Department of Education and Special Education (2010-)",
	"DoECaL"                     : "Department of Education, Communication and Learning",
	"DoFaNaSS"                   : "Department of Food and Nutrition, and Sport Science",
	"DoHS"                       : "Department of Historical Studies",
	"DoHaEG"                     : "Department of Human and Economic Geography (-2012)",
	"DoI"                        : "Department of Informatics (-2005)",
	"DoLaL"                      : "Department of Languages and Literatures (2009-)",
	"DoL"                        : "Department of Law",
	"DoLHoIaR"                   : "Department of Literature, History of Ideas, and Religion",
	"DoMSc"                      : "Department of Marine Sciences",
	"DoMSt"                      : "Department of Mathematical Sciences",
	"DoPCaPS"                    : "Department of Pedagogical, Curricular and Professional Studies",
	"DoPaToS"                    : "Department of Philosophy,Lingustics and Theory of Science",
	"DoPS"                       : "Department of Political Science",
	"DoPs"                       : "Department of Psychology",
	"DoSW"                       : "Department of Social Work",
	"DoS"                        : "Department of Sociology (-2011)",
	"DoSaWS"                     : "Department of Sociology and Work Science",
	"DoSMLT"                     : "Department of Swedish, Multilingualism, Language Technology",
	"DoWS"                       : "Department of Work Science (-2011)",
	"GS"                         : "Graduate School",
	"HSoDaC"                     : "HDK - School of Design and Crafts (2012-2019)",
	"HVAoAaD"                    : "HDK - Valand - Academy of Art and Design (2020-)",
	"IoB"                        : "Institute of Biomedicine",
	"IoCS"                       : "Institute of Clinical Sciences",
	"IoHaCS"                     : "Institute of Health and Care Sciences",
	"IoM"                        : "Institute of Medicine",
	"IoNaP"                      : "Institute of Neuroscience and Physiology",
	"DoPh"                       : "Department of Physics",
	"JDoJMaC"                    : "JMG - Department of Journalism, Media and Communication",
	"L"                          : "Lärarutbildningsnämnden (2010-)",
	"PDaIL"                      : "Pedagogical Development and Interactive Learning",
	"PoHRDaLR"                   : "Programme on Human Resource Development and Labour Relation",
	"Pfpoa"                      : "Programmet för personal- och arbetslivsfrågor(-2010)",
	"SoBEaL"                     : "School of Business, Economics and Law",
	"SoGS"                       : "School of Global Studies",
	"SSoCaD"                     : "Steneby - School of Craft and Design (-jun 2012)",
	"TSoDaC"                     : "The School of Design and Crafts (-jun 2012)",
	"TSoFD"                      : "The School of Film Directing",
	"TSoPA"                      : "The School of Public Administration",
	"UofflU"                     : "Utbildnings- och forskningsnämnden för lärarutbildning, UFL, (-2010)",
	"VA"                         : "Valand Academy (-2019)"
}

dep_nicknamer: dict[str, str] = {
	"Academy of Music and Drama"                                           : "AoMaD" ,
	"Department of Applied Information Technology"                         : "DoAIT",
	"Department of Biological and Environmental Sciences"                  : "DoBaES",
	"Department of Business Administration"                                : "DoBA",
	"Department of Chemistry and Molecular Biology (2012-)"                : "DoCaMB",
	"Department of Comparative Literature (-2008)"                         : "DoCL",
	"Department of Computer Science and Engineering"                       : "DoCSaE",
	"Department of Conservation"                                           : "DoC",
	"Department of Cultural Sciences"                                      : "DoCS",
	"Department of Earth Sciences"                                         : "DoES",
	"Department of Economics"                                              : "DoEc",
	"Department of Economy and Society (2013-)"                            : "DoEaS",
	"Department of Education (-2010)"                                      : "DoEd",
	"Department of Education and Special Education (2010-)"                : "DoEaSE",
	"Department of Education, Communication and Learning"                  : "DoECaL",
	"Department of Food and Nutrition, and Sport Science"                  : "DoFaNaSS",
	"Department of Historical Studies"                                     : "DoHS",
	"Department of Human and Economic Geography (-2012)"                   : "DoHaEG",
	"Department of Informatics (-2005)"                                    : "DoI",
	"Department of Languages and Literatures (2009-)"                      : "DoLaL",
	"Department of Law"                                                    : "DoL",
	"Department of Literature, History of Ideas, and Religion"             : "DoLHoIaR",
	"Department of Marine Sciences"                                        : "DoMSc",
	"Department of Mathematical Sciences"                                  : "DoMSt",
	"Department of Pedagogical, Curricular and Professional Studies"       : "DoPCaPS",
	"Department of Philosophy,Lingustics and Theory of Science"            : "DoPaToS",
	"Department of Political Science"                                      : "DoPS",
	"Department of Psychology"                                             : "DoPs",
	"Department of Social Work"                                            : "DoSW",
	"Department of Sociology (-2011)"                                      : "DoS",
	"Department of Sociology and Work Science"                             : "DoSaWS",
	"Department of Swedish, Multilingualism, Language Technology"          : "DoSMLT",
	"Department of Work Science (-2011)"                                   : "DoWS",
	"Graduate School"                                                      : "GS",
	"HDK - School of Design and Crafts (2012-2019)"                        : "HSoDaC",
	"HDK - Valand - Academy of Art and Design (2020-)"                     : "HVAoAaD",
	"Institute of Biomedicine"                                             : "IoB",
	"Institute of Clinical Sciences"                                       : "IoCS",
	"Institute of Health and Care Sciences"                                : "IoHaCS",
	"Institute of Medicine"                                                : "IoM",
	"Institute of Neuroscience and Physiology"                             : "IoNaP",
	"Department of Physics"                                                : "DoPh",
	"JMG - Department of Journalism, Media and Communication"              : "JDoJMaC",
	"Lärarutbildningsnämnden (2010-)"                                      : "L",
	"Pedagogical Development and Interactive Learning"                     : "PDaIL",
	"Programme on Human Resource Development and Labour Relation"          : "PoHRDaLR",
	"Programmet för personal- och arbetslivsfrågor(-2010)"                 : "Pfpoa",
	"School of Business, Economics and Law"                                : "SoBEaL",
	"School of Global Studies"                                             : "SoGS",
	"Steneby - School of Craft and Design (-jun 2012)"                     : "SSoCaD",
	"The School of Design and Crafts (-jun 2012)"                          : "TSoDaC",
	"The School of Film Directing"                                         : "TSoFD",
	"The School of Public Administration"                                  : "TSoPA",
	"Utbildnings- och forskningsnämnden för lärarutbildning, UFL, (-2010)" : "UofflU",
	"Valand Academy (-2019)"                                               : "VA"
}

dep_to_faculty: dict[str, str] = {
	"AoMaD"    : "TAF",
	"DoAIT"    : "FoSaT",
	"DoBaES"   : "FoSaT",
	"DoBA"     : "SoBEaL",
	"DoCaMB"   : "FoSaT",
	"DoCL"     : "FoH",
	"DoCSaE"   : "FoSaT",
	"DoC"      : "FoSaT",
	"DoCS"     : "FoH",
	"DoES"     : "FoSaT",
	"DoEc"     : "SoBEaL",
	"DoEaS"    : "SoBEaL",
	"DoEd"     : "FoE",
	"DoEaSE"   : "FoE",
	"DoECaL"   : "FoE",
	"DoFaNaSS" : "FoE",
	"DoHS"     : "FoH",
	"DoHaEG"   : "SoBEaL",
	"DoI"      : "SoBEaL",
	"DoLaL"    : "FoH",
	"DoL"      : "SoBEaL",
	"DoLHoIaR" : "FoH",
	"DoMSc"    : "FoSaT",
	"DoMSt"    : "FoSaT",
	"DoPCaPS"  : "FoE",
	"DoPaToS"  : "FoH",
	"DoPS"     : "FoSaT",
	"DoPs"     : "FoSaT",
	"DoSW"     : "FoSaT",
	"DoS"      : "FoSaT",
	"DoSaWS"   : "FoSaT",
	"DoSMLT"   : "FoH",
	"DoWS"     : "FoE",
	"GS"       : "GS",
	"HSoDaC"   : "TAF",
	"HVAoAaD"  : "TAF",
	"IoB"      : "SA",
	"IoCS"     : "SA",
	"IoHaCS"   : "SA",
	"IoM"      : "SA",
	"IoNaP"    : "SA",
	"DoPh"     : "FoSaT",
	"JDoJMaC"  : "FoSaT",
	"L"        : "UFL",
	"PDaIL"    : "PIL",
	"PoHRDaLR" : "PoHRDaLR",
	"Pfpoa"    : "Pfpoa",
	"SoBEaL"   : "SoBEaL",
	"SoGS"     : "FoSaT",
	"SSoCaD"   : "TAF",
	"TSoDaC"   : "TAF",
	"TSoFD"    : "TAF",
	"TSoPA"    : "FoSaT",
	"UofflU"   : "UFL",
	"VA"       : "TAF"
}

