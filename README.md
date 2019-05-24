# BitsharesRealTimeAccountTracker


### Elevator Summary:
The idea for this project is to allow Dexbot users the ability to see how their MM endeavors are going in a visually explanatory manor. MM is a complex  and often times requires automation and visualizations to evaluate performance. 


### High Level Proposal
Dexbot needs the capabilities to record profit and loss, and explain the different factors at play. This will enable the end user to determine how they would evaluate the bot’s performance. For example, if your country’s currency is USD, and you are market making between BTS and OPEN.ETH and you care about value gained in terms of USD at the end of day then there are a lot of moving pieces. Generally speaking, the dexbot on relative orders, will make money through alpha; in short, alpha is taking advantage of the inefficiencies in a market. So during market making activities dexbot may gain BTS and/or ETH relative to how much was started with, but if the fluctuation in the price of BTS/USD and/or ETH/USD are negative enough to offset any gains made through alpha, then you would still be at a net loss for the day in terms of USD. These are important concepts to understand, and because we don’t know the use case for every market maker, we should supply them the metrics to evaluate the data for themselves to determine if dexbot was achieving what they wanted. I have provided a rough draft sample chart, with analysis to provide some clarity. 

![example charting](https://github.com/JRizzly/BitsharesRealTimeAccountTracker/blob/master/pics/Example%20Performance%20Analysis.jpg)

This analysis and data gathering was done quickly so I could evaluate how dexbot was working. I shared the results in some of the Telegram groups, and I was overwhelmed with replies from people interested in how I made the results. I am willing to offer my services to automate the creation of metrics for dexbot so people can run this proposed program along dexbot to see how they are doing. 

### Technical Aim
Currently, the python-bitshares api does not support api calls past 100 operations, so the idea is to use elastic search (link below) to get the initial pull of fills, then use python-bitshare once current to watch in real time. 

EWS: https://eswrapper.bitshares.eu/apidocs/#!/wrapper/get_account_history 

EWS2: https://wrapper.elasticsearch.bitshares.ws/apidocs/#!/wrapper/get_account_history

Python-bitshares documentation: https://buildmedia.readthedocs.org/media/pdf/python-bitshares/latest/python-bitshares.pdf


### Updates
This is a work in progress, and I will update readme as appropriate. 


