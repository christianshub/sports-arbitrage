### What is Sports Arbitrage?

When betting on sports events, using arbitrage opportunities is a popular technique used to gain an edge against sportsbookmakers.  
The idea is simple; place one bet per each outcome with different betting companies, the bettor can make a profit regardless of the outcome. Mathematically arbitrage occurs when there are a set of odds, which represent all mutually exclusive outcomes that cover all state space possibilities (i.e. all outcomes) of an event ([wikipedia](https://en.wikipedia.org/wiki/Arbitrage_betting)).

Professional bettors are currently paying for a subscription at https://www.oddstorm.com/ to get arbitrage opportunities. If you are willing to do it on your own, this repo may save you some time.

### What does this tool do?

The tool scrapes for odds at (currently) two bookmaker websites and stores the data in a database.

We use [Selenium webdriver](https://www.seleniumhq.org/projects/webdriver/) to create a headless browser giving you, the user, the opportunity to read javascript data from the bookmaker websites, parse this data and extract the sorted data into a SQLite database. 

The tool will do the following 
1) Open 1xbet.com and asianodds.com using a headless browser (chrome).
2) Navigate to username and password fields on the websites and input username and password seen in AO.py and XB.py.
3) Every 10th minute scrape the websites for dates, time, teamnames and odds)
4) Parse the data and extract it to a SQlite database.



### Which sites are being scraped for data?

Currently 1xbet.com and asianodds.com is being scraped for it's data as arbitrage opportunities between the two are often occuring. 



### Requirements 

Accounts (username and password) at 1xbet.com and asianodds.com. This must go into XB.py and AO.py respectively. 





