# -------------------------------------------------
# DON'T CHANGE THIS FILE.
# Base class for maze implementations. 
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------

from typing import List

from maze.util import Coordinates


class Maze:
    """
    Base (abstract) class for mazes.
    """


    def __init__(self, rowNum:int, colNum:int):
        """
        Constructor.

        @param rowNum: number of rows in the maze.
        @param colNum: number of columns in the maze
        """
        self.m_rowNum = rowNum
        self.m_colNum = colNum

        # entrances and exits
        self.m_entrance = list()
        self.m_exit = list()



    def initCells(self, addWallFlag:bool = False):
        """
        Initialises the cells in the maze. 
        Override to customise behaviour.

        @param addWallFlag: Whether we should also add the walls between cells.  Default is False.
        """
        pass



    def addWall(self, cell1:Coordinates, cell2:Coordinates)->bool:
        """
        Adds a wall between cells cell1 and cell2.
        cell1 and cell2 should be adjacent.
        Override to customise behaviour.

        @param cell1: Coordinates of cell1.
        @param cell2: Coordinates of cell2.

        @return True if successfully added a wall, otherwise False in all other cases.
        """
        pass



    def removeWall(self, cell1:Coordinates, cell2:Coordinates)->bool:
        """
        Removes a wall between cells cell1 and cell2.
        cell1 and cell2 should be adjacent.
        Override to customise behaviour.

        @param cell1: Coordinates of cell1.
        @param cell2: Coordinates of cell2.

        @return True if successfully removed a wall, otherwise False in all other cases.
        """
        pass



    def allWalls(self):
        """
        Add walls between all cells in the maze.
        """

        # add walls to the left and bottom of a 2d traversal of cells
        for r in range(-1,self.m_rowNum):
            for c in range(-1,self.m_colNum):
                self.addWall(Coordinates(r,c), Coordinates(r+1,c))
                self.addWall(Coordinates(r,c), Coordinates(r,c+1))
                
        # add the wall along the right maze boundary, and top maze boundary
        for r in range(0,self.m_rowNum):
            self.addWall(Coordinates(r,self.m_colNum-1), Coordinates(r,self.m_colNum))

        for c in range(0,self.m_colNum):
            self.addWall(Coordinates(self.m_rowNum-1, c), Coordinates(self.m_rowNum, c))



    def addEntrance(self, cell: Coordinates)->bool:
        """
        Adds an entrance to the maze.  A maze can have more than one entrance, so this method can be called more than once.

        @return True if successfully added an entrance, otherwise False.
        """

        # check if cell of entrance is valid
        assert(self.checkCoordinates(cell))

        # check if cell of the entrance is on the boundary of the maze, as an entrance should only be added along the boundary
        if (cell.getRow() == -1 and cell.getCol() >= 0 and cell.getCol() < self.m_colNum) \
            or (cell.getRow() == self.m_rowNum and cell.getCol() >= 0 and cell.getCol() < self.m_colNum) \
            or (cell.getCol() == -1 and cell.getRow() >= 0 and cell.getRow() < self.m_rowNum) \
            or (cell.getCol() == self.m_colNum and cell.getRow() >= 0 and cell.getRow() < self.m_rowNum):
            
            self.m_entrance.append(cell)

            return True
        else:
            # not on the boundary
            return False



    def addExit(self, cell: Coordinates)->bool:
        """
        Adds an exit to the maze.  A maze can have more than one exit, so this method can be called more than once.

        @return True if successfully added an exit, otherwise False.
        """

        # check if cell of exit is valid
        assert(self.checkCoordinates(cell))

        # check if cel of exitl is on the boundary of the maze, as an exit should only be added along the boundary
        if (cell.getRow() == -1 and cell.getCol() >= 0 and cell.getCol() < self.m_colNum) \
            or (cell.getRow() == self.m_rowNum and cell.getCol() >= 0 and cell.getCol() < self.m_colNum) \
            or (cell.getCol() == -1 and cell.getRow() >= 0 and cell.getRow() < self.m_rowNum) \
            or (cell.getCol() == self.m_colNum and cell.getRow() >= 0 and cell.getRow() < self.m_rowNum):
            
            self.m_exit.append(cell)

            return True
        else:
            # not on boundary
            return False
        


    def getEntrances(self)->List[Coordinates]:
        """
        @returns list of entrances that the maze has.
        """
        return self.m_entrance
    


    def getExits(self)->List[Coordinates]:
        """
        @returns list of exits that the maze has.
        """
        return self.m_exit



    def hasWall(self, cell1:Coordinates, cell2:Coordinates)->bool:
        """
        Checks if there is a wall between cell1 and cell2.
        Override if need to customise behaviour

        @returns True, if there is a wall.

        """
        pass



    def rowNum(self)->int:
        """
        @returns The number of rows the maze has.
        """

        return self.m_rowNum



    def colNum(self)->int:
        """
        @return The number of columns the maze has.
        """

        return self.m_colNum



    def checkCoordinates(self, coord:Coordinates)->bool:
        """
        Checks if the coordinates is a valid one.
        
        @param coord: Cell/coordinate to check if it is a valid one.
        
        @returns True if coord/cell is valid, otherwise False.
        """

        return coord.getRow() >= -1 and coord.getRow() <= self.m_rowNum and coord.getCol() >= -1 and coord.getCol() <= self.m_colNum

    

    def isPerfect(self)->bool:
        """
        Checks if the maze is perfect.
        Please feel free to make your own implementation to evaluate if your generated mazes are perfect.  You will
        not be assessed for this by for your own checking.  Please do not submit your implementation when submitting in Canvas.
        If you do accidentally, we will replace this file with the existing one when testing, but ideally better if you didn't.

        @returns True if the generated maze is perfect, or False if not.
        """
        pass