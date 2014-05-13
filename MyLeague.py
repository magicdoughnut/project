#!/bin/python

# Import the class definition for a generic league and team
from LeagueClass import League
from TeamClass   import Team
#from Match import Score

# Let's set up a really simple league!
MyLeague = League('The Cornish First Division', 2)

# Add a couple of silly teams
MyLeague.AddTeam('Mark F.C.')
MyLeague.AddTeam('Jack Rovers')
MyLeague.AddTeam('Bastard United')

# Print out all the teams in our league
MyLeague.PrintTeams()

# Now lets say 'Bastard United' get relegated
MyLeague.RemoveTeam('Bastard United')

# Print out all the teams in our league again
MyLeague.PrintTeams()

