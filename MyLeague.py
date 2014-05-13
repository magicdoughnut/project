#!/bin/python

# Import the class definition for a generic league and team
from LeagueClass import League
from TeamClass   import Team
#from Match import Score

# Let's set up a really simple league!
MyLeague = League('The World Cup Group Stages', 2)

# Add a couple of silly teams
MyLeague.AddTeam('Uruguay')
MyLeague.AddTeam('England')
MyLeague.AddTeam('Italy')

# Print out all the teams in our league
MyLeague.PrintTeams()

# Now lets say 'Bastard United' get relegated
MyLeague.RemoveTeam('England')

# Print out all the teams in our league again
MyLeague.PrintTeams()

