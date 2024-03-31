from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated

def add_user_prefix(name):
    return f"u/{name}"

def add_subreddit_prefix(name):
    return f"r/{name}"

class Post(BaseModel):
    title: str
    author: Annotated[str, AfterValidator(add_user_prefix)]
    subreddit: Annotated[str, AfterValidator(add_subreddit_prefix)]
    url: str
    post_id : str

