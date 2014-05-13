import urllib2
import string
import numpy as np

# get user to pick a team
songname = raw_input('Enter a Team Name: ')
songname = songname.replace(" ","")
url = "http://www1.skysports.com/football/teams/"+songname
request = urllib2.Request(url)
handle = urllib2.urlopen(request)
content = handle.read()

# get goalkeepers
splitpage = content.split("Goalkeepers",1);
splitpage = splitpage[1].split("Defenders",1);
splitpage = splitpage[0].split("title=" )

for i in range(1,len(splitpage)):
	val = splitpage[i].split(">")
	if i == 1:
		Goalkeepers = val[0]
	else :
		Goalkeepers = Goalkeepers +val[0]

print '\n   Goalkeepers:   \n' + Goalkeepers

# get defenders
splitpage = content.split("Defenders",1);
splitpage = splitpage[1].split("Midfielders",1);
splitpage = splitpage[0].split("title=" )

for i in range(1,len(splitpage)):
	val = splitpage[i].split(">")
	if i == 1:
		Defenders = val[0]
	else :
		Defenders = Defenders +val[0]

print '\n   Defenders:   \n' + Defenders

# get midfielders
splitpage = content.split("Midfielders",1);
splitpage = splitpage[1].split("Attacking Midfielders",1);
splitpage = splitpage[0].split("title=" )

for i in range(1,len(splitpage)):
	val = splitpage[i].split(">")
	if i == 1:
		Midfielders = val[0]
	else :
		Midfielders = Midfielders +val[0]

print '\n   Midfielders:   \n' + Midfielders


# get attacking midfielders
splitpage = content.split("Attacking Midfielders",1);
splitpage = splitpage[1].split("Strikers",1);
splitpage = splitpage[0].split("title=" )

for i in range(1,len(splitpage)):
	val = splitpage[i].split(">")
	if i == 1:
		AMidfielders = val[0]
	else :
		AMidfielders = AMidfielders +val[0]

print '\n   Attacking Midfielders:   \n' + AMidfielders


# get strikers
splitpage = content.split("Strikers",1);
splitpage = splitpage[1].split("</ul>",1);
splitpage = splitpage[0].split("title=" )

for i in range(1,len(splitpage)):
	val = splitpage[i].split(">")
	if i == 1:
		Strikers = val[0]
	else :
		Strikers = Strikers +val[0]

print '\n   Strikers:   \n' + Strikers


