valid_grades = ['A', 'B', 'C', 'D', 'F', 'N/A', 'Credit', 'No Credit']

year_to_num = {'Freshman' : 0,
               'Sophomore' : 1,
               'Junior' : 2,
               'Senior' : 3,
               '5th Year Senior': 4,
               'Grad Student' : 5}

req_to_num = {'General Ed' : 0,
              'Major' : 1,
              'Support' : 2,
              'Elective' : 3,
              'N/A' : 4}

rating_to_num = {'F' : 0,
                 'D' : 1,
                 'C' : 2,
                 'B' : 3,
                 'A' : 4}

departments = {
    'AEPS': 'Ag and Environmental Plant Sci',
    'AERO': 'Aerospace Engineering',
    'AGB':  'Agribusiness',
    'AG':   'Agriculture',
    'AGC':  'Agricultural Communication',
    'AGED': 'Agricultural Education',
    'ANT':  'Anthropology',
    'ARCE': 'Architectural Engineering',
    'ARCH': 'Architecture',
    'ART':  'Art',
    'ASCI': 'Animal Science',
    'ASTR': 'Astronomy',
    'BIO':  'Biology',
    'BMED': 'Biomedical Engineering',
    'BOT':  'Botany',
    'BRAE': 'BioResource & Agricultural Eng',
    'BUS':  'Business',
    'CD':   'Child Development',
    'CE':   'Civil Engineering',
    'CHEM': 'Chemistry',
    'CHIN': 'Chinese',
    'CM':   'Construction Management',
    'COMS': 'Communication Studies',
    'CPE':  'Computer Engineering',
    'CRP':  'City and Regional Planning',
    'CSC':  'Computer Science',
    'DANC': 'Dance',
    'DATA': 'Data Science',
    'DSCI': 'Dairy Science',
    'ECON': 'Economics',
    'EDES': 'Environmental Design',
    'EDUC': 'Education',
    'EE':   'Electrical Engineering',
    'ENGL': 'English',
    'ENGR': 'Engineering',
    'ENVE': 'Environmental Engineering',
    'ERSC': 'Earth Science',
    'ES':   'Ethnic Studies',
    'FR':   'French',
    'ESE':  'Early Start English',
    'ESM':  'Early Start Math',
    'FSN':  'Food Science and Nutrition',
    'GEOG': 'Geography',
    'GEOL': 'Geology',
    'GER':  'German',
    'GRC':  'Graphic Communication',
    'GSB':  'Graduate Studies Business',
    'HIST': 'History',
    'HNRC': 'Honors Contract',
    'HNRS': 'Honors',
    'IME':  'Industrial & Manufacturing Eng',
    'ISLA': 'Interdisc Stds in Liberal Arts',
    'ITAL': 'Italian',
    'ITP':  'Industrial Tech and Packaging',
    'JOUR': 'Journalism',
    'JPNS': 'Japanese',
    'KINE': 'Kinesiology',
    'LA':   'Landscape Architecture',
    'LAES': 'Liberal Arts and Engr Studies',
    'LS':   'Liberal Studies',
    'MATE': 'Materials Engineering',
    'MATH': 'Mathematics',
    'MCRO': 'Microbiology',
    'ME':   'Mechanical Engineering',
    'MSCI': 'Marine Science',
    'MSL':  'Military Science Leadership',
    'MU':   'Music',
    'NR':   'Natural Resources',
    'PEM':  'Intercollegiate Athletics Men',
    'PEW':  'Intercollegiate Athletics Women',
    'PHIL': 'Philosophy',
    'PHYS': 'Physics',
    'POLS': 'Political Science',
    'PSC':  'Physical Sciences',
    'PSY':  'Psychology',
    'RELS': 'Religious Studies',
    'RPTA': 'Rec, Parks & Tourism Admin',
    'SCM':  'Science and Mathematics',
    'SOC':  'Sociology',
    'SOCS': 'Social Sciences',
    'SPAN': 'Spanish',
    'SS':   'Soil Science',
    'STAT': 'Statistics',
    'TH':   'Theatre',
    'UNIV': 'University Studies',
    'WGS':  "Women's and Gender Studies",
    'WLC':  'World Languages and Cultures',
    'WVIT': 'Wine and Viticulture',
}


departments = {
    'Crop Science': 'AEPS',
    'Environmental Horticulture Science': 'AEPS',
    'Aerospace Engineering': 'AERO'
    'Agribusiness': 'AGB',
    'Agriculture': 'AG',
    'Agricultural Education and Communication': 'AGED',
    'Architectural Engineering': 'ARCE',
    'Architecture': 'ARCH',
    'Art and Design': 'ART',
    'Animal Science': 'ASCI',
    'Biological Sciences': 'BIO',
    'Biomedical Engineering': 'BMED',
    'Bioresource and Agricultural Engineering': 'BRAE',
    'Business': 'BUS',
    'Civil and Environmental Engineering': 'CE',
    'Chemistry and Biochemistry': 'CHEM',
    'Construction Management': 'CM',
    'Communication Studies': 'COMS',
    'Computer Engineering': 'CPE',
    'City and Regional Planning': 'CRP',
    'Computer Science': 'CSC',
    'DANC'
    'DATA'
    'Dairy Science': 'DSCI',
    'Economics': 'ECON',
    'Environmental Design': 'EDES',
    'Education': 'EDUC',
    'Electrical Engineering': 'EE',
    'English': 'ENGL',
    'Engineering': 'ENGR',
    'ENVE'
    'ERSC'
    'Ethnic Studies': 'ES',
    'FR'
    'ESE'
    'ESM'
    'Food Science and Nutrition': 'FSN',
    'GEOG'
    'GEOL'
    'GER'
    'GRC'
    'Graduate Programs': 'GSB',
    'HIST'
    'HNRC'
    'HNRS'
    'IME'
    'ISLA'
    'ITAL'
    'ITP'
    'JOUR'
    'JPNS'
    'KINE'
    'LA'
    'LAES'
    'LS'
    'MATE'
    'MATH'
    'MCRO'
    'ME'
    'MSCI
    'MSL'
    'MU'
    'NR'
    'PEM'
    'PEW'
    'PHIL'
    'PHYS'
    'POLS'
    'PSC'
    'PSY'
    'RELS
    'RPTA
    'SCM'
    'SOC'
    'SOCS'
    'SPAN'
    'SS'
    'STAT
    'TH'
    'UNIV'
    'WGS'
    'WL'
    'WVIT'
}










Graduate Programs


Graphic Communication
History
Humanities
Industrial and Manufacturing Engineering
Industrial Technology
Journalism
Landscape Architecture
Liberal Studies
Materials Engineering
Mathematics
Mechanical Engineering
Military Science
Modern Languages and Literatures
Music
Natural Resources Management
Philosophy
Physical Education and Kinesiology
Physics
Political Science
Psychology and Human Development
Science and Mathematics
Social Sciences
Soil Science
Statistics
Theater and Dance
University Honors
University Library
Women's and Gender Studies
Womens Studies