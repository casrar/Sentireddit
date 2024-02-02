import requests, sched, time, logging
from utils.database import get_current_delay

def scrape() -> None:
    requests.get('127.0.0.1:5000/scrape')

def get_current_delay(auth_token):
    pass

def main() -> None:
    scheduler = sched.scheduler(time.monotonic, time.sleep)
    while True:
        delay = get_current_delay(auth_token) 
        if delay is None:
            continue
        scheduler.enter(delay=delay, priority=0, action=scrape, argument=())
        scheduler.run()

if __name__ == '__main__':
    main()