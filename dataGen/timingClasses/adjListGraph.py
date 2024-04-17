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
import timeit
import atexit

class AdjListGraph:
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

    def __init__(self):
        start_time = timeit.default_timer()

        # Dictionary to store adjacency list, key is a vertex and value is the list of neighbours.
        self.adjList = {}

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["__init__"].append(execution_time)
        AdjListGraph.function_calls["__init__"] += 1

    def addVertex(self, label: Coordinates):
        start_time = timeit.default_timer()

        # Add a vertex to the graph if it does not exist
        if label not in self.adjList:
            self.adjList[label] = []

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["addVertex"].append(execution_time)
        AdjListGraph.function_calls["addVertex"] += 1

    def addVertices(self, vertLabels: List[Coordinates]):
        start_time = timeit.default_timer()

        # Add multiple vertices to the graph
        for label in vertLabels:
            self.addVertex(label)

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["addVertices"].append(execution_time)
        AdjListGraph.function_calls["addVertices"] += 1

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        start_time = timeit.default_timer()

        # Adds an undirected edge from vert1 to vert2 (and vice versa)
        if vert1 in self.adjList and vert2 in self.adjList:
            self.adjList[vert1].append((vert2, addWall))
            self.adjList[vert2].append((vert1, addWall))
            result = True
        else:
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["addEdge"].append(execution_time)
        AdjListGraph.function_calls["addEdge"] += 1
        return result

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        start_time = timeit.default_timer()

        # Updates the wall status of an edge
        if vert1 in self.adjList and vert2 in self.adjList:
            for i, (vertex, isWall) in enumerate(self.adjList[vert1]):
                if vertex == vert2:
                    self.adjList[vert1][i] = (vertex, wallStatus)
            for i, (vertex, isWall) in enumerate(self.adjList[vert2]):
                if vertex == vert1:
                    self.adjList[vert2][i] = (vertex, wallStatus)
            result = True
        else:
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["updateWall"].append(execution_time)
        AdjListGraph.function_calls["updateWall"] += 1
        return result

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        start_time = timeit.default_timer()

        # Removes the undirected edge from vert1 to vert2 (and vice versa)
        if vert1 in self.adjList and vert2 in self.adjList:
            self.adjList[vert1] = [neighbour for neighbour in self.adjList[vert1] if neighbour[0] != vert2]
            self.adjList[vert2] = [neighbour for neighbour in self.adjList[vert2] if neighbour[0] != vert1]
            result = True
        else:
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["removeEdge"].append(execution_time)
        AdjListGraph.function_calls["removeEdge"] += 1
        return result

    def hasVertex(self, label: Coordinates) -> bool:
        start_time = timeit.default_timer()

        # Checks if a vertex exists in the graph
        result = label in self.adjList

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["hasVertex"].append(execution_time)
        AdjListGraph.function_calls["hasVertex"] += 1
        return result

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        start_time = timeit.default_timer()

        # Checks if an edge exists between vert1 and vert2
        if vert1 in self.adjList:
            result = any(neighbour[0] == vert2 for neighbour in self.adjList[vert1])
        else:
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjListGraph.function_times["hasEdge"].append(execution_time)
        AdjListGraph.function_calls["hasEdge"] += 1
        return result

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        start_time = timeit.default_timer()

        # Returns the wall status between vert1 and vert2
        if vert1 in self.adjList:
            for neighbour, isWall in self.adjList[vert1]:
                if neighbour == vert2:
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

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        start_time = timeit.default_timer()

        # Returns a list of neighbours for the given vertex
        if label in self.adjList:
            result = [neighbour[0] for neighbour in self.adjList[label]]
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