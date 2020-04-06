from Graph import Graph
import math
import random

class Node (object):
    def __init__(self, val, neighbors,x ,y):
        self.val = val
        self.neigh = neighbors
        self.x = x
        self.y = y

# extends the Graph class
class GridGraph:

    def __init__(self, dict):
        self.adjancyList = dict

    def isNeighbor(self,gridNodeA,gridNodeB):
        # assuming no duplicate values
        if gridNodeB.x <0 or gridNodeB.y <0:
            return False
        xMoves = [0,1,-1]
        yMoves = [0,1,-1]
        for combo in xMoves:
            if gridNodeA.x + combo == gridNodeB.x and gridNodeA.y == gridNodeB.y:
                return True
        for yCombo in yMoves:
            if gridNodeA.x == gridNodeB.x and gridNodeA.y+ yCombo ==gridNodeB.y:
                return True

        return False

        pass
    def addNode (self , gridNode):
        self.adjancyList[gridNode] = gridNode.neigh

    def addGridNode(self, x ,y , nodeVal):
        # TODO please implement
        nodeTemp = Node(nodeVal,[],x,y)
        self.addNode(nodeTemp)

    def addUndirectedEdge(self,gridNodeA,gridNodeB):
        if self.isNeighbor(gridNodeB,gridNodeA):
            if gridNodeB not in gridNodeA.neigh:
                gridNodeA.neigh.append(gridNodeB)
            if gridNodeA not in gridNodeB.neigh:
                gridNodeB.neigh.append(gridNodeA)
        self.addNode(gridNodeB)
        self.addNode(gridNodeA)
    def removeUndirectedEdge (self, gridNodeA, gridNodeB):
        if gridNodeA in gridNodeB.neigh:
            gridNodeB.remove(gridNodeA)
        if gridNodeB in gridNodeA.neigh:
            gridNodeA.remove(gridNodeB)
    def getAllNodes (self):
        rtSet = set()
        for node in self.adjancyList:
            rtSet.add(node)
        return rtSet



def getDistance ( gridNodeA,gridNodeB):
    return math.sqrt(pow((gridNodeB.x-gridNodeA.x),2)+pow((gridNodeB.y-gridNodeA.y),2))

# driver methods

def randomPoint(startPair,max):

    tempX = startPair[0]
    tempY = startPair[-1]
    if  tempX == max and tempY< max:
        return ((tempX,tempY+1))
    elif tempY == max and tempX< max:
        return ((tempX+1,tempY))


    probality = random.randint(0, 2)
   # todo make this a helper method
    if probality == 0:
        tempX =1
        tempX += startPair[0]
    else:
        tempY = 1
        tempY += startPair[-1]
    return ((tempX,tempY))

def valid (pair , myDict):
    if pair[0]  <0 or pair[-1]< 0:
        return False
    if pair not in myDict:
        return  False
    return True

def createRandomGridGraph(n):
    """
    :param n: int
    :return: GridGraph
    """
    graph = GridGraph(dict())
    myDict = dict()
    for x in range(n):
        for y in range(n):
            myDict[(x,y)]=Node(x,[],x,y)
    # randomise the graph
    for key  in myDict:
        # get the random
        if key == (n-1,n-1):
            graph.addNode(myDict[key])
            break
        myNeigh = randomPoint(key,n-1)
        while not valid(myNeigh,myDict):
            myNeigh = randomPoint(key)
        graph.addUndirectedEdge(myDict[key],myDict[myNeigh])
    return graph


def hurstic (gridNodeA , gridNodeB):
    # TODO calcualte the manhatten distance bettween the two
    return abs(gridNodeA.x-gridNodeB.x) + abs(gridNodeA.y-gridNodeB.y)

def astar (sourceNode , destNode):
    """
    :param sourceNode: GridNode
    :param destNode: GridNode
    :return: list()
    """
    if sourceNode == None or destNode == None:
        print("input is not correct")
        return None
    rtVal = []
    map = dict()
    visted = set()
    curent = sourceNode
    map[curent] = [0,hurstic(curent,destNode)]
    while curent != destNode:
        if curent == None:
            print("there is an error")
            break
        for neighbors in curent.neigh:
            if neighbors not in visted:
                gVal =getDistance(neighbors,curent) + map[curent][0]
                hVal = hurstic(neighbors,destNode)
                if neighbors not in map:
                    map[neighbors] = [gVal,hVal]
                elif gVal< map[neighbors][0]:
                    # update the mapping
                    map[neighbors] = [gVal,hVal]
        visted.add(curent)
        rtVal.append(curent)
        # find the next min path ( gval + hval)
        # this is probly the error
        minVal = 99999
        newNode = None
        for node in map:
            if node not in visted:
                if sum(map[node]) <minVal:
                    minVal = sum(map[node])
                    newNode = node
        curent = newNode
        if curent == destNode:
            rtVal.append(curent)

    return rtVal
