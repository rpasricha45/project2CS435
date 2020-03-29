"""
Problem 3 A Graph implementation
"""

class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neigh = neighbors

class Graph:
    adjancyList = dict()
    # I am changing the definition of the method
    def addNode(self,node):
        #Todo please implement
        self.adjancyList[node] = node.neigh
    def addUndirectedEdge ( self,nodeA ,nodeB):
        if nodeA not in nodeB.neigh:
            nodeB.neigh.append(nodeA)
        if nodeB not in nodeA.neigh:
            nodeA.neigh.append(nodeB)
    def removeUndirectedEdge (self,nodeA, nodeB):
        if nodeA  in nodeB.neigh:
            nodeB.neigh.remove(nodeA)
        if nodeB in nodeA.neigh:
            nodeA.neigh.remove(nodeB)
    def getAllNodes(self):
        rtSet = set()
        for node in self.adjancyList:
            rtSet.add(node)
        return rtSet


