# twitter slop poster bot

slop (/släp/) - Effortless content posted to grow on a social media platform

## Description

This is a project that aims to create an automated twitter account that selects random popular posts from specified subreddits and posts them on Twitter. Currently, it's configured to post from an assortment of Genshin and Honkai subreddits, but is being built to be subreddit-agnostic.

## How to Use?


0. Install Python, create a twitter account, create a Reddit account, create a [Reddit application](https://www.reddit.com/prefs/apps)
1. Clone the repository or [download it as zip](https://github.com/spiiritual/twitter-slopbot/archive/refs/heads/main.zip)
2. Go into the folder where you extracted/cloned it and install the python requirements by opening a command prompt in the folder and running ```python pip install -r requirements.txt```
3. Create a file called ```.env``` in the folder where the slopbot is located and fill out the details according to the .env file section in Components (scroll down)
4. Run the script by running ```python main.py [INSERT ARGUMENT HERE]```

### Arguments

```-at```: Add a twitter user to track for retweet using their @

```-ct```: Check the tracked twitter users for new retweets

```-sr```: Submit a random reddit post to twitter

```-sq```: Submit a random question to twitter

## Components

### Reddit 

The reddit.py file contains everything related to the reddit functionality of the slopbot. This includes the selecting of a random hot post from the specified subreddits and download images from posts.

### Twitter

The twitter.py file contains everything related to the twitter functionality of the slopbot. This includes uploading images to Twitter, generating Tweets, and posting Tweets.

### main.py

The main.py file is where tasks, such as uploading reddit posts to twitter, are written. Main.py is supposed to be where subreddit/topic specific details are added to the workflow, with reddit.py and twitter.py being decoupled from the given topic.

### .env file

The .env file contains the credentials needed to run the twitter and reddit portions of the slopbot. It requires the following fields to be filled, in no particular order:
- TWITTER_USERNAME
- TWITTER_EMAIL
- TWITTER_PASSWORD
- REDDIT_CLIENT_ID
- REDDIT_CLIENT_SECRET
- REDDIT_USER_AGENT





