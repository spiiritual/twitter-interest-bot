import reddit
import twitter
import model
import requests
import os

def submit_reddit_post_for_twitter():
    post = reddit.get_top_posts()
    print(vars(post))
    image_filename = reddit.download_post_image(post.url, post.id)
    twitter.upload_media_with_tweet(post, image_filename)
    os.remove(image_filename)

submit_reddit_post_for_twitter()