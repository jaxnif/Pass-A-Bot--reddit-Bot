#!/usr/bin/python
import praw
import os
import random
from config_bot import *


# Create the Reddit instance
user_agent = ("PassABot v.4")
r = praw.Reddit(user_agent=user_agent)

# and login
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)

with open ("username.txt", "r") as myfile:
    username=myfile.read()

with open("replied_to.txt", "r") as f:
    replied_to = f.read().splitlines()


final_name = ''
user = r.get_redditor(username)
#list of words
hotwords = "/u/"
hotcats = ['cat', 'cats', 'kitten']
hotdogs = ['dog', 'dogs', 'puppy', 'husky']



print (username)
#take responses.txt and turn it into a list
hot_lists = ['general', 'cat', 'dog']
for word in hot_lists:
    final_word = word + '_responses'
    final_file = final_word + '.txt'
    with open(final_file) as f:
        final_list = final_file[:-4]
        final_word = f.read().splitlines()

print (cat_responses)

# with open('general_responses.txt') as f:
#     general_responses = f.read().splitlines()

# with open('cat_responses.txt') as f:
#     cat_responses = f.read().splitlines()
#
# with open('dog_responses.txt') as f:
#     dog_responses = f.read().splitlines()

#list of responses should the bot be passed on
with open('final_responses.txt') as f:
    final_responses = f.read().splitlines()

comments = user.get_comments(sort='old', time='day', limit=None)
for comment in comments:
    if hotwords in comment.body and comment.id not in replied_to:
        replied_to.append(comment.id)
        print('finalresponse')
    for word in hotcats:
        if word in comment.body and comment.id not in replied_to:
            replied_to.append(comment.id)
            print('testcat')
    for word in hotdogs:
        if word in comment.body and comment.id not in replied_to:
            replied_to.append(comment.id)
            print('testcat')

with open("replied_to.txt", "w") as f:
    for comment_id in replied_to:
        f.write(comment.id + "\n")