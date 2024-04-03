import sqlite3

def create_database():
    connection = sqlite3.connect("slopbot.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE used_reddit_posts (id TEXT)")
    cursor.execute("CREATE TABLE twitter_users (screen_name TEXT, last_tweet_id)")

def add_tracked_twitter_user(screen_name : str, last_tweet_id : str):
    connection = sqlite3.connect("slopbot.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO twitter_users VALUES(?, ?)", (screen_name, last_tweet_id))

    connection.commit()

    cursor.close()
    connection.close()

def add_used_reddit_post(post_id : str):
    connection = sqlite3.connect("slopbot.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO used_reddit_posts VALUES(?)", (post_id,))

    connection.commit()
    cursor.close()
    connection.close()

def check_for_reddit_post_id(post_id : str) -> str | None:
    connection = sqlite3.connect("slopbot.db")
    cursor = connection.cursor()

    target = cursor.execute("SELECT id FROM used_reddit_posts WHERE id = ?", (post_id,)).fetchone()

    if target is not None:
        return target[0]
    else:
        return None

def get_last_tweet_id_from_tracked(screen_name : str) -> str | None:
    connection = sqlite3.connect("slopbot.db")
    cursor = connection.cursor()

    target = cursor.execute("SELECT last_tweet_id FROM twitter_users WHERE screen_name = ?", (screen_name,)).fetchone()

    cursor.close()
    connection.close()

    if target is not None:
        return target[0]
    else:
        return None

