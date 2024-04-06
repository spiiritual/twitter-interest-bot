from twikit import Client, Tweet
from twikit.utils import build_query, SearchOptions, Result
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

def get_last_tweet_id(user_name: str) -> str:
    client = Client(language="en-US")
    client.load_cookies("cookies.json")

    target = client.get_user_by_screen_name(user_name)
    tweets = target.get_tweets(tweet_type="Tweets", count=1)

    return tweets[0].id

def retweet(tweet_id : str) -> None:
    client = Client(language="en-US")
    client.load_cookies("cookies.json")

    client.retweet(tweet_id)

def reply_to_tweet(tweet_id : str, text : str) -> None:
    client = Client(language="en-US")
    client.load_cookies("cookies.json")

    tweet = client.get_tweet_by_id(tweet_id)

    tweet.reply(text)

def get_popular_tweets_from_hashtag(hashtag : str | list[str]) -> Result[Tweet]:
    client = Client(language="en-US")
    client.load_cookies("cookies.json")

    if isinstance(hashtag, list):
        search_options = SearchOptions(
            hashtags=hashtag
        )
    else:
        search_options = SearchOptions(
            hashtags=[hashtag]
        )
    
    query = build_query(text="", options=search_options)
    return client.search_tweet(query, 'Top')

    

def get_hashtags_for_subreddit(subreddit : str) -> str:
    return "#HonkaiStarRail #HSR #StarRail #崩壊スターレイル" if subreddit == "HonkaiStarRail" else "#GenshinImpact #原神"
    
def get_hashtags_for_question_type(type : str) -> str:
    return "#HonkaiStarRail #HSR #StarRail #崩壊スターレイル" if type == "hsr" else "#GenshinImpact #原神"

load_dotenv()



