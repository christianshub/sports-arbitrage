### What is Sports Arbitrage?

When betting on sports events, using arbitrage opportunities is a popular technique used to gain an edge against sportsbookmakers.  
The idea is simple; place one bet per each outcome with different betting companies, the bettor can make a profit regardless of the outcome. Mathematically arbitrage occurs when there are a set of odds, which represent all mutually exclusive outcomes that cover all state space possibilities (i.e. all outcomes) of an event ([wikipedia](https://en.wikipedia.org/wiki/Arbitrage_betting)).



### What does this tool do?

This tool uses [Selenium webdriver](https://www.seleniumhq.org/projects/webdriver/) to create a headless browser giving you, the user, the opportunity to read javascript data from the bookmaker websites, parse this data and extract the sorted data into a SQLite database. 

The tool will do the following 
1) Open 1xbet.com and asianodds.com using a headless browser (chrome).
2) Navigate to username and password fields on the websites and input username and password seen in AO.py and XB.py.
3) Every 10th minute scrape the websites for dates, time, teamnames and odds)
4) Parse the data and extract it to a SQlite database.



### Which sites are being scraped for data?

Currently 1xbet.com and asianodds.com is being scraped for it's data as arbitrage opportunities between the two are often occuring. 



### Requirements 

Accounts (username and password) at 1xbet.com and asianodds.com. This must go into XB.py and AO.py respectively. 


### TODO
[ ] Design patterns
  * The tool was created before I've learned about [design patterns](https://sourcemaking.com/design_patterns). It's my goal to refactor the code to follow a popular design pattern.

[ ] SOLID principles 
  * The [SOLID principles](https://en.wikipedia.org/wiki/SOLID) haven't been taken into consideration which will also be reworked in the near future.

[ ] Check betting history for profits.
[ ] Login with NemID option (semi automatic).
[ ] AutoPlace bets.
[ ] Upload stats to a website.





