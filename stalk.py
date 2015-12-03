#!/usr/bin/python
import praw
import pdb
import re
import os
import time
from config_bot import *

# Check that the file that contains our username exists
if not os.path.isfile("config_bot.py"):
    print ("You must create a config file with your username and password.")
    print ("Please see config_skel.py")
    exit(1)

# Create the Reddit instance
user_agent = ("PassABot v.3")
r = praw.Reddit(user_agent=user_agent)

# and login
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)

#Karma Bot: (uncomment to use)
    # choose a user
    #user = r.get_redditor('aamfs94')
    # printing karma 
    #print (user.link_karma)
    #print (user.comment_karma)
# user to follow
user = r.get_redditor('jaxtestingbot')
#list of words
hotwords = ["/u/"]

##for comment in user.get_comments(limit=None):
##    if 'hotwords=' in str(comment.body).lower():
##        print (comment.body)
##    else:
##        print ('nothing found')

#finds the users comments
user.get_comments(limit=None)
#for comment in users comments that
for comment in user.get_comments(limit=None):
    #contain a word from the list hotwords
    for word in hotwords:
        #and if that word is in the body of the comment
        if word in comment.body:
            #print the comment body
            print (comment.body)
        #otherwise
        else:
            #print 'nada'
            print ("nada")
time.sleep(5)


