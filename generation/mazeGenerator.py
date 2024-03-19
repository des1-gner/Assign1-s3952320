# -------------------------------------------------------------------
# DON'T CHANGE THIS FILE.
# Base class for maze generator.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------


from maze.maze import Maze
from maze.util import Coordinates

class MazeGenerator:
	"""
	Base class for a maze generator.
	"""

	def generateMaze(self, maze:Maze):
		"""
	    Generates a maze.  Will update the passed maze.

		@param maze Maze which we update on to generate a maze. 
		"""
		pass



	def addEntrances(self, maze:Maze):
		"""
		Add entrance(s) to the maze.

		@param maze Maze which we update on to generate a maze. 
		"""
		
		# when adding the entrances, we need to remove the relevant boundary wall
		for ent in maze.getEntrances():
			# need to figure out which direction to remove wall
			# entrance is at bottom, need to remove wall in "up" direction
			if ent.getRow() == -1:
				maze.removeWall(ent, Coordinates(0, ent.getCol()))
			# entrance is at top, need to remove wall in "down" direction
			elif ent.getRow() == maze.rowNum():
				maze.removeWall(ent, Coordinates(maze.rowNum()-1, ent.getCol()))
			# entrace is to the left, need to remove wall in "right" direction
			elif ent.getCol() == -1:
				maze.removeWall(ent, Coordinates(ent.getRow(), 0))
			# entrance is to the right, need to remove wall in "left" direction
			elif ent.getCol() == maze.colNum():
				maze.removeWall(ent, Coordinates(ent.getRow(), maze.colNum()-1))




	def addExits(self, maze:Maze):
		"""
		Add exit(s) to the maze.

		@param maze Maze which we update on to generate a maze. 
		"""
		
		# when adding the exits, we need to remove the relevant boundary wall
		for ext in maze.getExits():
			# need to figure out which direction to remove wall
			# exit is at bottom, need to remove wall in "up" direction
			if ext.getRow() == -1:
				maze.removeWall(ext, Coordinates(0, ext.getCol()))
			# exit is at top, need to remove wall in "down" direction
			elif ext.getRow() == maze.rowNum():
				maze.removeWall(ext, Coordinates(maze.rowNum()-1, ext.getCol()))
			# exit is to the left, need to remove wall in "right" direction
			elif ext.getCol() == -1:
				maze.removeWall(ext, Coordinates(ext.getRow(), 0))
			# exit is to the right, need to remove wall in "left" direction
			elif ext.getCol() == maze.colNum():
				maze.removeWall(ext, Coordinates(ext.getRow(), maze.colNum()-1))

		