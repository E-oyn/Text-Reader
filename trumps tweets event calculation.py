#Lab Seasons
from datetime import datetime

#1.Directory and Import Relative Modules

import os 
input_directory = "C:/Users/Ege/Dropbox/QMEF/Lab/Python/tt2017"
output_file = "C:/Users/Ege/Dropbox/QMEF/Lab/Python/output1/Tweets.txt"

#2. Listing All Files

def list_files(directory):
	allfiles = [] 
	for dirname, dirnames, filenames in os.walk(directory):
		for filename in filenames: 
	 		allfiles.append(os.path.join(dirname,filename)) 
	return allfiles

allfiles = list_files(input_directory)
allfiles.sort()

print(list_files("C:/Users/Ege/Dropbox/QMEF/Lab/Python/tt2017"))



#3.Checking for desired words/outputs

def multiple_string_check(text):
    count = 0
    string1 = "china"
    string2 = "trade"
    word_count1 = text.count(string1)
    word_count2 = text.count(string2)
    if word_count1 >= 1 and word_count2 >= 1:
    	count = 1
    return count

def get_tweet_id(filename):
	id = filename.split("/")
	id = id[-1]
	id = id.split("\\")
	id = id[-1]
	id = id.split(".")
	return id[0]

def get_tweet_date(text):
	date = text.split("\n")
	return date[0]

def get_tweet_text(text):
	tweet = text.split("\n")
	return tweet[1]

outfile = open("C:/Users/Ege/Dropbox/QMEF/Assigments/2/Stata/New Stock Data/nnn/Python Folders/outfile14.txt", mode = 'w') 

origin_date = datetime(2016,11,21)
flag = -1 
for filename in allfiles:	
	with open(filename) as file:
		text = file.read()
		text = text.lower()
		tweet_id = get_tweet_id(filename)
		date = get_tweet_date(text)
		tweet_text = get_tweet_text(text)
		china_trade = multiple_string_check(tweet_text)
		counter = "-" 
		if flag == 1:
			counter = datetime(int(date[-4:]),int(date[3:5]),int(date[:2])).date() - origin_date.date()
			efe = str(counter.days).split("day")[0]
		else: 
			efe = "-"
		if china_trade == 1: 
			flag = 1
			origin_date = datetime(int(date[-4:]),int(date[3:5]),int(date[:2]))
	


		outfile.write(str(tweet_id)+ "," + str(date) + "," + str(china_trade)+","+efe+ "\n")
		
		print(efe)
		


outfile.close()
