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

	# A method which updates Goals and Points
	def UpdateGandP (self):

		# Make up a result and home/away status
		HA = 1 # 1 = home 0 = away?
		result = [3,2]

		if HA == 1:
			self.GoalsScored = GoalsScored + result[1]
			self.GoalsConceeded = GoalsConceeded + result[2]

			# Calculate if team has won drawn or lost and add points
			if result[1]>result[2]:
				self.Point = self.Point + 3
			elif result[1]==result[2]:
				self.Point = self.Point + 1
			elif result[1]<result[2]:
				self.Point = self.Point + 0

		else:
			self.GoalsScored = self.GoalsScored + result[2]
			self.GoalsConceeded = self.GoalsConceeded + result[1]

			# Calculate if team has won drawn or lost (WDL) 
			if result[1]<result[2]:
				self.Point = self.Point + 3
			elif result[1]==result[2]:
				self.Point = self.Point + 1
			elif result[1]>result[2]:
				self.Point = self.Point + 0
				

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

	
