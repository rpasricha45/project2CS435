from Graph import Graph
from Graph import Node
from PartB import createLinkedList
from PartB import BSTRec
from PartB import BSTIter
from PartB import createRandomUnweightedGraphIter

graph = Graph()

# driver code

graphX = createLinkedList(10000)


def BFTRecLinkedList (graph):
    if graph == None:
        print("null value")
        return None
    return BSTRec(graph)

def BFTItter ( graph):
    return BSTIter(graph)
# BFTRecLinkedList(graphX)
BFTItter(graphX)