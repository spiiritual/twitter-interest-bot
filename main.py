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

    if image_filename is not None:
        caption = f'"{post.title}"\n\nOn r/{post.subreddit.display_name} by u/{post.author.name}\n\n{twitter.get_hashtags_for_subreddit(post.subreddit.display_name)}'
        twitter.upload_media_tweet(caption, image_filename)
        os.remove(image_filename)
    else:
        submit_question_on_twitter() 
        # eventually find a way to fix the none error, for now just give up

       
def submit_question_on_twitter():
    random = questions.get_random_question()
    hashtags = twitter.get_hashtags_for_question_type(random["type"])
    caption = f"{random["question"]}\n\n{hashtags}"

    twitter.upload_text_tweet(caption)

submit_reddit_post_for_twitter()
