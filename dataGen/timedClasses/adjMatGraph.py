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

import timeit

import atexit

class AdjMatGraph:

    """
    Represents an undirected graph. Please complete the implementations of each method. See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    function_times = {

        "__init__": [],
        "addVertex": [],
        "addVertices": [],
        "addEdge": [],
        "updateWall": [],
        "removeEdge": [],
        "hasVertex": [],
        "hasEdge": [],
        "getWallStatus": [],
        "neighbours": []

    }
    function_calls = {

        "__init__": 0,
        "addVertex": 0,
        "addVertices": 0,
        "addEdge": 0,
        "updateWall": 0,
        "removeEdge": 0,
        "hasVertex": 0,
        "hasEdge": 0,
        "getWallStatus": 0,
        "neighbours": 0

    }

    # Initialises an empty Graph

    def __init__(self):

        start_time = timeit.default_timer()
        
        ### Implement me! ###
        
        self.adjMatrix = [] # List to store Edges of the Adjacency Matrix
        self.vertices = [] # List to store Vertices of the Adjacency Matrix
        self.vertex_indices = {} # Dictionary to store Vertex-Index Mappings
        
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["__init__"].append(execution_time)
        AdjMatGraph.function_calls["__init__"] += 1

    # Adds a Vertex with the given label to the Graph

    def addVertex(self, label:Coordinates):

        start_time = timeit.default_timer()
        
        ### Implement me! ###

        if label not in self.vertices:
        
            self.vertices.append(label)
            self.vertex_indices[label] = len(self.vertices) - 1

            # Expand the Adjacency Matrix for the new Vertex
        
            for row in self.adjMatrix:
        
                row.append(0)
        
            self.adjMatrix.append([0] * len(self.vertices))
            
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["addVertex"].append(execution_time)
        AdjMatGraph.function_calls["addVertex"] += 1

    # Adds multiple Vertices with the given labels to the Graph

    def addVertices(self, vertLabels:List[Coordinates]):

        start_time = timeit.default_timer()

        ### Implement me! ###
        
        for label in vertLabels:
        
            self.addVertex(label)
            
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["addVertices"].append(execution_time)
        AdjMatGraph.function_calls["addVertices"] += 1

    # Adds an Edge between the Vertices 

    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool=False)->bool:

        start_time = timeit.default_timer()

        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            # 1 represents an Edge, 2 represents a Wall
        
            self.adjMatrix[index1][index2] = 2 if addWall else 1
            self.adjMatrix[index2][index1] = 2 if addWall else 1

            # remember to return booleans

            # True if Edge is added successfully e.g. addWall() is True
        
            result = True
        
        # Else False
        
        else:

            result = False
            
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["addEdge"].append(execution_time)
        AdjMatGraph.function_calls["addEdge"] += 1
        
        return result
    
    # Updates the Wall status of the Edge between two coordinates

    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:

        start_time = timeit.default_timer()
        
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
            
                result = True
            
            else:

                result = False
        
        else:

            result = False
            
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["updateWall"].append(execution_time)
        AdjMatGraph.function_calls["updateWall"] += 1
        
        return result
    
    # Removes the Edge between coordinates

    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:

        start_time = timeit.default_timer()
        
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
        
                result = True
            
            else:

                result = False
        
        # Else False
        
        else:

            result = False
            
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["removeEdge"].append(execution_time)
        AdjMatGraph.function_calls["removeEdge"] += 1
        
        return result
    
    # Checks if the Vertex label exists in the Graph

    def hasVertex(self, label:Coordinates)->bool:

        start_time = timeit.default_timer()
        
        ### Implement me! ###

        # Returns True if Vertex exists, else False

        result = label in self.vertex_indices
        
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["hasVertex"].append(execution_time)
        AdjMatGraph.function_calls["hasVertex"] += 1
        
        return result
    
    # Checks if an Edge exists between two Vertices

    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:

        start_time = timeit.default_timer()
        
        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            # remember to return booleans

            # Returns True if Edge exists
        
            result = self.adjMatrix[index1][index2] != 0
        
        # Else False
        
        else:

            result = False
            
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["hasEdge"].append(execution_time)
        AdjMatGraph.function_calls["hasEdge"] += 1
        
        return result
    
    # Checks if the Edge between coordinates is a Wall

    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:

        start_time = timeit.default_timer()
        
        ### Implement me! ###

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
        
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]

            # remember to return booleans

            # Returns True if the Edge is a Wall
        
            result = self.adjMatrix[index1][index2] == 2
        
        # Else False
        
        else:

            result = False
            
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["getWallStatus"].append(execution_time)
        AdjMatGraph.function_calls["getWallStatus"] += 1
        
        return result
    
    # Returns a List of coordinates representing the neighbouring Vertices of the label

    def neighbours(self, label:Coordinates)->List[Coordinates]:

        start_time = timeit.default_timer()
        
        ### Implement me! ###

        if label not in self.vertex_indices:
        
            result = []

        else:

            index = self.vertex_indices[label]

            # remember to return list of coordinates
        
            result = [self.vertices[i] for i, val in enumerate(self.adjMatrix[index]) if val != 0]
            
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["neighbours"].append(execution_time)
        AdjMatGraph.function_calls["neighbours"] += 1
        
        return result

def print_average_times():

    print("Average execution times:")

    for function_name, times in AdjMatGraph.function_times.items():

        if len(times) > 0:

            average_time = sum(times) / len(times)

            print(f"{function_name}: {average_time:.6f} seconds")

        else:

            print(f"{function_name}: Not called")

def print_function_calls():

    print("Function call counts:")

    for function_name, count in AdjMatGraph.function_calls.items():

        print(f"{function_name}: {count} calls")

atexit.register(print_average_times)
atexit.register(print_function_calls)