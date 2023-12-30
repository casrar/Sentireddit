# Sentireddit
A self hostable full stack app to provide sentiment analysis Reddit data.

![image](https://github.com/casrar/Sentireddit/assets/79720481/4b9bc67c-e9c3-4ea7-9dd3-b6df310182af)
![image](https://github.com/casrar/Sentireddit/assets/79720481/76a4bc9c-7073-4e66-b589-9112162620e9)
![image](https://github.com/casrar/Sentireddit/assets/79720481/078b1e3f-00ae-4463-bb9b-14c4a27f131a)


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



