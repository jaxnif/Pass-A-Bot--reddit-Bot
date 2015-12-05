#!/usr/bin/python
import praw
import pdb
import re
import os
import time
import random
import string
import fileinput
from config_bot import *


# Check that the file that contains our username exists
if not os.path.isfile("config_bot.py"):
    print ("You must create a config file with your username and password.")
    print ("Please see config_skel.py")
    exit(1)


# Create the Reddit instance
user_agent = ("PassABot v.4")
r = praw.Reddit(user_agent=user_agent)

# and login
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)

with open ('username.txt', 'r') as myfile:
    username=myfile.read()
final_name = ''
user = r.get_redditor(username)
#list of words
hotwords = ["/u/"]
hotcats = ['cat', 'cats', 'kitten']
hotdogs = ['dog', 'dogs', 'puppy', 'husky']
print (username)
#take responses.txt and turn it into a list
with open('general_responses.txt') as f:
    general_responses = f.read().splitlines()
    
with open('cat_responses.txt') as f:
    cat_responses = f.read().splitlines()
    
with open('dog_responses.txt') as f:
    dog_responses = f.read().splitlines()

#list of responses should the bot be passed on
with open('final_responses.txt') as f:
    final_responses = f.read().splitlines()
    
#finds the users comments
user.get_comments(limit=None)
#for comment in users comments that
for comment in user.get_comments(limit=None):
    #contain a word from the list hotwords
    for word in hotwords:
        #and if that word is in the body of the comment
        if word in comment.body:
            #print the comment body
            body = comment.body
            #gets string "/u/username ....*rest of comment*"
            new_name = body.split('/u/')[1]
            #takes the /u/username and takes it and gives back username
            final_name = new_name.split(' ',1)[0]
            print (final_name)
            #prints random final response
            #switch to comment.reply for deployment
            print (random.choice(final_responses))
        #otherwise
    for word in hotcats:
        if word in comment.body:
            #switch to comment.reply for deployment
            print (random.choice(cat_responses))
    for word in hotdogs:
        if word in comment.body:
            #switch to comment.reply for deployment
            print (random.choice(dog_responses))
print (username)
print (final_name)

with open ('username.txt', 'w') as myfile:
    myfile.write(final_name)
with open ('username.txt', 'w') as myfile:
    username = myfile.read()
print (username)

