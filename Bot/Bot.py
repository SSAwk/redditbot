#Simple automated reply bot
import praw
import config
import os
import time

def login():
	print("Logging in.")
	r = praw.Reddit(username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = "MissingSources's Bot v0.1")
	print("Login successful.")
	return r
		
def run(r, replied):
	print("Searching comments.")
	replied = []
	for comment in r.subreddit('test').comments(limit=10):
		if "!Fluff" in comment.body and comment.id not in replied and comment.author != r.user.me():
			print("Command called in comment " + comment.id)
				comment.reply("[For](https://media.giphy.com/media/wZfNWF8Y6f4Bi/giphy.gif)[ you, ](http://i.imgur.com/MqGBqZs.gif)[friend!](http://i.imgur.com/8VPNV2H.gifv)")
			print("Reply sent to " + comment.id)
			replied.append(comment.id)
			with open("replied.txt", "a"):
				f.write(comment.id + "\n")
	print("Sleeping for 30 seconds.")
	time.sleep(30)
	
def save():
	if not os.path.isfile("replied.txt"):
		replied = []
	else:
		with open("replied.txt", "r") as f:
			replied = f.read()
			replied = replied.split("\n")
			replied = filter(None, replied)
	return replied
	
r = login()
replied = save()

while True:
	run(r, replied)
