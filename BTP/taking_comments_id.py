import praw

reddit = praw.Reddit(client_id='LchMksVUmRUeyg', client_secret='gb1XyXX-r0ycV9KKFM-ujFVNOogO_w', user_agent='Data Scraping')

subreddit = reddit.subreddit('sarcasm')

hot_python = subreddit.hot(limit=None)
for submission in hot_python:
    print(submission.id)
