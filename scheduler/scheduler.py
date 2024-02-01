import requests, sched, time, logging
from utils import database

def scrape() -> None:
    requests.get('')

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