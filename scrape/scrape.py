import sys
import re
import requests
import difflib

from bs4 import BeautifulSoup

from database import Database
import log

# Keep track of professors seen
profs_seen = {}

# Threshhold for similar names
RATIO = 0.85

# New DB isntance, defined in database.py
db = Database()

def main():
    r = requests.get('http://polyratings.com/list.php')
    html = r.text

    soup = BeautifulSoup(html, 'html.parser')
    prof_links = soup.find_all('a', {'class' : 'no-link-highlight'})
    get_ratings(prof_links)


@log.time_scrape
def get_ratings(prof_links):
    for a in prof_links:
        url = a['href']
        prof_page = requests.get(url).text
        soup = BeautifulSoup(prof_page, 'html.parser')

        try:
            prof = soup.find('h1', {'class' : 'text-primary'}).text
        # For whatever reason, prof doesnt exist, so skip
        except AttributeError:
            continue
        prof_rating = soup.find('h2', {'class' : 'text-primary'}).text[:-5]
        prof_department = soup.find_all('h4', {'class': None})[-1].text.strip()
        id = add_prof(prof, prof_rating, prof_department)
        log.log_status(prof)
        get_reviews(soup, id)


def get_reviews(page, id):
    class_groups = page.find_all('section', {'class' : 'group'})
    for group in class_groups:
        class_ = group.find('h2').text
        reviews_html = group.find_all('div', {'class' : 'subgroup'})
        reviews = parse_reviews(reviews_html, class_, id)


def parse_reviews(reviews, class_, id):
    for review in reviews:
        review_text = review.find('div', {'class' : 'eval-comment'}).text
        review_data = review.find('div', {'class' : 'eval-info'}).text
        review_data = review_data.split('\n')[1:-1]
        db.add_review(review_data, review_text, class_, id)


def add_prof(prof, rating, prof_department):
    if rating.replace('.', '').isdigit():
        rating = float(rating)
    else:
        rating = -1

    prof = normalize(prof)

    # See if the name was just a mispelling (or the same) of a previous professor
    prof_similar = check_similar(prof, profs_seen.keys())

    # To reduce false positives, make sure similar name has the same department 
    # UNLESS we have an exact match (this assumes it is more likely they are the same person
    # listed under different departments than just two people with the same name)
    other_department = profs_seen.get(prof_similar, dict()).get('department', None)
    count = 1

    if other_department == prof_department or prof == prof_similar:
        prof = prof_similar
        prof_department = other_department

        # get count (for averaging)
        count = profs_seen[prof_similar]['count']
        count += 1
        profs_seen[prof_similar]['count'] = count

        # take average of all ratings
        rating = profs_seen[prof_similar]['rating'] * (1 / count) \
            + rating * ((count - 1) / count)

        db.update_professor(prof, prof_department, rating)
        id = profs_seen[prof_similar]['id']
    else:
        id = db.add_professor(prof, prof_department, rating)

    # add/update seen table
    profs_seen[prof] = {'rating' : rating,
                        'department' : prof_department,
                        'count' : count,
                        'id' : id}
    return id



def check_similar(prof_name, prof_list):
    for prof in prof_list:
        if is_similar(prof, prof_name):
            return normalize(prof)
    return None

def is_similar(first, second):
    return difflib.SequenceMatcher(None, first, second).ratio() > RATIO


def normalize(prof):
    norm = prof.title().replace(u'\xa0', '')
    return norm


if __name__ == '__main__':
    main()