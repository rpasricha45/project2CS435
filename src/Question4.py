# Question 4
from Graph import Graph
from Graph import Node
import random

#B
class DirectedGraph(Graph):
    # other methods are implemented via Graph class
    def addDirectedEdge(self,nodeA , nodeB):
        # will not add if there is a cycle
        if nodeB not in nodeA.neigh and nodeA not in nodeB.neigh:
            nodeA.neigh.append(nodeB)
        self.addNode( nodeA)
        self.addNode(nodeB)
    def removeDirectedEdge(self,nodeA,nodeB):
        if nodeB in nodeA.neigh:
            nodeA.neigh.remove(nodeB)


#C
def createRandomDAGIter(n):
    graph = DirectedGraph(dict())
    myNodes = dict()
    for i in range(n+1):
        myNodes[i] = Node(i,[])
    #Random add the nodes
    nodesAdded = 0
    while nodesAdded <n:
        numb1 =  random.randint(0, n)
        numb2 = random.randint(0,n)
        graph.addDirectedEdge(myNodes[numb1],myNodes[numb2])
        nodesAdded = len(graph.adjancyList)
    return graph



class TopSort():
    #TODO please implement
    def inorder ( self , node,inorder,hasSeen):
        """
        :param node
        :return:
        """
        if node not in inorder:
            inorder[node] = 0
        for neigh in node.neigh:
            hasSeen.add(neigh)
            if neigh not in inorder:
                inorder[neigh] = 1
            elif neigh in inorder :
                inorder[neigh] +=1
            self.inorder(neigh,inorder,hasSeen)


    def Kahns (self,graph):
        nodeDependencies = dict()
        adList = graph.adjancyList

        # first find the then number of dependecies
        hasSeen = set()
        for node in adList:
            if node not in hasSeen:
                self.inorder(node,nodeDependencies,hasSeen)
                hasSeen.add(node)
        q = []
        rtVal = []
        for node in nodeDependencies:
            if nodeDependencies[node] == 0:
                q.append(node)
        while len(q) != 0:
            n = q.pop(0)
            rtVal.append(n)
            for neighbors in n.neigh:
                nodeDependencies[neighbors] -=1
                if nodeDependencies[neighbors] == 0:
                    q.append(neighbors)
            nodeDependencies[n] = -1
        return rtVal


    def helperMdfs(self, node , stack,hasSeen):
        #Todo please fix how the logic for visted
        if len(node.neigh) == 0:
            stack.append(node)
            return
        for neighbors in node.neigh:
            # if  neighbors in hasSeen:
            #     print("there is a cycle")
            #     return
            hasSeen.add(neighbors)
            self.helperMdfs(neighbors,stack,hasSeen)

        stack.append(node)


    def mDFS (self, graph):
        """
        :return: type list
        """
        adjancyList = graph.adjancyList
        hasSeen = set()
        stack = []
        for node in adjancyList:
            # call the helper method
            if node not in hasSeen:
                self.helperMdfs(node , stack,hasSeen)
        return stack






