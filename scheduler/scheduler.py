import requests, sched, time, logging
from utils.database import auth_with_password

def scrape() -> None:
    requests.get('127.0.0.1:5000/scrape') # should be set as an env variable

def get_current_delay() -> int:
    auth_token = auth_with_password() # params come from env variable
    if auth_token == None:
        return auth_token
    try:
        response = requests.get(url=f'{env}/api/collections/scraper_delay_records', #replace with env
                                headers={'Authorization': auth_token}).json()
    except:
        logging.warning('Error with request, 400')
        return None
    if not response['totalItems'] > 0:
        return None

    return response['items'][0]['scraper_delay']

def main() -> None:
    scheduler = sched.scheduler(time.monotonic, time.sleep)
    while True:
        delay = get_current_delay() 
        if delay is None:
            continue
        scheduler.enter(delay=delay, priority=0, action=scrape, argument=())
        scheduler.run()

if __name__ == '__main__':
    main()