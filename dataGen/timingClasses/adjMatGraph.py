# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', Oisin Aeonn s3952320
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------

from typing import List, Dict
from maze.util import Coordinates
from maze.graph import Graph
import timeit
import atexit

class AdjMatGraph:
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

        self.adjMatrix = []  # Adjacency matrix to store edges
        self.vertices = []  # List to store vertices
        self.vertex_indices = {}  # Dictionary to store vertex-index mappings

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["__init__"].append(execution_time)
        AdjMatGraph.function_calls["__init__"] += 1

    def addVertex(self, label):
        start_time = timeit.default_timer()

        if label not in self.vertices:
            self.vertices.append(label)
            self.vertex_indices[label] = len(self.vertices) - 1

            # Expand the adjacency matrix for the new vertex
            for row in self.adjMatrix:
                row.append(0)
            self.adjMatrix.append([0] * len(self.vertices))

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["addVertex"].append(execution_time)
        AdjMatGraph.function_calls["addVertex"] += 1

    def addVertices(self, vertLabels):
        start_time = timeit.default_timer()

        for label in vertLabels:
            self.addVertex(label)

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["addVertices"].append(execution_time)
        AdjMatGraph.function_calls["addVertices"] += 1

    def addEdge(self, vert1, vert2, addWall=False):
        start_time = timeit.default_timer()

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]
            # Use 1 for edge, 2 to represent wall
            self.adjMatrix[index1][index2] = 2 if addWall else 1
            self.adjMatrix[index2][index1] = 2 if addWall else 1
            result = True
        else:
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["addEdge"].append(execution_time)
        AdjMatGraph.function_calls["addEdge"] += 1
        return result

    def updateWall(self, vert1, vert2, wallStatus):
        start_time = timeit.default_timer()

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]
            if self.adjMatrix[index1][index2] != 0:  # Edge exists
                self.adjMatrix[index1][index2] = 2 if wallStatus else 1
                self.adjMatrix[index2][index1] = 2 if wallStatus else 1
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

    def removeEdge(self, vert1, vert2):
        start_time = timeit.default_timer()

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]
            if self.adjMatrix[index1][index2] != 0:  # Edge exists
                self.adjMatrix[index1][index2] = 0
                self.adjMatrix[index2][index1] = 0
                result = True
            else:
                result = False
        else:
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["removeEdge"].append(execution_time)
        AdjMatGraph.function_calls["removeEdge"] += 1
        return result

    def hasVertex(self, label):
        start_time = timeit.default_timer()

        result = label in self.vertex_indices

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["hasVertex"].append(execution_time)
        AdjMatGraph.function_calls["hasVertex"] += 1
        return result

    def hasEdge(self, vert1, vert2):
        start_time = timeit.default_timer()

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]
            result = self.adjMatrix[index1][index2] != 0
        else:
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["hasEdge"].append(execution_time)
        AdjMatGraph.function_calls["hasEdge"] += 1
        return result

    def getWallStatus(self, vert1, vert2):
        start_time = timeit.default_timer()

        if vert1 in self.vertex_indices and vert2 in self.vertex_indices:
            index1 = self.vertex_indices[vert1]
            index2 = self.vertex_indices[vert2]
            result = self.adjMatrix[index1][index2] == 2
        else:
            result = False

        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        AdjMatGraph.function_times["getWallStatus"].append(execution_time)
        AdjMatGraph.function_calls["getWallStatus"] += 1
        return result

    def neighbours(self, label):
        start_time = timeit.default_timer()

        if label not in self.vertex_indices:
            result = []
        else:
            index = self.vertex_indices[label]
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