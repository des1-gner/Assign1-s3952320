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
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """
    
    def __init__(self):
        
        ### Implement me! ###
        
        self.adjMatrix = [] # List to store Edges of the Adjacency Matrix
        self.vertices = [] # List to store Vertices of the Adjacency Matrix
        self.vertex_indices = {} # Dictionary to store Vertex-Index Mappings

    def addVertex(self, label:Coordinates):
        
        ### Implement me! ###

        if label not in self.vertices:
        
            self.vertices.append(label)
            self.vertex_indices[label] = len(self.vertices) - 1

            # Expand the adjacency matrix for the new vertex
        
            for row in self.adjMatrix:
        
                row.append(0)
        
            self.adjMatrix.append([0] * len(self.vertices))

    def addVertices(self, vertLabels:List[Coordinates]):

        ### Implement me! ###
        
        for label in vertLabels:
        
            self.addVertex(label)

    def addEdge(self, vert1, vert2, addWall=False):

        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            # Use 1 for edge, 2 to represent wall
        
            self.adjMatrix[index1][index2] = 2 if addWall else 1
            self.adjMatrix[index2][index1] = 2 if addWall else 1

            # remember to return booleans
        
            return True
        
        return False

    def updateWall(self, vert1, vert2, wallStatus):
        
        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            if self.adjMatrix[index1][index2] != 0:  # Edge exists
            
                self.adjMatrix[index1][index2] = 2 if wallStatus else 1
                self.adjMatrix[index2][index1] = 2 if wallStatus else 1

                # remember to return booleans
            
                return True
        
        return False

    def removeEdge(self, vert1, vert2):
        
        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            if self.adjMatrix[index1][index2] != 0:  # Edge exists
        
                self.adjMatrix[index1][index2] = 0
                self.adjMatrix[index2][index1] = 0

                # remember to return booleans
        
                return True
        
        return False

    def hasVertex(self, label):
        
        ### Implement me! ###

        return label in self.vertex_indices

    def hasEdge(self, vert1, vert2):
        
        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            # remember to return booleans
        
            return self.adjMatrix[index1][index2] != 0
        
        return False

    def getWallStatus(self, vert1, vert2):
        
        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            # remember to return booleans
        
            return self.adjMatrix[index1][index2] == 2
        
        return False

    def neighbours(self, label):
        
        ### Implement me! ###

        if label not in self.vertex_indices:
        
            return []

        index = self.vertex_indices[label]

        # remember to return list of coordinates
        
        return [self.vertices[i] for i, val in enumerate(self.adjMatrix[index]) if val != 0]