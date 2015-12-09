#!/usr/bin/python
import praw
import random
import time
from config_bot import *


# reddit Stuff:
user_agent = ("PassABot v.4")
r = praw.Reddit(user_agent=user_agent)
# and login
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)
with open ("username.txt", "r") as myfile:
    username = myfile.read()
user = r.get_redditor(username)
# end of reddit stuff

with open("replied_to.txt", "r") as f:
    replied_to = f.read().splitlines()


#list of words
hotword = "/u/"
hotcats = ['cat', 'cats', 'kitten']
hotdogs = ['dog', 'dogs', 'puppy', 'husky']

final_files = ['general_responses.txt', 'cat_responses.txt', 'dog_responses.txt', 'final_responses.txt']
responses = {}
for word in final_files:
    with open(word) as f:
        word = word[:-4]
        responses[word] = f.read().splitlines()

current_time = time.time()

comments = user.get_comments(sort='old', time='day', limit=None)

for comment in comments:
    # post has to be 24hours old or newer
    if current_time - comment.created_utc <= 86400:
        if hotword in comment.body and comment.id not in replied_to:
            replied_to.append(comment.id)
            print(random.choice(responses['final_responses']))
        for word in hotcats:
            if word in comment.body and comment.id not in replied_to:
                replied_to.append(comment.id)
                print(random.choice(responses['cat_responses']))
        for word in hotdogs:
            if word in comment.body and comment.id not in replied_to:
                replied_to.append(comment.id)
                print(random.choice(responses['dog_responses']))

with open("replied_to.txt", "w") as f:
    for comment.id in replied_to:
        f.write(comment.id + "\n")