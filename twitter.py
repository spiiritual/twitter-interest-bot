from twikit import Client
from dotenv import load_dotenv
import os

def generate_cookies():
    client = Client(language="en-US")
    client.login(
        auth_info_1=os.getenv("TWITTER_USERNAME"),
        auth_info_2=os.getenv("TWITTER_EMAIL"),
        password=os.getenv("TWITTER_PASSWORD")
    )

    client.save_cookies('cookies.json')

def upload_media_tweet(caption, image_filename):
    client = Client(language="en-US")
    client.load_cookies("cookies.json")
    media_id = []

    if isinstance(image_filename, list):
        for url in image_filename:
            media_id.append(client.upload_media(f"{url}"))
    else:
        media_id.append(client.upload_media(f"{image_filename}"))
        
    client.create_tweet(
        text=caption,
        media_ids=media_id
)
    
def get_hashtags_for_subreddit(subreddit):
    if subreddit == "r/HonkaiStarRail":
        return "#HonkaiStarRail #HSR #StarRail #崩壊スターレイル"
    else:
        return "#GenshinImpact #原神"

load_dotenv()

