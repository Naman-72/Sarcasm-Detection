import praw

reddit = praw.Reddit(client_id='LchMksVUmRUeyg', client_secret='gb1XyXX-r0ycV9KKFM-ujFVNOogO_w', user_agent='Data Scraping')

subreddit = reddit.subreddit('csk')

hot_python = subreddit.hot(limit=None)
for submission in hot_python:
    if not submission.stickied:
        submission.comment_sort = 'new'  # You can change this to other sorting options if needed
        submission.comments.replace_more(limit=None, threshold=0)

        for comment in submission.comment_forest:
            print(20 * '-')
            print('Parent ID:', comment.parent_id)
            print('Comment ID:', comment.id)
            print(comment.body)
