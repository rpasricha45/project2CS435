from Question4 import DirectedGraph
import random
class Node(object):
    """
    :param int val , dict() neighbors , int weight
    """
    def __init__(self, val, neighbors,):
        self.val = val
        self.neigh = neighbors
class WeightedGraph (DirectedGraph):
    def addNode(self,value):
        self.adjancyList[Node(value , dict())]
    def add(self,node):
        self.adjancyList[node] = node.neigh
    def addWeightedEdge (self, nodeA , nodeB , edgeWeight):
        # check if it is a directed graph
        if nodeA in nodeB.neigh:
            nodeA.neigh[nodeB] = nodeB.neigh[nodeA]
            return
        nodeA.neigh[nodeB] = edgeWeight
        self.add(nodeA)
    #Override
    def removeDirectedEdge(self,nodeA,nodeB):
        if nodeB in nodeA.neigh:
            del nodeA.neigh[nodeB]


# 5c
def createRandomCompleteWeightedGraph(n):
    myList = []
    g = WeightedGraph(dict())

    for i in range (n):
        myList.append(Node(i,dict()))
    for i in range (len(myList)):
        for k in range(0,len(myList)):
            if k!= i:
                rand = random.randint(0,10)
                g.addWeightedEdge(myList[i],myList[k],rand)

    return g

# 5 d
#TODO please implement
def createLinkedList(n):
    graph = WeightedGraph(dict())
    myNodes = []
    for i in range ( n):
        myNodes.append(Node(i,[]))
    for i in range(1,len(myNodes)):
        graph.addWeightedEdge(myNodes[i],myNodes[i-1],i)

    return graph

#5c

def dikstras ( startNode , endNode):
    myMap  = dict()
    myMap[startNode] = 0
    myMap[endNode] = 9999999
    hasSeen = set()
    distance = 0
    current = startNode
    while current != endNode:
        #relax it's neighbors
        for  node in current.neigh:
            distance = myMap[current] + current.neigh[node]
            if node not in myMap:
                myMap[node] = distance
            elif distance < myMap[node]:
                myMap[node] = distance

        # choose the minimum path
        hasSeen.add(current)
        minVal = 99999
        minNode = None
        for node in myMap:
            if node not in hasSeen:
                if myMap[node] <  minVal:
                    minVal = myMap[node]
                    minNode = node
        distance += myMap[current]
        current = minNode
    return distance

def dijkstrasDriver(start,endNode,hasSeen,rtVal):
    rtVal[endNode] = dikstras(start ,endNode)
    hasSeen.add(endNode)
    for neigh in endNode.neigh:

        if neigh not in hasSeen:
            dijkstrasDriver(start,neigh,hasSeen,rtVal)
def dijkstrasMain(start):
    rtVal = dict()
    hasSeen = set()
    dijkstrasDriver(start ,start,hasSeen,rtVal)
    return rtVal

