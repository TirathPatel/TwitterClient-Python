import tweepy
from pprint import pprint
from Tkinter import *
import json


consumer_key = 'OsA1h78gDVIvgL9TNLXdPBn9E'
consumer_secret = 'gq6PWkyBqgu7VCiUcn6vtOK2ZixxCTFCXFmgNqxRcL2Qy9ywoN'
access_token = '333153736-lCFUKmq8XMnzDIdbWCJAj4lEt3baX18UUr1KsUym'
access_secret = 'qV94aPw0kABLXjQVFyLEaym5jdnM5RErBVgQV9N3Jsn3y'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

light_blue = '#%02x%02x%02x' % (41,152,238)

def getPublicTweets(GUI):
	global listbox

	public_tweets = api.home_timeline()

	scrollbar = Scrollbar(GUI)
	scrollbar.pack(side=RIGHT,fill=Y)

	listbox = Listbox(root, yscrollcommand=scrollbar.set)
	listbox.config(width=69, bg='light blue')
	listbox.pack(side=LEFT,fill=BOTH)

	scrollbar.config(command=listbox.yview)

	for tweet in public_tweets:
		phrase = ''
		"""
		tweet_json = public_tweets[0]
		json_str = json.dumps(tweet_json._json)
		json_str = json_str.json()
		print json_str["entities"]["user_mentions"][0]["screen_name"]
		print
		"""
		for x in tweet.text:
			try:
				phrase = phrase + str(x)
			except UnicodeEncodeError: 
				phrase = phrase + "*"
		listbox.insert(END, phrase[:70])
		listbox.insert(END, phrase[70:])
		listbox.insert(END,"_"*70)

def addNewTweets(GUI):
	listbox.delete(0,END)
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
		phrase = ''
		for x in tweet.text:
			try:
				phrase = phrase + str(x)
			except UnicodeEncodeError: 
				phrase = phrase + "*"
		listbox.insert(END, phrase[:70])
		listbox.insert(END, phrase[70:])
		listbox.insert(END,"_"*70)
	

def createTweetEntry(GUI):
	global textbox
	textbox = Text(GUI,height=2,width=70)
	textbox.pack(side=TOP,anchor=W)

	submit_button = Button(text='Tweet', fg='gray')#, command=api.update_status(status=str(textbox.get()) ))
	submit_button.pack(side=TOP,anchor=E)

def checkLength():
	tweet = ''
	if len(str(textbox.get('1.0',"end-1c"))) > 140:
		tweet = str(textbox.get('1.0',"end-1c"))[:140]
		textbox.delete('1.0','3.0')
		textbox.insert('1.0',tweet)
	root.after(1000,checkLength)


def title(GUI):
	Label(text='TWITTER @tirathp', font=('Pacifico','20'), bg=light_blue).pack(side=TOP)

def refresh(GUI):
	global refresh_button
	refresh_button = Button(GUI, text='Refresh', command= lambda:addNewTweets(GUI), bg='blue')
	refresh_button.pack(side=TOP,anchor=W)


root = Tk()
root.configure(background=light_blue)

title(root)
createTweetEntry(root)
root.after(1000,checkLength)
refresh(root)
getPublicTweets(root)




root.mainloop()






