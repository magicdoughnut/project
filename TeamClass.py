#!/bin/python

class Team:

	# A little documentation
	'''A first attempt at a class for a team spec'''

	# Member objects of our class
	TeamName        = ''	# The name of the team
	Points          = 0	# The number of points the team has got

	# Goals stats
	GoalsScored     = 0	# The number of goals scored
	GoalsConceeded  = 0	# The number of goals conceeded

	# Games stats
	GamesPlayed = 0		# The number of games played
	GamesWon    = 0		# The number of games won
	GamesLost   = 0		# The number of games lost
	GamesDrawn  = 0		# The number of games drawn

	# Player stats
	PlayerList  = ['']	# A list of the players names

	# The class' 'constructor' i.e. what happens when we create a 'Team' object
	def __init__ (self, Name):

		# Take the values given and save them in our object
		self.TeamName = Name

	# A method which updates the goals and points stats
	def SubmitResult (self, GoalsScored, GoalsConceeded):

		# Update games played stat
		GamesPlayed += 1

		# Update Goal stats
		self.GoalsScored    += GoalsScored
		self.GoalsConceeded += GoalsConceeded

		# If we won
		if GoalsScored > GoalsConceeded:
			Points   += 3
			GamesWon += 1
		# If we Drew
		else if GoalsConceeded == GoalsConceeded:
			Points     += 1
			GamesDrawn += 1
		# If we Lost
		else:
			GamesLost += 1

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

	# Calculate the teams goal difference
	def GetGoalDifference (self): return self.GoalsScored - self.GoalsConceeded
