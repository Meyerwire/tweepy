from tkinter import *
from tkinter import tkk
import tweepyMain

master_window = tkk.Tk()
master_window.title = ("Tweepy")
master_window.geometry("300x150")
master_window.resizable(False,False)

tweetText = tkk.Entry(master_window).pack()
TweetButton = tkk.Button(master_window,width=10,text="Tweet",command =lambda: print(tweetText)).pack()