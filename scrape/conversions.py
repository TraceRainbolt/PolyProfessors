# This file contains useful dictionaries for converting strings
# to the values that will be stored in the database

year_to_num = {'Freshman' : 0,
               'Sophomore' : 1,
               'Junior' : 2,
               'Senior' : 3,
               '5th Year Senior': 4,
               'Graduate Student' : 5}

req_to_num = {'General Ed' : 0,
              'Required (Major)' : 1,
              'Required (Support)' : 2,
              'Elective' : 3,
              'N/A' : 4}

month_to_num = { 'Jan' : 1,
                 'Feb' : 2,
                 'Mar' : 3,
                 'Apr' : 4,
                 'May' : 5,
                 'Jun' : 6,
                 'Jul' : 7,
                 'Aug' : 8,
                 'Sep' : 9,
                 'Oct' : 10,
                 'Nov' : 11,
                 'Dec' : 12 }


# Polyratings uses an outdated list of departments
# Below is a dictionary to convert them to their 4 letter initials
# Some departments have been renamed, combined, or removed.
# In these cases, I put what I figured was a close match
departments = {
    'Crop Science': 'AEPS',
    'Environmental Horticulture Science': 'AEPS',
    'Aerospace Engineering': 'AERO',
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
    'Dairy Science': 'DSCI',
    'Economics': 'ECON',
    'Environmental Design': 'EDES',
    'Education': 'EDUC',
    'Electrical Engineering': 'EE',
    'English': 'ENGL',
    'Engineering': 'ENGR',
    'Ethnic Studies': 'ES',
    'Food Science and Nutrition': 'FSN',
    'Graphic Communication': 'GRC',
    'Graduate Programs': 'GSB',
    'History': 'HIST',
    'University Honors': 'HNRS',
    'Industrial and Manufacturing Engineering': 'IME',
    'Industrial Technology': 'ITP',
    'Journalism': 'JOUR',
    'Physical Education and Kinesiology': 'KINE',
    'Landscape Architecture': 'LA',
    'Liberal Studies': 'LS',
    'Materials Engineering': 'MATE',
    'Mathematics': 'MATH',
    'Mechanical Engineering': 'ME',
    'Military Science': 'MSL',
    'Music': 'MU',
    'Natural Resources Management': 'NR',
    'Philosophy': 'PHIL',
    'Physics': 'PHYS',
    'Political Science': 'POLS',
    'Psychology and Human Development': 'PSY',
    'Science and Mathematics': 'SCM',
    'Humanities': 'SOC',
    'Social Sciences': 'SOCS',
    'Soil Science': 'SS',
    'Statistics': 'STAT',
    'Theater and Dance': 'TH',
    "Women's and Gender Studies": 'WGS',
    'Womens Studies': 'WGS',
    'Modern Languages and Literatures': 'WLC'
}