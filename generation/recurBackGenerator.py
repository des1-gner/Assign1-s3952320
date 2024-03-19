# -------------------------------------------------------------------
# DON'T CHANGE THIS FILE.
# Recursive backtracking maze generator.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------

from random import randint, choice
from collections import deque

from maze.maze import Maze
from maze.util import Coordinates
from generation.mazeGenerator import MazeGenerator




class RecurBackMazeGenerator(MazeGenerator):
	"""
	Recursive backtracking maze generator.
	Overrides genrateMaze of parent class.
	"""

	def generateMaze(self,maze: Maze):

		# make sure we start the maze with all walls there
		maze.initCells(True)

		# select starting cell 
		startCoord : Coordinates = Coordinates(randint(0, maze.rowNum()-1), randint(0, maze.colNum()-1))

		# run recursive backtracking/DFS from starting cell
		stack : deque = deque()
		stack.append(startCoord)
		currCell : Coordinates = startCoord 
		visited : set[Coordinates] = set([startCoord])

		totalCells = maze.rowNum() * maze.colNum()

		while len(visited) < totalCells:
			# find all neighbours of current cell
			neighbours : list[Coordinates] = maze.neighbours(currCell)

			# filter to ones that haven't been visited and within boundary
			nonVisitedNeighs : list[Coordinates] = [neigh for neigh in neighbours if neigh not in visited and neigh.getRow() >= 0 and neigh.getRow() < maze.rowNum() and neigh.getCol() >= 0 and neigh.getCol() < maze.colNum()]
			
			# see if any unvisited neighbours
			if len(nonVisitedNeighs) > 0:
				# randomly select one of them
				neigh = choice(nonVisitedNeighs)

				# we move there and knock down wall
				maze.removeWall(currCell, neigh)

				# add to stack
				stack.append(neigh)

				# updated visited
				visited.add(neigh)

				# update currCell
				currCell = neigh
			else:
				# backtrack
				currCell = stack.pop()

		
