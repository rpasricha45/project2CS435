from Graph import Graph
from Graph import Node
import random
# question 3

# b
def createRandomUnweightedGraphIter(n):
    graph = Graph()
    for i in range(n):
        temp = Node(n,[])
        graph.addNode(temp)
    myAdjacnyList = graph.adjancyList
    nodes = []
    random.shuffle(nodes)
    for node in myAdjacnyList:
        nodes.append(node)
    for i in range(1, len(nodes)):
        graph.addUndirectedEdge(nodes[i],nodes[i-1])
    return graph

# c
def createLinkedList (n):
    graph = Graph()
    nodeList = []
    for i in range (n):
        tempNode =  Node(n,[])
        nodeList.append(tempNode)
    for i in range ( 1, len(nodeList)):
        nodeList[i-1].neigh.append(nodeList[i])
    for node in nodeList:
        graph.addNode(node)
    return  graph


# d
def dfsHelper (curNode, targetNode , mySet , rtList ):
    if curNode == targetNode:
        rtList.append(curNode)
        return
    if curNode == None:
        return
    rtList.append(curNode)
    neighbors = curNode.neigh
    for neighbor in neighbors:
        if neighbor not in mySet:
            dfsHelper(neighbor,targetNode,mySet,rtList)
def DFSRec ( start , end):
    """
        :param start: Node
        :param end: Node
        :return: List[Node]
        """
    rtList = []
    hasSeen = set()
    dfsHelper(start,end ,hasSeen,rtList )
    if end not in rtList:
        return None
    else:
        return rtList
# e
def DFSIter ( start , end):
    """
        :param start: Node
        :param end: Node
        :return: List[Node]
        """
    rtList = []
    hasSeen = set()
    stack = [start]
    while len( stack) >0:
        currNode = stack.pop(-1)
        rtList.append(currNode)
        hasSeen.add(currNode)
        for node in currNode.neigh:
            if node not in hasSeen:
                stack.append(node)
    if end not in rtList:
        return None
    return rtList

# f
def BSTHelper ( q,rtList,hasSeen):
    if len(q) <1:
        return
    myNode = q.pop(-1)
    rtList.append(myNode)
    hasSeen.add(myNode)
    myList = myNode.neigh

    for node in myList:
        if node not in hasSeen:
            q.append(node)
    BSTHelper(q,rtList,hasSeen)

#todo check the names
def BSTRec ( graph):
    """

    :return: List[Node]
    """
    rtList = []
    hasSeen = set()
    for node in graph.adjancyList:
        # Recursive helper function
        BSTHelper([node],rtList,hasSeen)

    return rtList
#G
def BSTIterHelper ( node,rtList ,hasSeen):
    if node == None:
        return
    q = [node]
    while len(q) > 0:
        myNode = q.pop(0)
        rtList.append(myNode)
        hasSeen.add(myNode)
        for nodes in myNode.neigh:
            if nodes not in hasSeen:
                q.append(nodes)


def BSTIter( graph):
    """
    :param graph: Graph
    :return: List []
    """
    rtList = []
    hasSeen = set ()
    for nodes in graph.adjancyList:
        BSTIterHelper(nodes, rtList , hasSeen)
    return rtList

# h
