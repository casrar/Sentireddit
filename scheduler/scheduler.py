import requests, sched, time, os
from typing import Optional
from utils.database.database import auth_with_password
from utils.logger.logger import get_logger

logger = get_logger()

def scrape() -> None:
    try:
        response = requests.post(os.getenv('SCRAPER_URL') + '/scrape')
        response.raise_for_status()
    except Exception as e:
        logger.critical(f'Error with scrape(): {e}')

def get_current_delay() -> Optional[int]:
    try:
        auth_token = auth_with_password(os.getenv('DB_URL'), os.getenv('DB_IDENTITY'), os.getenv('DB_PASSWORD'))
        response = requests.get(url=os.getenv('DB_URL') + '/api/collections/scraper_delay/records', 
                                headers={'Authorization': auth_token})
        response.raise_for_status()
        response = response.json()
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