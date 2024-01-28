import sched, time, scraper

delay = 1 #  
scheduler = sched.scheduler(time.monotonic, time.sleep)
  
def run_scraper():
    scraper.main()

while True:
    # if delay not set
        # continue
    # set delay = to delay in db
    scheduler.enter(delay, 0, run_scraper, ())
    scheduler.run()
