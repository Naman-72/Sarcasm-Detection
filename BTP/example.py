# import praw

# reddit = praw.Reddit(client_id='LchMksVUmRUeyg', client_secret='gb1XyXX-r0ycV9KKFM-ujFVNOogO_w', user_agent='Data Scraping')


# submission = reddit.submission("3v6iq7")

# if not submission.stickied:
#     # print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,submission.ups,submission.downs,submission.visited))
#     submission.comments.replace_more(limit=0)

#     for comment in submission.comments.list() :
#         print(20*'-')
#         print ('Parent ID:', comment.parent())
#         print ('Comment ID:', comment.id)
#         print (comment.body+" " +str(comment.downs)+" "+str(comment.ups))

import praw

reddit = praw.Reddit(client_id='LchMksVUmRUeyg', client_secret='gb1XyXX-r0ycV9KKFM-ujFVNOogO_w', user_agent='Data Scraping')

submission = reddit.submission("3v6iq7")

if not submission.stickied:
    submission.comment_limit = 5000  # Adjust this limit based on your needs
    submission.comments.replace_more(limit=None)

    for comment in submission.comments.list():
        if isinstance(comment, praw.models.MoreComments):
            continue  # Skip instances of "load more comments"
        
        print(20 * '-')
        print('Parent ID:', comment.parent_id)
        print('Comment ID:', comment.id)
        print(comment.body + " " + str(comment.downs) + " " + str(comment.ups))
