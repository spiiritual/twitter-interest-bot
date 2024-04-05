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

dynamic_questions = [
    "How do you feel about", 
    "Do you like", 
    "What do you like about",
    "What do you not like about"
]

dynamic_subjects = [
    {"type": "genshin", "subject": "Mondstadt"},
    {"type": "genshin", "subject": "Liyue"},
    {"type": "genshin", "subject": "Inazuma"},
    {"type": "genshin", "subject": "Sumeru"},
    {"type": "genshin", "subject": "Fontaine"},
    {"type": "genshin", "subject": "this patch"},
    {"type": "genshin", "subject": "Genshin"},
    {"type": "genshin", "subject": "the desert in Sumeru"},
    {"type": "genshin", "subject": "the gacha system"}
]

def get_random_question() -> dict[str, str]:
    choice = random.randint(0, 1)

    if choice == 0:
        return get_random_static_question()
    else:
        return get_random_dynamic_question()

def get_random_static_question() -> dict[str, str]:
    return random.choice(static_questions)

def get_random_dynamic_question() -> dict[str, str]:
    selected_question = random.choice(dynamic_questions)
    selected_subject = random.choice(dynamic_subjects)

    return {"type": selected_subject["type"], "question": f'{selected_question} {selected_subject["subject"]}?'}
