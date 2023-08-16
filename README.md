# Sentireddit
A self hostable full stack app to provide sentiment analysis Reddit data.

# TODO
- Update syntax for calling APIs, very hacky
- QOL for scraping
  - Add cron jobs
  - User config parameters (time_filter, log errors/handling, etc.)
- QOL for front end
  - Multipage (Intro, Data Source Management, Data Analysis)
  - ~~Method to remove datasources~~
    - Fix bug where data source remains in selectbox after deletion
    - Rework logic to reduce coupling (ex: sentiment values error if nothing selected)
  - Method to call scraping logic from frontend
- Clean up comments
- Prefer logging
- Refactor (var names, file names, logic, etc)
- ...  
- Create config script
- Look into faster ways of searching, either web scraping or .info method (from PRAW)
- Research Docker



