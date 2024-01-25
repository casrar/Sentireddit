# Sentireddit
A self hostable full stack app to provide sentiment analysis Reddit data.

![image](https://github.com/casrar/Sentireddit/assets/79720481/4b9bc67c-e9c3-4ea7-9dd3-b6df310182af)
![image](https://github.com/casrar/Sentireddit/assets/79720481/f6778ff3-c72c-4af5-83a3-b6c3ce0864f2)
![image](https://github.com/casrar/Sentireddit/assets/79720481/39f01f78-e787-4b3b-a6de-f14b14a6b6bb)


# Setup
- Navigate to project directory
- Run database 
  - ```database/pocketbase serve```
- Create account for database
- Configure ```.env``` file in ```src/``` directory
  - ![image](https://github.com/casrar/Sentireddit/assets/79720481/51fb8aa2-8d86-4247-8f51-a83b98a298c9)
- Run server 
  - ```cd src```
  - Run ```pipenv run flask --app sentireddit.py run``` (or add ```--debug``` after ```sentireddit.py run```)
- Configure data sources on Sentireddit
- Run scraper 
  - ```cd src/comment-scraper```
  - Run ```pipenv run python main.py```



