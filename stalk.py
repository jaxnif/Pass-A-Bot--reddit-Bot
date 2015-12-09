#!/usr/bin/python
import praw
import random
import time
import string
from config_bot import *

# reddit Stuff:
user_agent = ("PassABot v.7")
r = praw.Reddit(user_agent=user_agent)
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)
with open ("username.txt", "r") as f:
    username = f.read()
user = r.get_redditor(username)
# end of reddit stuff

with open("previous_time.txt", "r") as f:
    previous_time = f.read()

previous_time = float(previous_time)

with open("replied_to.txt", "r") as f:
    replied_to = f.read().splitlines()

#list of words
hotword = "/u/"
hotcats = ['cat', 'cats', 'kitten']
hotdogs = ['dog', 'dogs', 'puppy', 'husky']

blacklist = [' ', 'jaxtestingbot']
final_files = ['general_responses.txt', 'cat_responses.txt', 'dog_responses.txt', 'final_responses.txt']
responses = {}
for word in final_files:
    with open(word) as f:
        word = word[:-4]
        responses[word] = f.read().splitlines()

current_time = time.time()

comments = user.get_comments(sort='old', time='all', limit=None)

for comment in comments:
    if comment.created_utc > previous_time:
        if hotword in comment.body and comment.id not in replied_to:
            result = comment.body.split('/u/',1)[1]
            result = result.split('\n',1)[0]
            result = result.split(' ',1)[0]
            result = "".join(l for l in result if l not in string.punctuation)
            username = result
            comment.reply(username + ' is the new target')
            replied_to.append(comment.id)
            comment.reply(random.choice(responses['final_responses']))
            if result not in blacklist:
                with open("replied_to.txt", "w") as f:
                    for comment.id in replied_to:
                        f.write(comment.id + "\n")
                with open("username.txt", "w") as f:
                    f.write(username)
                with open("previous_time.txt", "w") as f:
                    f.write(str(comment.created_utc))
                quit()
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
with open("username.txt", "w") as f:
    f.write(username)

quit()