from tkinter import *
#import tkinter as tk
import tweepyMain

    



master_window = Tk()
master_window.title = ("Tweepy")
master_window.geometry("300x150")
master_window.resizable(False,False)

tweetText = Entry(master_window)
tweetText.pack()
TweetButton = Button(master_window,width=10,text="Tweet",command= lambda:tweepyMain.tweetText(tweetText.get())).pack()

tweetID1 = Entry(master_window)
tweetID1.pack()
TweetButton = Button(master_window,width=10,text="Like",command= lambda:tweepyMain.likeTweet(int(tweetID1.get()))).pack()

tweetID2 = Entry(master_window)
tweetID2.pack()
TweetButton = Button(master_window,width=10,text="Unlike",command= lambda:tweepyMain.unlikeTweet(int(tweetID2.get()))).pack()

master_window.mainloop()