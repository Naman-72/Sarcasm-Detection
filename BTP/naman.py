import praw

reddit = praw.Reddit(client_id='LchMksVUmRUeyg', client_secret='gb1XyXX-r0ycV9KKFM-ujFVNOogO_w', user_agent='Data Scraping')

# Read submission IDs from a file
with open('comments.txt', 'r') as file:
    submission_ids = [line.strip() for line in file]

# Open a new file to write the results

for submission_id in submission_ids:
    submission = reddit.submission(submission_id)
    # print(vars(submission))
    # print(dir(submission))
    print("Title : "+ submission.title + ", Author : "+str(submission.author)+ ", Comments : "+str(submission.num_comments)+", Score : "+str(submission.score)+", ID :"+str(submission.id))
    print(30*'+')
    submission.comments.replace_more(limit=None)
    comment_queue = submission.comments[:]  # Seed with top-level
    while comment_queue:
        comment = comment_queue.pop(0)
        print("Body : "+ comment.body +", ID : "+str(comment.id)+ ", Author : "+str(comment.author)+", Score : "+str(comment.score)+", Parent ID:"+str(comment.parent_id))
        print(30*'-')
        comment_queue.extend(comment.replies)
    print("\n")
    print(60*'_')