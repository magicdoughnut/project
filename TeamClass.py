#!/bin/python

class Team:

	# A little documentation
	'''A first attempt at a class for a team spec'''

	# Member objects of our class
	TeamName        = ''	# The name of the team
	Points          = 0	# The number of points the team has got
	GoalsScored     = 0	# The number of goals scored
	GoalsConceeded  = 0	# The number of goals conceeded
	PlayerList      = ['']	# A list of the players names

	# The class' 'constructor' i.e. what happens when we create a 'Team' object
	def __init__ (self, Name):

		# Take the values given and save them in our object
		self.TeamName = Name

	# A method which updates team stats
	def UpdateTeam (self):

		result = [3,2]
		print (result)

	# A method for adding a player
	def AddPlayer (self, PlayerName):

		# Add the name to the league
		self.PlayerList.append(TeamName)

		# Sort the list of players names alphabetically
		self.PlayerList = sorted(self.PlayerList, key = str.lower)
	
	# A method which removes a player from 'PlayerList'
	def RemoveTeam (self, PlayerName):

		# If the team is in 'TeamList' remove
		if PlayerName in self.PlayerList:
			self.TeamList.remove(PlayerName)

	# A method which prints out the names of the teams in the league
	def PrintTeams (self):

		print '\n   -> Team Name:', self.TeamName

		# If the team has no players...
		if len(self.PlayerList) == 0:
			print '      League currently empty!'

		# Otherwise print out the names
		else:
			# For each entry in the list of teams
			for i in range(len(self.PlayerList)):

				# Print the team name
				print '           ', self.PlayerList[i]

			print '\n'