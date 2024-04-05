import os
import argparse
import random

import modules.reddit as reddit
import modules.twitter as twitter
import modules.questions as questions
import modules.database as database

def submit_reddit_post_for_twitter():
    print("Submiting reddit post for twitter...")
    post = reddit.select_random_top_post("Genshin_Impact+HonkaiStarRail+Genshin_Memepact", ["Fluff", "Meme / Fluff"])

    if hasattr(post, "gallery_data"):
        image_filename = reddit.download_images_from_gallery(post)
    else:
        image_filename = reddit.download_post_image(post)

    if image_filename is not None:
        caption = f"{post.title}\n\nOn r/{post.subreddit.display_name} by u/{post.author.name}\n\n{twitter.get_hashtags_for_subreddit(post.subreddit.display_name)}"
        twitter.upload_media_tweet(caption, image_filename)
        os.remove(image_filename)
    else:
        submit_question_on_twitter() 
        # eventually find a way to fix the none error, for now just give up
    
       
def submit_question_on_twitter():
    print("Submiting question for twitter...")
    random = questions.get_random_question()
    hashtags = twitter.get_hashtags_for_question_type(random['type'])
    caption = f"{random['question']}\n\n{hashtags}"

    twitter.upload_text_tweet(caption)

def submit_random():
    choice = random.randint(1, 10)

    if choice <= 8:
        submit_reddit_post_for_twitter()
    else:
        submit_question_on_twitter()
    

def check_and_retweet_tracked_users():
    target = database.get_tracked_twitter_users()

    if target is not None:
        for account in target:
            last_posted_tweet = twitter.get_last_tweet_id(account[0])
            if account[1] != last_posted_tweet:
                twitter.retweet(last_posted_tweet)
            else:
                print(f"No new tweets from {account[0]}")
    else:
        print("OY ADD SOME TRACKED ACCOUNTS FIRST")


if __name__ == "__main__":
    if not os.path.isfile("cookies.json"):
        twitter.generate_cookies()
    
    if not os.path.isfile("slopbot.db"):
        database.create_database()
    
    if not os.path.isdir("temp"):
        os.mkdir("temp")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-at", "--add-tracked-user", type=str, help="Add a twitter user to track for retweet using their @")
    parser.add_argument("-ct", "--checked-tracked-users", action='store_true', help="Check the tracked twitter users for new retweets")
    parser.add_argument("-sr", "--submit-reddit-post", action='store_true', help="Submit a random reddit post to twitter")
    parser.add_argument("-sq", "--submit-question", action='store_true', help="Submit a random question to twitter")
    parser.add_argument("-r", "--random", action='store_true', help="Randomly submit a question or reddit post to twitter")
    args = parser.parse_args()

    if args.add_tracked_user:
         last_id = twitter.get_last_tweet_id(args.add_tracked_user)
         database.add_tracked_twitter_user(args.add_tracked_user, last_id)
    
    if args.checked_tracked_users:
        check_and_retweet_tracked_users()

    if args.submit_reddit_post:
        submit_reddit_post_for_twitter()

    if args.submit_question:
        submit_question_on_twitter()
        
    if args.random:
        submit_random()
