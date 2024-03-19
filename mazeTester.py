# -------------------------------------------------------------------
# DON'T CHANGE THIS FILE.
# This is the entry point to run the program.
# Refer to usage() for exact format of input expected to the program.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------


import sys
import time
import json
from typing import List

from maze.util import Coordinates
from maze.maze import Maze
from maze.arrayMaze import ArrayMaze
from maze.graphMaze import GraphMaze

from generation.mazeGenerator import MazeGenerator
from generation.recurBackGenerator import RecurBackMazeGenerator


# this checks if Visualizer has been imported properly.
# if not, likely missing some packages, e.g., matplotlib.
# in that case, regardless of visualisation flag, we should set the canVisualise flag to False which will not call the visuslisation part.
canVisualise = True
try:
	from maze.maze_viz import Visualizer
except:
	Visualizer = None
	canVisualise = False



def usage():
	"""
	Print help/usage message.
	"""

	# On Teaching servers, use 'python3'
	# On Windows, you may need to use 'python' instead of 'python3' to get this to work
	print('python3 mazeTester.py', '<configuration file>')
	sys.exit(1)


#
# Main.
#
if __name__ == '__main__':
	# Fetch the command line arguments
	args = sys.argv

	if len(args) != 2:
		print('Incorrect number of arguments.')
		usage()


	# open configuration file		
	fileName: str = args[1]
	with open(fileName,"r") as configFile:
		# use json parser
		configDict = json.load(configFile)

		# assign to variables storing various parameters
		dsApproach: str = configDict['dataStructure']
		rowNum: int = configDict['rowNum']
		colNum: int = configDict['colNum']
		entrances: List[List[int]] = configDict['entrances']
		exits: List[List[int]] = configDict['exits']
		genApproach: str = configDict['generator']
		bVisualise: bool = configDict['visualise']

		#
		# Initialise maze object (which also selects which data structure implementation is used).
		#
		maze: Maze = None
		if dsApproach == 'array':
			maze = ArrayMaze(rowNum, colNum)
		elif dsApproach == 'adjlist':
			maze = GraphMaze(rowNum, colNum, dsApproach)
		elif dsApproach == 'adjmat':
			maze = GraphMaze(rowNum, colNum, dsApproach)
		else:
			print('Unknown data structure approach specified.')
			usage()

		# add the entraces and exits
		for [r,c] in entrances:
			maze.addEntrance(Coordinates(r, c))
		for [r,c] in exits:
			maze.addExit(Coordinates(r, c))

		
		#
		# Generate maze
		#
		generator: MazeGenerator = None
		if genApproach == 'recur':
			generator = RecurBackMazeGenerator()
		else:
			print('Unknown generator approach specified.')
			usage()


		# timer for generation
		startGenTime : float = time.perf_counter()

		generator.generateMaze(maze)

		# stop timer
		endGenTime: float = time.perf_counter()

		print(f'Generation took {endGenTime - startGenTime:0.4f} seconds')

		# add/generate the entrances and exits
		generator.addEntrances(maze)
		generator.addExits(maze)

		#
		# Display maze.
		#
		if bVisualise and canVisualise:
			cellSize = 1
			visualiser = Visualizer(maze, cellSize) 
			visualiser.show_maze()
			
