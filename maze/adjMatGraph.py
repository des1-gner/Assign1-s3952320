# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', 'Oisin Aeonn s3952320'
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------

from typing import List, Dict

from maze.util import Coordinates

from maze.graph import Graph

class AdjMatGraph:
    
    """
    Represents an undirected graph. Please complete the implementations of each method. See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    # Initialises an empty Graph

    def __init__(self):
        
        ### Implement me! ###
        
        self.adjMatrix = [] # List to store Edges of the Adjacency Matrix
        self.vertices = [] # List to store Vertices of the Adjacency Matrix
        self.vertex_indices = {} # Dictionary to store Vertex-Index Mappings

    # Adds a Vertex with the given label to the Graph

    def addVertex(self, label:Coordinates):
        
        ### Implement me! ###

        if label not in self.vertices:
        
            self.vertices.append(label)
            self.vertex_indices[label] = len(self.vertices) - 1

            # Expand the Adjacency Matrix for the new Vertex
        
            for row in self.adjMatrix:
        
                row.append(0)
        
            self.adjMatrix.append([0] * len(self.vertices))

    # Adds multiple Vertices with the given labels to the Graph

    def addVertices(self, vertLabels:List[Coordinates]):

        ### Implement me! ###
        
        for label in vertLabels:
        
            self.addVertex(label)

    # Adds an Edge between the Vertices 

    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool=False)->bool:

        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            # 1 represents an Edge, 2 represents a Wall
        
            self.adjMatrix[index1][index2] = 2 if addWall else 1
            self.adjMatrix[index2][index1] = 2 if addWall else 1

            # remember to return booleans

            # True if Edge is added successfully e.g. addWall() is True
        
            return True
        
        # Else False
        
        return False
    
    # Updates the Wall status of the Edge between two coordinates

    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        
        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            # Edge exists

            if self.adjMatrix[index1][index2] != 0: 

                # 1 represents an Edge, 2 represents a Wall
            
                self.adjMatrix[index1][index2] = 2 if wallStatus else 1
                self.adjMatrix[index2][index1] = 2 if wallStatus else 1

                # remember to return booleans
            
                return True
        
        return False
    
    # Removes the Edge between coordinates

    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        
        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            # Edge exists

            if self.adjMatrix[index1][index2] != 0:  
        
                self.adjMatrix[index1][index2] = 0
                self.adjMatrix[index2][index1] = 0

                # remember to return booleans

                # True if Edge is removed
        
                return True
            
        # Else False
        
        return False
    
    # Checks if the Vertex label exists in the Graph

    def hasVertex(self, label:Coordinates)->bool:
        
        ### Implement me! ###

        # Returns True if Vertex exists, else False

        return label in self.vertex_indices
    
    # Checks if an Edge exists between two Vertices

    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        
        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            # remember to return booleans

            # Returns True if Edge exists
        
            return self.adjMatrix[index1][index2] != 0
        
        # Else False
        
        return False
    
    # Checks if the Edge between coordinates is a Wall

    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        
        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            # remember to return booleans

            # Returns True if the Edge is a Wall
        
            return self.adjMatrix[index1][index2] == 2
        
        # Else False
        
        return False
    
    # Returns a List of coordinates representing the neighbouring Vertices of the label

    def neighbours(self, label:Coordinates)->List[Coordinates]:
        
        ### Implement me! ###

        if label not in self.vertex_indices:
        
            return []

        index = self.vertex_indices[label]

        # remember to return list of coordinates
        
        return [self.vertices[i] for i, val in enumerate(self.adjMatrix[index]) if val != 0]