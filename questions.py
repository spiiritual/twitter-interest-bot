import random

static_questions = [
    {"type": "genshin", "question": "What is your favorite thing about Genshin?"},
    {"type": "genshin", "question": "Who is your favorite Genshin character?"},
    {"type": "genshin", "question": "Who is your least favorite Genshin character?"},
    {"type": "genshin", "question": "What do you not like about Genshin?"},
    {"type": "genshin", "question": "Which Genshin region is your personal favorite?"},
    {"type": "genshin", "question": "Who is the most interesting Genshin character?"},
    {"type": "genshin", "question": "If you could spend a day with any Genshin Impact character, who would it be and what would you do together?"},
    {"type": "genshin", "question": "In your opinion, which Genshin Impact character has the most interesting backstory?"},
    {"type": "genshin", "question":  "What is your favorite quest or storyline in Genshin Impact?"},
    {"type": "hsr", "question":  "What is your favorite thing about Honkai Star Rail?"},
    {"type": "hsr", "question":  "Who is your favorite Honkai Star Rail character?"},
    {"type": "hsr", "question":  "Who is your least favorite Honkai Star Rail character?"},
    {"type": "hsr", "question":  "What do you not like about Honkai Star Rail?"},
]

def get_random_question() -> dict[str, str]:
    return random.choice(static_questions)