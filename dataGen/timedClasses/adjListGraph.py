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

import timeit
import atexit

class AdjListGraph:

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

        """
        Dictionary to store the Adjacency List where: 
        Key is the Vertex, 
                & 
        Value is the List of Neighbours
        """
        
        self.adjList = {}

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["__init__"].append(execution_time)
        AdjListGraph.function_calls["__init__"] += 1

    # Adds a Vertex to the Graph if it does not exist

    def addVertex(self, label:Coordinates):
    
        start_time = timeit.default_timer()
        
        ### Implement me! ###

        if label not in self.adjList:
            
            self.adjList[label] = []

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["addVertex"].append(execution_time)
        AdjListGraph.function_calls["addVertex"] += 1

    # Adds multiple Vertices with the given coordinates to the Graph

    def addVertices(self, vertLabels: List[Coordinates]):
    
        start_time = timeit.default_timer()
        
        ### Implement me! ###

        for label in vertLabels:
            
            self.addVertex(label)

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["addVertices"].append(execution_time)
        AdjListGraph.function_calls["addVertices"] += 1

    # Adds an undirected Edge between coordinates

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
    
        start_time = timeit.default_timer()
        
        ### Implement me! ###

        # Adds an undirected edge from coordinates

        if vert1 in self.adjList and vert2 in self.adjList: # if addWall() is True, the Edge is marked as a Wall
            
            self.adjList[vert1].append((vert2, addWall))
            self.adjList[vert2].append((vert1, addWall))
            
            # remember to return booleans

            # True if Edge is added successfully 
            
            result = True
                
        # Else False
        
        else:
    
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["addEdge"].append(execution_time)
        AdjListGraph.function_calls["addEdge"] += 1
    
        return result

    # Update the Wall status of the Edge between coordinates

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
    
        start_time = timeit.default_timer()
        
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

            result = True
        
        # Else False
        else:
    
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["updateWall"].append(execution_time)
        AdjListGraph.function_calls["updateWall"] += 1
    
        return result

    # Removes an undirected Edge between coordinates

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
    
        start_time = timeit.default_timer()
        
        ### Implement me! ###

        # Removes the undirected Edge from coordinates

        if vert1 in self.adjList and vert2 in self.adjList: 
        
            self.adjList[vert1] = [neighbour for neighbour in self.adjList[vert1] if neighbour[0] != vert2]
            self.adjList[vert2] = [neighbour for neighbour in self.adjList[vert2] if neighbour[0] != vert1]

            # remember to return booleans

            # True if Vertex exists
        
            result = True
        
        # Else False
    
        else: 
    
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["removeEdge"].append(execution_time)
        AdjListGraph.function_calls["removeEdge"] += 1
    
        return result

    # Checks if the Vertex of the coordinates exists in the Graph

    def hasVertex(self, label: Coordinates) -> bool:
    
        start_time = timeit.default_timer()
        
        ### Implement me! ###

        # Checks if a Vertex exists in the Graph

        # remember to return booleans

        # Returns True if the Vertex exists, else False

        result = label in self.adjList

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["hasVertex"].append(execution_time)
        AdjListGraph.function_calls["hasVertex"] += 1
    
        return result

    # Checks if an Edge exists between the coordinates

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
    
        start_time = timeit.default_timer()
        
        ### Implement me! ###

        if vert1 in self.adjList:

            # remember to return booleans

            # True if Edge exists
        
            result = any(neighbour[0] == vert2 for neighbour in self.adjList[vert1])
        
        # Else False
    
        else:
    
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["hasEdge"].append(execution_time)
        AdjListGraph.function_calls["hasEdge"] += 1
    
        return result

    # Check if the Edge between coordinates is marked as a Wall

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
    
        start_time = timeit.default_timer()
        
        ### Implement me! ###

        # Returns the Wall status between coordinates

        if vert1 in self.adjList:
        
            for neighbour, isWall in self.adjList[vert1]:
        
                if neighbour == vert2:

                    # remember to return booleans

                    # True if the Edge is a Wall
        
                    result = isWall
    
                    break
            else:
    
                result = False
    
        else:
    
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["getWallStatus"].append(execution_time)
        AdjListGraph.function_calls["getWallStatus"] += 1
    
        return result

    # Returns a List of coordinates of the neighbouring Vertices

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
    
        start_time = timeit.default_timer()
        
        ### Implement me! ###
        
        # Returns a List of Neighbours for the given Vertex

        if label in self.adjList:

            # remember to return list of coordinates

            # Returns List if there are neighbours
        
            result = [neighbour[0] for neighbour in self.adjList[label]]
        
        # Else empty List
    
        else:
    
            result = []

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["neighbours"].append(execution_time)
        AdjListGraph.function_calls["neighbours"] += 1
    
        return result

def print_average_times():
    
    print("Average execution times:")
    
    for function_name, times in AdjListGraph.function_times.items():
    
        if len(times) > 0:
    
            average_time = sum(times) / len(times)
    
            print(f"{function_name}: {average_time:.6f} seconds")
    
        else:
    
            print(f"{function_name}: Not called")

def print_function_calls():
    
    print("Function call counts:")
   
    for function_name, count in AdjListGraph.function_calls.items():
   
        print(f"{function_name}: {count} calls")

atexit.register(print_average_times)
atexit.register(print_function_calls)