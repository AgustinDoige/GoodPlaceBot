# GoodPlaceBot
  

A Python Reddit Bot for modding the subreddit TheGoodPlace  


# # Description:  

This is a bot written in Python 3 for reddit, specifically the subreddit r/TheGoodPlace. It uses the module reddit's API wrapper [**PRAW**](https://praw.readthedocs.io)  

It performs several actions in the sub and requires mod privileges.  


# # Functions:  

# # # *Updating Sidebar*  

Module: **sidebarCountdown.py**  

With a schedule of release of episodes, it updates the sidebar of the subreddit every X amount of seconds with a **countdown** towards the next episode.  

It has an aware date with customizable timezone. It uses the **datetime** and **pytz** modules  

# # # *Point System*  

Module: **RRRRRRRR.py**  

With accordance to the show's story, the sub has a (in joke) point system that the bot takes care of. It reads comments and submissions and other different actions on the subreddit and weighs those with certain rules to give that user a certain amount of positive or negative points.  

Each week the bot publishes that week's top 10 "Best People" and it also updates the sidebar to show that TOP10.  



