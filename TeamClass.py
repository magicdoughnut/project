#!/bin/python

#class Team:

	# A little documentation
	'''A first attempt at a class for a team spec'''

	# Member objects of our class
	Points  = 0	# The name of the league we want to model
	GoalsScored =  0  # The number of teams in our league
	GoalsConceeded  = 0  # A list of the teams in the league

	# The class' 'constructor' i.e. what happens when we create a 'Team' object
	def __init__ (self, Name):

		# Take the values given and save them in our object
		self.Points  = 0
		self.GoalsScored = 0
		self.GoalsConceeded  = 0

	# A method which updates team stats
	def UpdateTeam (self):

		result = [3,2]
		print (result)
