# ------------------------------------------------------------------------
# DON'T CHANGE THIS FILE.
# Array-based maze implementation.
# Provided as an example, please use this also as an example of what you
# need to do for the graph implementations.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List
from maze.maze import Maze
from maze.util import Coordinates


class ArrayMaze(Maze):
    """
    Array implementation of a 2D, square cell maze.
    Provided as example of an implementation.
    """

    def __init__(self, rowNum:int, colNum:int):
        
        super().__init__(rowNum, colNum)
        # this grid storages both the cells, the walls and all the cells strounding the outer boundary of the maze
        # Hence we need 2*rowNum/colNum + 2
        self.m_grid = [[True for c in range(2*colNum+2)] for r in range(2*rowNum+2)]



    def initCells(self, addWallFlag:bool = False):

        super().initCells(addWallFlag)
        if addWallFlag:
            super().allWalls()
        # otherwise we don't need to do anything, as the cells are initiated already.



    def addWall(self, cell1:Coordinates, cell2:Coordinates)->bool:

        # checks if coordinates are valid
        assert(self.checkCoordinates(cell1) and self.checkCoordinates(cell2))

        # check if cells are adjacent
        if cell1.isAdjacent(cell2):
            # difference between the rows and columns for the two cells we adding a wall between
            diff:tuple[int,int] = (cell2.getRow() - cell1.getRow(), cell2.getCol() - cell1.getCol())
            # check if wall exist
            if self.m_grid[cell1.getRow()*2 + diff[0] + 2][cell1.getCol()*2 + diff[1] + 2]:
                return False
            else:
                # wall doesn't exist, hence we can add a wall there
                self.m_grid[cell1.getRow()*2 + diff[0] + 2][cell1.getCol()*2 + diff[1] + 2] = True
   
        return True



    def removeWall(self, cell1:Coordinates, cell2:Coordinates)->bool:

        # checks if coordinates are valid
        assert(self.checkCoordinates(cell1) and self.checkCoordinates(cell2))

        # check if cells are adjacent
        if cell1.isAdjacent(cell2):
            # difference between the rows and columns for the two cells we are moving a wall between
            diff:tuple[int,int] = (cell2.getRow() - cell1.getRow(), cell2.getCol() - cell1.getCol())
            if not self.m_grid[cell1.getRow()*2 + diff[0] + 2][cell1.getCol()*2 + diff[1] + 2]:
                return False
            else:
                # wall does exist, hence we can remove a wall there
                self.m_grid[cell1.getRow()*2 + diff[0] + 2][cell1.getCol()*2 + diff[1] + 2] = False
   
        return True
    


    def hasWall(self, cell1:Coordinates, cell2:Coordinates)->bool:

        # checks if coordinates are valid
        assert(self.checkCoordinates(cell1) and self.checkCoordinates(cell2))

        # check if cells are adjacent
        if cell1.isAdjacent(cell2):
            # difference between the rows and columns for the two cells we are checking if a wall exists between them
            diff:tuple[int,int] = (cell2.getRow() - cell1.getRow(), cell2.getCol() - cell1.getCol())
            return self.m_grid[cell1.getRow()*2 + diff[0] + 2][cell1.getCol()*2 + diff[1] + 2]
        else:
            # if not adjacent, then return False.
            return False
                
        

    def neighbours(self, cell:Coordinates)->List[Coordinates]:

        # checks if coordinates are valid
        assert(self.checkCoordinates(cell))

        # neighbour one cell below
        neighbours : List[Coordinates] = []
        if cell.getRow()-1 >= -1:
            neighbours.append(Coordinates(cell.getRow()-1, cell.getCol()))
        # neighbour one cell above
        if cell.getRow()+1 <= self.rowNum():
            neighbours.append(Coordinates(cell.getRow()+1, cell.getCol()))
        # neighbour one cell to the left
        if cell.getCol()-1 >= -1:
            neighbours.append(Coordinates(cell.getRow(), cell.getCol()-1))
        # neighbour one cell to the right
        if cell.getCol()+1 <= self.colNum():
            neighbours.append(Coordinates(cell.getRow(), cell.getCol()+1))            

        return neighbours


