# PolyProfessors
The source code for polyprofessors.com.

This repository contains three folders: vue, flask, and scrape.

Vue contains all vue (frontend) related files.
Flask contains all flask (backend) related files.
Scape contains all the PolyRatings scraping code.

This website operates using a RESTful API implemented using flask. You can currently find all endpoints in routes.py. I may or may not make this API public in the future.

The frontend was built using Vue CLI 3.

To get the PolyRatings scraping scripts running you simply need the Python libraries BeautiulSoup and mysql.connector. Both can be installed using pip. Once installed, run  ```python scrape.py```. Note that you must have a mysql installed with a databse named "poly_professors" and the init.sql executed.
