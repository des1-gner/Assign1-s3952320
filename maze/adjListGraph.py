# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', 'Oisin Aeonn s3952320'
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------

from typing import List

from maze.util import Coordinates

from maze.graph import Graph

class AdjListGraph:

    """
    Represents an undirected graph. Please complete the implementations of each method. See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    # Initialises an empty Graph

    def __init__(self):

        ### Implement me! ###

        """
        Dictionary to store the Adjacency List where: 
        Key is the Vertex, 
                & 
        Value is the List of Neighbours
        """
        
        self.adjList = {}

    # Adds a Vertex to the Graph if it does not exist

    def addVertex(self, label:Coordinates):
        
        ### Implement me! ###

        if label not in self.adjList:
            
            self.adjList[label] = []

    # Adds multiple Vertices with the given coordinates to the Graph

    def addVertices(self, vertLabels: List[Coordinates]):
        
        ### Implement me! ###

        for label in vertLabels:
            
            self.addVertex(label)

    # Adds an undirected Edge between coordinates

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        
        ### Implement me! ###

        # Adds an undirected edge from coordinates

        if vert1 in self.adjList and vert2 in self.adjList: # if addWall() is True, the Edge is marked as a Wall
            
            self.adjList[vert1].append((vert2, addWall))
            self.adjList[vert2].append((vert1, addWall))
            
            # remember to return booleans

            # True if Edge is added successfully 
            
            return True
                
        # Else False
        
        return False

    # Update the Wall status of the Edge between coordinates

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        
        ### Implement me! ###

        # Updates the Wall status of an Edge
        
        if vert1 in self.adjList and vert2 in self.adjList: # if addWall() is True, the Edge is a Wall
        
            for i, (vertex, isWall) in enumerate(self.adjList[vert1]):
        
                if vertex == vert2:
        
                    self.adjList[vert1][i] = (vertex, wallStatus)
        
            for i, (vertex, isWall) in enumerate(self.adjList[vert2]):
        
                if vertex == vert1:
        
                    self.adjList[vert2][i] = (vertex, wallStatus)

            # remember to return booleans

            # True if Edge is added

            return True
        
        # Else False
        
        return False

    # Removes an undirected Edge between coordinates

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        
        ### Implement me! ###

        # Removes the undirected Edge from coordinates

        if vert1 in self.adjList and vert2 in self.adjList: 
        
            self.adjList[vert1] = [neighbour for neighbour in self.adjList[vert1] if neighbour[0] != vert2]
            self.adjList[vert2] = [neighbour for neighbour in self.adjList[vert2] if neighbour[0] != vert1]

            # remember to return booleans

            # True if Vertex exists
        
            return True
        
        # Else False
        
        return False

    # Checks if the Vertex of the coordinates exists in the Graph

    def hasVertex(self, label: Coordinates) -> bool:
        
        ### Implement me! ###

        # Checks if a Vertex exists in the Graph

        # remember to return booleans

        # Returns True if the Vertex exists, else False

        return label in self.adjList

    # Checks if an Edge exists between the coordinates

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        
        ### Implement me! ###

        if vert1 in self.adjList:

            # remember to return booleans

            # True if Edge exists
        
            return any(neighbour[0] == vert2 for neighbour in self.adjList[vert1])
        
        # Else False
        
        return False

    # Check if the Edge between coordinates is marked as a Wall

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        
        ### Implement me! ###

        # Returns the Wall status between coordinates

        if vert1 in self.adjList:
        
            for neighbour, isWall in self.adjList[vert1]:
        
                if neighbour == vert2:

                    # remember to return booleans

                    # True if the Edge is a Wall
        
                    return isWall
                
        # Else False
        
        return False

    # Returns a List of coordinates of the neighbouring Vertices

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        
        ### Implement me! ###
        
        # Returns a List of Neighbours for the given Vertex

        if label in self.adjList:

            # remember to return list of coordinates

            # Returns List if there are neighbours
        
            return [neighbour[0] for neighbour in self.adjList[label]]
        
        # Else empty List
        
        return []