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
hotword = "/u/"
hotcats = ['cat', 'cats', 'kitten']
hotdogs = ['dog', 'dogs', 'puppy', 'husky']

# with open('general_responses.txt') as f:
#     general_responses = f.read().splitlines()
#
# with open('cat_responses.txt') as f:
#     cat_responses = f.read().splitlines()
#
# with open('dog_responses.txt') as f:
#     dog_responses = f.read().splitlines()
#
# with open('final_responses.txt') as f:
#     final_responses = f.read().splitlines()

final_files = ['general_responses.txt', 'cat_responses.txt', 'dog_responses.txt', 'final_responses.txt']
responses = {}
for word in final_files:
    with open(word) as f:
        word = word[:-4]
        responses[word] = f.read().splitlines()

print (responses['cat_responses'])

comments = user.get_comments(sort='old', time='day', limit=None)
for comment in comments:
    if hotword in comment.body and comment.id not in replied_to:
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