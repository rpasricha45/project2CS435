from Graph import Graph
from Graph import Node
from PartB import createLinkedList
from PartB import BSTRec
from PartB import createRandomUnweightedGraphIter

graph = createLinkedList(10000)

# driver code

graphX = createRandomUnweightedGraphIter(100)

def BFTRecLinkedList (graph):
    return BSTRec(graph)

BFTRecLinkedList(graphX)