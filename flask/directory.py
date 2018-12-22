import requests

directory_url = 'https://myportal.calpoly.edu/f/u36l1s13/p/directoryinfo.u36l1n24/max/action.uP?pP_action=search'

form_data = {
    'personType': 'imp',
    'simpleSearchParameters': 'john clements',
    'Submit': 'Search',
}

r = requests.post(directory_url, data=form_data)

print(r.text)