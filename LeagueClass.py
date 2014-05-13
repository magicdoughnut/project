#!/bin/python

class League:
	
	# A little documentation
	'A first attempt at a class for a football league'

	# Member objects of our class
	TeamName  = ''	# The name of the league we want to model
	TeamCount =  0  # The number of teams in our league
	TeamList  = []  # A list of the teams in the league

	# The number of teams to be promoted/relegated
	RelegCount = 3
	PromoCount = 3

	# The class' 'constructor' i.e. what happens when we create a 'League' object
	def __init__ (self, Name, Size):

		# Take the values given and save them in our object
		self.TeamName  = Name
		self.TeamCount = Size
		self.TeamList  = []

	# A method which returns the number of teams in the league
	def GetTeamCount (self):
		return len(self.TeamList)

	# A method which prints out the names of the teams in the league
	def PrintTeams (self):

		print '\n   -> League Name:', self.TeamName

		# If the league has no teams do this
		if len(self.TeamList) == 0:
			print '      League currently empty!'

		# Otherwise print out the names
		else:
			# For each entry in the list of teams
			for i in range(len(self.TeamList)):

				# Print the team name
				print '           ', self.TeamList[i]

			print '\n'

	# A method which adds a team to the 'TeamList' list
	def AddTeam (self, TeamName):

		# Add the name to the league
		self.TeamList.append(TeamName)

		# Sort the list of team names alphabetically
		self.TeamList = sorted(self.TeamList, key = str.lower)

	# A method which removes a team from the 'TeamList' list
	# Useful if, for instance, a team has been relegated
	def RemoveTeam (self, TeamName):

		# If the team is in 'TeamList' remove
		if TeamName in self.TeamList:
			self.TeamList.remove(TeamName)

# Class definition ends here