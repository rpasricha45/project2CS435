from Question4 import DirectedGraph
from Question4 import TopSort
from Question4 import  Node
from Question4 import createRandomDAGIter
from question5 import dijkstrasMain
from question5 import WeightedGraph
from question5 import createRandomCompleteWeightedGraph
from Question6 import astar
from Question6 import GridGraph
from Question6 import   createRandomGridGraph

#problem 4
def topolgicalSortTest (g):
    print("running test for question 4 ")

    topS = TopSort()
    list = topS.Kahns(g)
    print("khans algo ")
    for node in list:
        print( node.val)
    print("mdfs")
    list2 = topS.mDFS(g)
    for n in list2:
        print(n.val)

# problem 5
def dijkstrastest(g):
    print("starting test for problem 5 ")
    nodeStart = None
    for key in g.adjancyList:
        nodeStart =key
        break;
    rtval = dijkstrasMain(nodeStart)
    print(rtval)
# problem 6

def isPath(sourceNode, destNode, hasSeen):
    if sourceNode == destNode:
        return True
    hasSeen.add(sourceNode)
    for nodes in sourceNode.neigh:
        if nodes not in hasSeen:
            if isPath(nodes, destNode, hasSeen):
                return True
    return False

def printPair(gridNode):
    print(str(gridNode.x) + " ," + " " + str(gridNode.y))

def astartest(graph):
    print('starting test for problem 6 ')
    startNode = None
    for key in graph.adjancyList:
        if key.x == 0 and key.y == 0:
            startNode = key
            break

    endNode = None
    for key in graph.adjancyList:
        if key.x == 99 and key.y == 99:
            endNode = key

    printPair(startNode)
    printPair(endNode)
    myList = (astar(startNode, endNode))

    # # there is a mistake
    # print(startNode in myList )
    #
    print("   priting path ")
    for node in myList:
        printPair(node)
def main():
    #4
    g = createRandomDAGIter(1000)
    topolgicalSortTest(g)
    #5
    weighted  = createRandomCompleteWeightedGraph(10)
    dijkstrastest(weighted)
    #6
    grid =  createRandomGridGraph(100)

    astartest(grid)

if __name__=="__main__":
    main()