# Sentireddit
A self hostable full stack app to provide sentiment analysis Reddit data.

![image](https://github.com/casrar/Sentireddit/assets/79720481/c258c177-829a-486e-a8db-cafa570a1fc3)
![image](https://github.com/casrar/Sentireddit/assets/79720481/43e4d7c4-e480-453a-97d8-87b809132517)
![image](https://github.com/casrar/Sentireddit/assets/79720481/82d6e7a9-7674-48ec-a6e6-e796e6e7f597)


# How to run
- Navigate to Sentiment-Stocks directory
- Run database 
  - ```database/pocketbase serve```
- Create account for database
- Run server 
  - ```cd src```
  - run ```pipenv run flask --app sentireddit.py run```
- Configure data sources on Sentireddit
- Run scraper 
  - ```cd src/comment-scraper```
  - Run ```pipenv run python main.py```



