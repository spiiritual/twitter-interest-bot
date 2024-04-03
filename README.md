# twitter slop poster bot

slop (/släp/) - Effortless content posted to grow on a social media platform

## Description

This is a project that aims to create an automated twitter account that selects random popular posts from specified subreddits and posts them on Twitter. Currently, it's configured to post from an assortment of Genshin and Honkai subreddits, but is being built to be subreddit-agnostic.

## Required Libraries

This project uses:
- PRAW
- twikit*
- requests
- dotenv
- filetype

*I use a [fork of twikit](https://github.com/spiiritual/twikit) that disables randomzied user-agents, mostly because I think that 
stealthily automating Twitter isn't compatible with randomzing user agents with every usage. The regular twikit package should
work exactly the same since I only made that change, but I'm not guaranteeing anything. 

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

### (planned) Scheduled

The scheduled.py file will contain tasks that must be run at a regular interval that are **not** related to the normal posting of the slopbot, including posting new game announcements and retweeting posts from official game accounts. 





