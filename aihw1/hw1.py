from Queue import PriorityQueue, Queue
import pprint


# Set up a graph of connections and weights
class WeightedGraph:
    def __init__(self):
        self.edges = {}
        self.weights = {}
        self.closedList = set() # check this to see if node is in closed list
        self.closedList2 = Queue() # keep track of closed list/order removed from open
        self.openList = PriorityQueue()
        self.totalAddedToOpenListCounter = 1
        self.nodeCountOpen = {}  # for 1d
        self.nodeCountClosed = {}  # for 1e
        self.startNode = ''
        self.goalNode = ''
        self.totalCost = 0

    def showFinalResults(self):
        print("From Node " + self.startNode + " to Node " + self.goalNode)
        print("Total Cost: " + str(self.totalCost))
        print("A: Order Removed From Open List: " + str(self.closedList2.queue))
        print("B: Open List when Goal Found: "),
        # have to use a while loop to get the heap to print in order.
        while self.openList.qsize() != 0:
            cost, node, parent = self.openList.get()
            self.nodeCountOpen[node] += 1
            print("[" + str(node) + ', ' + str(cost) + ', ' + parent + "]"),
        print("\nB: Closed List when Goal Found: " + str(self.closedList2.queue))
        print("C: Total Nodes Added to Open List: " + str(self.totalAddedToOpenListCounter))
        print("D: Total time each node appears as the current node in the final open list: " + str(self.nodeCountOpen))
        print(
        "E: Total time each node appears as the current node in the final closed list: " + str(self.nodeCountClosed))
        print("\n#########################")

    '''
    TODO
    THis is waht we worked on at teh coffee shop. Copy and paste to a knew function and rename it because i want to keep
    this progress
    '''


    def uniformCostSearch(self, startNode, goalNode):
        self.startNode = startNode
        self.goalNode = goalNode
        self.openList.put((0, startNode, 'n/a'))  # the cost to start at the start node is ZERO
        print("Add " + startNode + " to open list at cost 0.")

        while self.openList:
            print("Open List is " + str(self.openList.queue))
            cost, node, parent = self.openList.get()  # get priority value from the openList
            print("Remove " + node + " from open list.")
            print("Open List is " + str(self.openList.queue))

            print("Check if " + node + " is in the closed list.")
            print("It is not, so...")
            self.closedList.add(node)  # not in closed list, so add it
            self.closedList2.put((node, cost, parent)) # keep track of order removed from closed list
            print("Add " + node + " to closed list.")
            self.nodeCountClosed[node] += 1

            if node == goalNode:
                print("Node " + node + " is the goal node! \n\n")
                self.totalCost = cost
                self.showFinalResults()
                return

            print("Checking the neighbors of node " + node)
            for neighbor in self.getNodeNeighbors(node):  # check all neighbors of the node
                print("Checking the neighbor " + neighbor + " of node " + node)
                if neighbor not in self.closedList:  # if the neighbor hasn't been closedList
                    print("Neighbor " + neighbor + " is not in closed list so...")
                    self.totalCost = cost + self.getPathCost(node, neighbor)
                    self.openList.put((self.totalCost, neighbor, node))
                    print("Add " + neighbor + " to open list at cost " + str(self.totalCost) + ".")
                    self.totalAddedToOpenListCounter += 1
                else:
                    print("Neighbor " + neighbor + " is in the closed list. Do nothing with it.")

    # Problem One. DONE. fwm.
    def uniformCostSearchProblem1(self, startNode, goalNode):
        self.startNode = startNode
        self.goalNode = goalNode
        self.openList.put((0, startNode, 'n/a'))  # the cost to start at the start node is ZERO

        while self.openList:
            cost, node, parent = self.openList.get()  # get priority value from the openList

            if node == goalNode:
                print("#########################\nPROBLEM 1\n")
                self.closedList2.put((node, cost, parent))
                self.nodeCountClosed[node] += 1
                self.totalCost = cost
                self.showFinalResults()
                return
            else:
                self.closedList2.put((node, cost, parent))
                self.nodeCountClosed[node] += 1
                for neighbor in self.getNodeNeighbors(node):
                    self.totalCost = cost + self.getPathCost(node, neighbor)
                    self.openList.put((self.totalCost, neighbor, node))
                    self.totalAddedToOpenListCounter += 1


    def resetForRun(self):
        self.closedList = set()
        self.openList = PriorityQueue()
        self.orderRemovedFromOpenList = set()
        self.totalAddedToOpenListCounter = 1
        self.startNode = ''
        self.goalNode = ''
        self.totalCost = 0

    '''
    This works for Problem Two, assuming that you don't want duplicates in the closed list. Pretty sure that's
    how bfs is supposed to work though
    '''
    def breadthFirstSearch(self, startNode, goalNode):
        self.resetForRun()
        for key in self.weights.keys():
            self.weights[key] = 1
        self.uniformCostSearch(startNode, goalNode)
        return

    def getNodeNeighbors(self, node):
        return self.edges[node]

    def getPathCost(self, from_node, to_node):
        if (from_node + to_node) in self.weights:
            return self.weights[(from_node + to_node)]
        # logic to make set input easier and not have to put reverse values
        elif (to_node + from_node) in self.weights:
            return self.weights[(to_node + from_node)]
        else:
            print("The Edge Does Not Exist")
            return

    def showGraph(self):
        pp = pprint.PrettyPrinter(indent=2)
        print("Connections")
        pp.pprint(self.edges)
        print("Weights")
        pp.pprint(self.weights)


# 'Node' is connected to ['Node1', 'Node2', ...]
connections = {  # edge, from node. to node.
    'A': ['B', 'D'],
    'B': ['D', 'C', 'A', 'F'],
    'C': ['B', 'F', 'E'],
    'D': ['A', 'E', 'B', 'G'],
    'E': ['C', 'D', 'J', 'H'],
    'F': ['B', 'C', 'J'],
    'G': ['D', 'H'],
    'H': ['E', 'G', 'J'],
    'J': ['F', 'H', 'E']
}

# 'Node1Node2' : pathCost
weights = {  # edge, what the edge connects
    'AB': 19,
    'AD': 7,
    'BD': 5,
    'BF': 12,
    'BC': 3,
    'CE': 10,
    'DG': 20,
    'DE': 11,
    'EH': 10,
    'GH': 10,
    'HJ': 25,
    'EJ': 10,
    'FJ': 4,
    'CF': 2
}

# Dictionary keeping track of node counts. 'Node': Count
nodeCount = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0
}

print("Benjamin Horn + Elisabeth Bruesewitz")
print("Artificial Intelligence")
print("Homework 1 \n")

# create, set up, and pretty print the graph
graphOne = WeightedGraph()
graphOne.edges.update(connections)
graphOne.weights.update(weights)
graphOne.nodeCountOpen.update(nodeCount)
graphOne.nodeCountClosed.update(nodeCount)


# Problem 1
# graphOne.uniformCostSearchProblem1('A', 'J')

# Problem 2
graphOne.breadthFirstSearch('A', 'J')

# Problem 3


# problem 4
# graphOne.uniformCostSearch('A', 'J')