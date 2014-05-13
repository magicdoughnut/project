import numpy as np
from random import randint

def Match(HomeTeam, AwayTeam):
	Score = np.ones((1,2))
	Score[0,0] = randint(0, 5)
	Score[0,1] = randint(0, 5)
	#return Score
