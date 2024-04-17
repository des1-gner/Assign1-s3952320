# ------------------------------------------------------------------------
# MODIFY IF NEED TO.
# Graph implementation of a maze.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.maze import Maze
from maze.util import Coordinates
from maze.graph import Graph
from maze.adjListGraph import AdjListGraph
from maze.adjMatGraph import AdjMatGraph



class GraphMaze(Maze):
    """
    Graph implementation of a 2D, square cell maze.
    """

    def __init__(self, rowNum:int, colNum:int, graphType:str):
        """
        Constructor.
        Has extra argument of the type of graph we will use as the underlying graph implementation.

        @param graphType: Name of underlying graph implementation.  [adjlist, adjmat].
        """

        super().__init__(rowNum, colNum)
        self.m_graph : Graph = None
        if graphType == 'adjlist':
            self.m_graph = AdjListGraph()
        elif graphType == 'adjmat':
            self.m_graph = AdjMatGraph()



    def initCells(self, addWallFlag:bool = False):

        super().initCells()

        # add the vertices and edges to the graph
        self.m_graph.addVertices([Coordinates(r,c) for r in range(self.m_rowNum) for c in range(self.m_colNum)])
        # add boundary vertices
        self.m_graph.addVertices([Coordinates(-1,c) for c in range(self.m_colNum)])
        self.m_graph.addVertices([Coordinates(r,-1) for r in range(self.m_rowNum)])
        self.m_graph.addVertices([Coordinates(self.m_rowNum,c) for c in range(self.m_colNum)])
        self.m_graph.addVertices([Coordinates(r,self.m_colNum) for r in range(self.m_rowNum)])

        # add adjacenies/edges to the graph
        # Scan across rows first
        for row in range(0, self.m_rowNum):
            for col in range(-1, self.m_colNum):
                self.m_graph.addEdge(Coordinates(row,col), Coordinates(row,col+1), addWallFlag)

        # scan columns now
        for col in range(0, self.m_colNum):
            for row in range(-1, self.m_rowNum):
                self.m_graph.addEdge(Coordinates(row,col), Coordinates(row+1,col), addWallFlag)



    def addWall(self, cell1:Coordinates, cell2:Coordinates)->bool:

        # checks if coordinates are valid
        assert(self.checkCoordinates(cell1) and self.checkCoordinates(cell2))

        # only can add wall if adjacent
        if self.m_graph.hasEdge(cell1, cell2):
            self.m_graph.updateWall(cell1, cell2, True)
            return True
        
        # in all other cases, we return False
        return False




    def removeWall(self, cell1:Coordinates, cell2:Coordinates)->bool:

        # checks if coordinates are valid
        assert(self.checkCoordinates(cell1) and self.checkCoordinates(cell2))

        # only can remove wall if adjacent
        if self.m_graph.hasEdge(cell1, cell2):
            self.m_graph.updateWall(cell1, cell2, False)
            return True
        
        # in all other cases, we return False
        return False



    def hasWall(self, cell1:Coordinates, cell2:Coordinates)->bool:
        return self.m_graph.getWallStatus(cell1, cell2)



    def neighbours(self, cell:Coordinates)->List[Coordinates]:
        return self.m_graph.neighbours(cell)


    