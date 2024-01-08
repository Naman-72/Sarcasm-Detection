import praw

reddit = praw.Reddit(client_id='LchMksVUmRUeyg', client_secret='gb1XyXX-r0ycV9KKFM-ujFVNOogO_w', user_agent='Data Scraping')

# Read submission IDs from a file
with open('ac.txt', 'r') as file:
    submission_ids = [line.strip() for line in file]

# Open a new file to write the results
with open('output_comments.txt', 'w', encoding='utf-8') as output_file:
    for submission_id in submission_ids:
        submission = reddit.submission(submission_id)

        if not submission.stickied:
            submission.comments.replace_more(limit=None)
            output_file.write(20 * '||' + '\n'+'\n'+'\n')
            for comment in submission.comments.list():
                output_file.write(20 * '-' + '\n')
                output_file.write('Parent ID: {}\n'.format(comment.parent()))
                output_file.write('Comment ID: {}\n'.format(comment.id))
                output_file.write('{}\n'.format(comment.body))
                output_file.write('Downs: {}\n'.format(comment.downs))
                output_file.write('Ups: {}\n'.format(comment.ups))
                output_file.write('\n')
