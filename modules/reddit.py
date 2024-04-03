import praw
import random
import requests
import filetype
import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from modules.database import add_used_reddit_post, check_for_reddit_post_id
from praw.models import Submission


def get_top_posts(subreddit : str, flairs : list[str] | None) -> list[Submission]:
    reddit = create_reddit_instance()

    top_posts = []

    for post in reddit.subreddit(subreddit).hot(limit=None):
        if (post.score > 1000 and not post.over_18 and check_if_post_is_old(post.created_utc) and not post.is_self):
            if flairs is not None:
                if post.link_flair_text in flairs:
                    top_posts.append(post)
            else:
                top_posts.append(post)

    return top_posts


def check_if_post_is_old(post_creation_time : str) -> bool:
    difference = datetime.now(timezone.utc) - datetime.fromtimestamp(
        post_creation_time, timezone.utc
    )
    difference_in_hours = difference.total_seconds() / 3600
    comparator = 18

    if difference_in_hours < comparator:
        return True
    else:
        return False


def select_random_top_post(subreddit : str, flairs : list[str] | None = None) -> Submission:
    posts = get_top_posts(subreddit, flairs)
    chosen_post = None

    while True:
        post = random.choice(posts)

        if check_for_reddit_post_id(post_id=post.id) is not None:
            continue
        else:
            chosen_post = post
            add_used_reddit_post(chosen_post.id)
            break

    return chosen_post

def download_post_image(post) -> str:
    post_url = post.url
    post_id = post.id
    headers = {
        'User-Agent': os.getenv("REDDIT_USER_AGENT")
    }

    r = requests.get(post_url, headers=headers)
    if r.status_code == 200:
        image_type = get_filetype_of_file(r.content)
        if image_type:
            filename = f"temp/{post_id}.{image_type}"
            with open(filename, "wb") as f:
                f.write(r.content)
            return filename

def get_image_urls_from_gallery(post : Submission) -> list[str]:
    gallery = []
    media_ids = [i["media_id"] for i in post.gallery_data["items"]]

    for id in media_ids:
        url = post.media_metadata[id]["p"][0]["u"]
        url = url.split("?")[0].replace("preview", "i")
        gallery.append(url)

    return gallery


def download_images_from_gallery(post : Submission) -> list[str]:
    image_filenames = []
    image_urls = get_image_urls_from_gallery(post)
    headers = {
        'User-Agent': os.getenv("REDDIT_USER_AGENT")
    }

    for i, url in enumerate(image_urls):
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            image_type = get_filetype_of_file(r.content)
            if image_type:
                filename = f"temp/{post.id}-{i}.{image_type}"
                with open(filename, "wb") as f:
                    f.write(r.content)
                image_filenames.append(filename)

    return image_filenames

def get_filetype_of_file(content : bytes) -> str:
    return filetype.guess_extension(content)

def create_reddit_instance() -> praw.reddit:
    load_dotenv()
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )

