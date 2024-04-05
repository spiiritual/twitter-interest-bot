# Modifying the slopbot

If you're downloading this, it most likely means that you want to change it to fit your specific purpose. That's great! Here's how to do the modifications that will allow you to do what you want with it:

## Changing content subreddits

If you're trying to adapt the bot to an interest other than Genshin and Honkai, you'll need to change the subreddits that the bot fetches content from. For now, you'll have to edit the main.py file. Inside the ```submit_reddit_post_for_twitter``` function, you'll see this line of code:

```
post = reddit.select_random_top_post("Genshin_Impact+HonkaiStarRail+Genshin_Memepact", ["Fluff","Meme / Fluff"])
```

The first argument that the ```select_random_top_post``` takes is a string that contains the name of the subreddit you want to fetch from. You can fetch from multiple subreddits at once by adding ```+``` between their names. The second argument is an array with strings that represent the flairs that you want to filter by in the posts. If you don't want to filter by flairs, just omit the array.

## Adding and removing questions

You can add, remove, and edit questions that the bot will ask in the questions.py file located in ```modules/questions.py```.

Questions are classified as static or dynamic. Static questions are ones that don't have a subject to be plugged in. Dynamic questions are questions that need a subject to be plugged in to make sense. 

