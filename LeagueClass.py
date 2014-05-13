#!/bin/python

class League:
	
	# A little documentation
	'A first attempt at a class for a football league'

	# Member objects of our class
	TeamName  = ''	# The name of the league we want to model
	TeamCount = -1  # The number of teams in our league
	TeamList  = []  # A list of the teams in the league

	# The class' 'constructor' i.e. what happens when we create a 'League' object
	def __init__ (self, Name = 'Premier League', Size = 20):

		# Take the values given and save them in our object
		self.TeamName  = Name
		self.TeamCount = Size
		self.TeamList  = []

	# A method which returns the number of teams in the league
	def GetTeamCount (self):
		return len(self.TeamList)

	# A 'method' which prints out the names of the teams in the league
	def PrintTeams (self):

		print '\n   -> Team Name:', self.TeamName

		# If the league has no teams do this
		if len(self.TeamList) == 0:
			print '      League currently empty!'
			return 0

		# Otherwise print out the names
		else:
			# For each entry in the list of teams
			for i in range(len(self.TeamList)):

				# Print the team name
				print '           ', self.TeamList[i]

			print '\n'

	# A 'method' which adds a team to the 'TeamList' list
	def AddTeam (self, TeamName):

		# Add the name to the league
		self.TeamList.append(TeamName)

		# Sort the list of team names alphabetically
		self.TeamList = sorted(self.TeamList, key = str.lower)

# Class definition ends here


