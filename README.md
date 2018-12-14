# GoodPlaceBot
  

A Python Reddit Bot for modding the subreddit TheGoodPlace  


## Description:  

This is a bot written in Python 3 for reddit, specifically the subreddit r/TheGoodPlace. It uses the module reddit's API wrapper [**PRAW**](https://praw.readthedocs.io)  

It performs several actions in the sub and requires mod privileges.  


## Functions:  

### *Updating Sidebar: Next Episode Countdown*  

Module: **sidebarCountdown.py**  

With a schedule of release of episodes, it updates the sidebar of the subreddit every X amount of seconds with a **countdown** towards the next episode.  

It has an aware date with customizable timezone. It uses the **datetime** and **pytz** modules  

It has a *'grace period'* feature where if a date has passed not so long ago (for example in the last 24hs) it updates a different kind of message.  

It has 3 custom strings for the sidebar for the cases it can get into. One is the grace period message, the other is no grace period but there's a future date to count to (the most common case), and third, message where all the dates have run out.  

### *Point System* (to be implemented)  

Module: **x.py**  

With accordance to the show's story, the sub has a (in joke) point system that the bot takes care of. It reads comments and submissions and other different actions on the subreddit and weighs those with certain rules to give that user a certain amount of positive or negative points.  

Each week the bot publishes that week's top 10 "Best People" and it also updates the sidebar to show that TOP10.  

## Use:  

#### Countdown:  

The countdown is activated in the *main.py* file and uses the files *sidebarCountdown.py* and *episodeSchedule.txt.*  

**Important:** The countdown will be on the top of the sidebar and will use a line separation that markdown reads as 3 underscores "___" as a separation of the sidebar string. So everything *before* the first line separation will be lost. Ideally that would mean the previous countdown, but the first time this has to be set up by adding 3 underscores, two spaces and two newlines at the top of the sidebar. If not there will be a potential loss of information or an error  

Inside the sidebarCountdown.py file there's a variable called timeZone with a [**pytz timezone string**](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568), so to change the timezone that the program will use, look into the specific pytz string of your timezone and replace that variable. Note that the time and date of the *EpisodeSchedule.txt* must be written in that timezone.  

The *episodeSchedules.txt* is the file that stores an easily parseable string of dates and times. The format is the following  

    YYYY - MM - DD - TT:TT AM  

An example would be:  

    2017 - 12 - 03 - 08:30 PM  
    2019 - 01 - 10 - 09:30 PM
    2019 - 01 - 17 - 09:30 PM  

Note that you do not need to remove past dates as the program deals with that for you.

Finally, the main.py contains the sleep() function that tells the program how long to wait (in seconds) until it updates the sidebar again.





