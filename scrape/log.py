import time
from time import gmtime, strftime

def time_scrape(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        curr_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print("[{}] Starting PolyRatings scrape...".format(curr_time))
        function(*args, **kwargs)
        end_time = time.time()
        print("[{}] Scrape complete.".format(curr_time))
        print("Scrape took {0:.3f} seconds.".format(end_time - start_time))
    return wrapper

# Format date so that it fits into DB DATE type
def minutes_past_midnight(t):
    try:
        PM = t[-2:] == 'PM'
        (h, m) = t[:-3].split(':')
    except:
        return None
    h = int(h)
    if PM and h != 12:
        h += 12
    return "{}:{}:{}".format(h, m, '00')


def log_status(current_read):
    curr_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print(f'[{curr_time}] Inserting reviews from {current_read}')
