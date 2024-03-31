# twitter slop poster bot

## Description
This is a project that aims to create an automated twitter account that selects random popular posts from specified subreddits and posts them on Twitter. Currently, it's configured to post from an assortment of Genshin and Honkai subreddits, but is being built to be subreddit-agnostic.

## Required Libraries
This project uses:
- PRAW
- twikit[*](https://github.com/spiiritual/twikit)
- requests
- dotenv

## Components

### Reddit 
The reddit.py file contains everything related to the reddit functionality of the slopbot. This includes the selecting of a random hot post from the specified subreddits and download images from posts.

### Twitter
The twitter.py file contains everything related to the twitter functionality of the slopbot. This includes uploading images to Twitter, generating Tweets, and posting Tweets.

### (planned) Scheduled
The scheduled.py file will contain tasks that must be run at a given interval that are **not** related to the normal posting of the slopbot, including posting new game announcements and retweeting posts from official game accounts. 

### .env file
The .env file contains the credentials needed to run the twitter and reddit portions of the slopbot. It requires the following fields to be filled, in no particular order:
- TWITTER_USERNAME
- TWITTER_EMAIL
- TWITTER_PASSWORD
- REDDIT_CLIENT_ID
- REDDIT_CLIENT_SECRET
- REDDIT_USER_AGENT

