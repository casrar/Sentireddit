import requests, sched, time, os
from utils.database.database import auth_with_password
from utils.logger.logger import get_logger

logger = get_logger()

def scrape() -> None:
    try:
        requests.post(os.getenv('SCRAPER_URL') + '/scrape')
    except Exception as e:
        logger.critical(f'Error with scrape(): {e}')

def get_current_delay() -> int:
    auth_token = auth_with_password(os.getenv('DB_URL'), os.getenv('DB_IDENTITY'), os.getenv('DB_PASSWORD'))
    if auth_token is None:
        return auth_token
    try:
        response = requests.get(url=os.getenv('DB_URL') + '/api/collections/scraper_delay/records', 
                                headers={'Authorization': auth_token}).json()
        if response.get('totalItems') is None:
            return None
        response = response['items'][0]['scraper_delay']
    except Exception as e:
        logger.warning(f'Error with get_current_delay(): {e}')
        return None
    return response

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