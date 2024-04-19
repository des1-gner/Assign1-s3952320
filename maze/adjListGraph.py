# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', Oisin Aeonn s3952320
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------

from typing import List

from maze.util import Coordinates

from maze.graph import Graph

class AdjListGraph:



    def __init__(self):

        ### Implement me! ###

        # Dictionary to store adjacency list, key is a vertex and value is the list of neighbours.
        self.adjList = {}

    def addVertex(self, label: Coordinates):
        
        ### Implement me! ###

        # Add a vertex to the graph if it does not exist
        if label not in self.adjList:
            
            self.adjList[label] = []

    def addVertices(self, vertLabels: List[Coordinates]):
        
        ### Implement me! ###

        # Add multiple vertices to the graph
        for label in vertLabels:
            
            self.addVertex(label)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        
        ### Implement me! ###

        # Adds an undirected edge from vert1 to vert2 (and vice versa)
        if vert1 in self.adjList and vert2 in self.adjList:
            
            self.adjList[vert1].append((vert2, addWall))
            self.adjList[vert2].append((vert1, addWall))
            
            return True
        
        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        
        ### Implement me! ###

        # Updates the wall status of an edge
        
        if vert1 in self.adjList and vert2 in self.adjList:
        
            for i, (vertex, isWall) in enumerate(self.adjList[vert1]):
        
                if vertex == vert2:
        
                    self.adjList[vert1][i] = (vertex, wallStatus)
        
            for i, (vertex, isWall) in enumerate(self.adjList[vert2]):
        
                if vertex == vert1:
        
                    self.adjList[vert2][i] = (vertex, wallStatus)
        
            return True
        
        return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        
        ### Implement me! ###

        # Removes the undirected edge from vert1 to vert2 (and vice versa)
        if vert1 in self.adjList and vert2 in self.adjList:
        
            self.adjList[vert1] = [neighbour for neighbour in self.adjList[vert1] if neighbour[0] != vert2]
            self.adjList[vert2] = [neighbour for neighbour in self.adjList[vert2] if neighbour[0] != vert1]
        
            return True
        
        return False

    def hasVertex(self, label: Coordinates) -> bool:
        
        ### Implement me! ###

        # Checks if a vertex exists in the graph
        return label in self.adjList

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        
        ### Implement me! ###

        # Checks if an edge exists between vert1 and vert2
        if vert1 in self.adjList:
        
            return any(neighbour[0] == vert2 for neighbour in self.adjList[vert1])
        
        return False

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        
        ### Implement me! ###

        # Returns the wall status between vert1 and vert2
        if vert1 in self.adjList:
        
            for neighbour, isWall in self.adjList[vert1]:
        
                if neighbour == vert2:
        
                    return isWall
        
        return False

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        
        ### Implement me! ###
        
        # Returns a list of neighbours for the given vertex
        if label in self.adjList:
        
            return [neighbour[0] for neighbour in self.adjList[label]]
        
        return []