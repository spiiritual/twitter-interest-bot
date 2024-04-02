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

def upload_media_tweet(caption : str, image_filename : list[str] | str):
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
    
def upload_text_tweet(caption : str):
    client = Client(language="en-US")
    client.load_cookies("cookies.json")

    client.create_tweet(
        text=caption
    )
    
def get_hashtags_for_subreddit(subreddit : str) -> str:
    return "#HonkaiStarRail #HSR #StarRail #崩壊スターレイル" if subreddit == "HonkaiStarRail" else "#GenshinImpact #原神"
    
def get_hashtags_for_question_type(type : str) -> str:
    return "#HonkaiStarRail #HSR #StarRail #崩壊スターレイル" if type == "hsr" else "#GenshinImpact #原神"

load_dotenv()

