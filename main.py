import reddit
import twitter
import os

def submit_reddit_post_for_twitter():
    post = reddit.select_random_top_post()

    if hasattr(post, "gallery_data"):
        image_filename = reddit.download_images_from_gallery(post)
    else:
        image_filename = reddit.download_post_image(post)
    twitter.upload_media_with_tweet(post, image_filename)
    os.remove(image_filename)

submit_reddit_post_for_twitter()
