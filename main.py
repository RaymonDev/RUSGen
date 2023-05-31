
import os
import bart_large_cnn_samsum
import praw
from tqdm import tqdm

# reddit object
reddit = praw.Reddit(
)


# user object
user = input("Enter a username: ")
print("\n")
user = reddit.redditor(user)

#delete the txt files if they already exist
if os.path.exists("user_data.txt"):
    os.remove("user_data.txt")
if os.path.exists("summarized.txt"):
    os.remove("summarized.txt")




#create a txt file with the name of the columns as first row, separated by commas
with open('user_data.txt', 'w') as f:
    f.write("username, title, selftext, num_comments\n")

    print("Writing to file...")
    #for every submission in the user's history, write a row to the txt file, separated by commas. Everything has to be strings
    for submission in tqdm(user.submissions.new(limit=None)):
        f.write(str(user.name) + ",")
        f.write(str(submission.title) + ",")
        f.write(str(submission.selftext) + ",")
        f.write(str(submission.num_comments) + ",")
        f.write("\n")


#save the text of "user_data.txt" to a variable
with open('user_data.txt', 'r') as f:
    data = f.read()

#call bart_large_cnn_samsum.py and pass the text of "user_data.txt" as an argument
summarized = bart_large_cnn_samsum.summarize(data)


#append the summarized text to another file called "summarized.txt"
with open('summarized.txt', 'a') as f:

    #write the username as the first line
    f.write(user.name + "\n")
    #write the summarized text as the second line with "\n" as the separator after each full stop
    f.write("\n".join(summarized.split(".")))
    f.write("\n\n")

#print the summarized text, with "\n" as the separator after each full stop
print("\n".join(summarized.split(".")))










