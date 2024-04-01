import reddit
import twitter
import questions
import os

def submit_reddit_post_for_twitter():
    post = reddit.select_random_top_post()

    if hasattr(post, "gallery_data"):
        image_filename = reddit.download_images_from_gallery(post)
    else:
        image_filename = reddit.download_post_image(post)
    twitter.upload_reddit_tweet(post, image_filename)
    os.remove(image_filename)

def submit_question_on_twitter():
    random = questions.get_random_question()



submit_reddit_post_for_twitter()
