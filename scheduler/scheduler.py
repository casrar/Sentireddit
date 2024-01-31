import sched, time, logging, requests, multiprocessing
from ..scraper import scraper
from dotenv import dotenv_values

config = dotenv_values(".env")
scheduler = sched.scheduler(time.monotonic, time.sleep)

def auth_to_db(config):
    # error check and log
    response = requests.post(
        'http://127.0.0.1:8090/api/collections/users/auth-with-password', 
        data={'identity': config['IDENTITY'], 'password': config['PASSWORD']}).json()
    auth_token = response['token']
    return auth_token

def get_current_delay(auth_token):
    # error check and log
    response = requests.get(
        'http://127.0.0.1:8090/api/collections/scraper_delay/records', 
        headers={'Authorization': auth_token}).json()

    if not response['totalItems'] > 0:  
        return None
    
    current_delay = response['items'][0]['scraper_delay']
    return current_delay

def run_scraper():
    scraper.main()

auth_token = auth_to_db(config)
# while True: # not functioning
#     delay = get_current_delay(auth_token)
#     if delay is None:
#         continue
#     scheduler.enter(delay, 0, run_scraper, ())
#     scheduler.run()
