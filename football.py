import urllib2
import numpy as np

def get_info(club):
	url = "http://www.bbc.co.uk/sport/football/premier-league/results"
	request = urllib2.Request(url)
	handle = urllib2.urlopen(request)
	content = handle.read()

	# Cut down data
	splitpage = content.split("fixtures-table full-table-medium",1);
	content = splitpage[1]
	splitpage = content.split("Please note: All times",1);
	content = splitpage[0]

	# Cut down data - into matchdays
	splitpage = content.split('<h2 class="table-header">')
	matchdays = splitpage[1:len(splitpage)]

	GD_log = []
	for i in matchdays:
		# Cut dpwn data - into games each day
		splitpage = i.split("<tr class='report'")
		for m in splitpage:
			if club in m:
				# Get Score
				splitpage = m.split("<abbr title='Score'>")
				score = splitpage[1]
				score = score[1:4]
				# Work out if win or lose
				splitpage = m.split("<span class='team-away teams'>")
				if club in splitpage[1]:
					HA = 'A'
					GD = int(score[2])-int(score[0])
				else:
					HA = 'H'
					GD = int(score[0])-int(score[2])
				GD_log.append(GD)

	# Calculate points
	P_log = []
	for k in GD_log:
		if k >0:
			P_log.append(3)
		elif k<0:
			P_log.append(0)
		elif k == 0:
			P_log.append(1)


	# Calculate Cumulative points
	P_log.reverse()
	cum_P_log = np.cumsum(P_log)
	cum_P_log = cum_P_log.tolist()

	GD_log.reverse()
	for m in range(0,len(GD_log)):
		if m<0:
			GD_log[m] = 0 
	return(cum_P_log,GD_log)





#Plot
import matplotlib.pyplot as plt

City_P,City_GD = get_info('Man City')
City_x = range(1,len(City_P)+1)
plt.plot(City_x,City_P,color = '#4682b4')
for j in range(1,len(City_P)+1):
	plt.plot(j,City_P[j-1],'o',markersize = City_GD[j-1]*5,markeredgecolor =  '#4682b4',markerfacecolor = 'none')

United_P,United_GD = get_info('Man Utd')
United_x = range(1,len(United_P)+1)
plt.plot(United_x,United_P,'r')
for j in range(1,len(United_P)+1):
	plt.plot(j,United_P[j-1],'o',markersize = United_GD[j-1]*5,markeredgecolor = 'r',markerfacecolor = 'none')

Chelsea_P,Chelsea_GD = get_info('Chelsea')
Chelsea_x = range(1,len(Chelsea_P)+1)
plt.plot(Chelsea_x,Chelsea_P,'b')
for j in range(1,len(Chelsea_P)+1):
	plt.plot(j,Chelsea_P[j-1],'o',markersize = Chelsea_GD[j-1]*5,markeredgecolor = 'b',markerfacecolor = 'none')

Arsenal_P,Arsenal_GD = get_info('Arsenal')
Arsenal_x = range(1,len(Arsenal_P)+1)
plt.plot(Arsenal_x,Arsenal_P,color = '#b22222')
for j in range(1,len(Arsenal_P)+1):
	plt.plot(j,Arsenal_P[j-1],'ok',markersize = Arsenal_GD[j-1]*5, markeredgecolor = '#b22222',markerfacecolor = 'none')


teams = ['Everton','Liverpool','Tottenham','Crystal Palace','Watford','West Brom','Leicester','Hull','Middlesbrough','Southampton','Swansea','Burnley','Bournemouth','West Ham','Sunderland','Stoke']

for n in teams:
	P,GD = get_info(n)
	x = range(1,len(P)+1)
	plt.plot(x,P,'k')
	for j in range(1,len(P)+1):
		plt.plot(j,P[j-1],'o',markersize = GD[j-1]*5,markeredgecolor = 'k' ,markerfacecolor = 'none')



plt.ylabel('Points')
plt.xlabel('Match Day')
plt.show()






