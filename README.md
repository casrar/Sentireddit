# Sentireddit
A self hostable full stack app to provide sentiment analysis Reddit data.

![image](https://github.com/casrar/Sentireddit/assets/79720481/34eba270-ed99-439b-bca8-ea4906a0d1c5)
![image](https://github.com/casrar/Sentireddit/assets/79720481/30bf87a8-0459-4f17-8faa-c0f0792255d6)
![image](https://github.com/casrar/Sentireddit/assets/79720481/fee06da5-652a-4a68-9b55-4dfba5bac381)

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



