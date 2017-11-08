from Queue import PriorityQueue, Queue
import pprint


# Set up a graph of connections and weights
class WeightedGraph:
    def __init__(self):
        self.edges = {}
        self.weights = {}
        self.heuristics = {}
        self.closedList = set() # check this to see if node is in closed list
        self.closedList2 = Queue() # keep track of closed list/order removed from open
        self.openList = PriorityQueue()
        self.totalAddedToOpenListCounter = 1
        self.nodeCountOpen = {}  # for 1d
        self.nodeCountClosed = {}  # for 1e
        self.startNode = ''
        self.goalNode = ''
        self.totalCostWithHeuristic = 0
        self.totalCostWithOutHeuristic = 0

    def showFinalResults(self):
        print("From Node " + self.startNode + " to Node " + self.goalNode)
        print("Total Cost: " + str(self.totalCostWithOutHeuristic))
        print("A: Order Removed From Open List: " + str(self.closedList2.queue))
        print("B: Open List when Goal Found: "),
        # have to use a while loop to get the heap to print in order.
        while self.openList.qsize() != 0:
            withH, node, parent, withOutH = self.openList.get()
            self.nodeCountOpen[node] += 1
            print("[" + str(node) + ', ' + str(withOutH) + ', ' + str(withH - withOutH) + ', ' + str(parent) + "]"),
        print("\nB: Closed List when Goal Found: " + str(self.closedList2.queue))
        print("C: Total Nodes Added to Open List: " + str(self.totalAddedToOpenListCounter))
        print("D: Total time each node appears as the current node in the final open list: " + str(self.nodeCountOpen))
        print(
        "E: Total time each node appears as the current node in the final closed list: " + str(self.nodeCountClosed))

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

    def getHeuristicValue(self, node):
        return self.heuristics['h' + node]

    def showGraph(self):
        pp = pprint.PrettyPrinter(indent=2)
        print("Connections")
        pp.pprint(self.edges)
        print("Weights")
        pp.pprint(self.weights)

    def aStarSearch(self, startNode, goalNode):
        self.startNode = startNode
        self.goalNode = goalNode
        self.openList.put((14, startNode, 'n/a', 0))  # the cost to start at the start node is ZERO
        print("Add " + startNode + " to open list at cost 0.")

        while self.openList:
            print("Open List is " + str(self.openList.queue))
            tempWithHeuristic, node, parent, tempWithOutHeuristic = self.openList.get()

            self.closedList.add(node)  # not in closed list, so add it
            self.closedList2.put((node, tempWithOutHeuristic, tempWithHeuristic - tempWithOutHeuristic, parent)) # keep track of order removed from closed list
            print("Add " + node + " to closed list.")
            self.nodeCountClosed[node] += 1

            if node == goalNode:
                print("Node " + node + " is the goal node! \n\n")

                self.showFinalResults()
                return

            print("Checking the neighbors of node " + node)
            for neighbor in self.getNodeNeighbors(node):  # check all neighbors of the node
                print("Checking the neighbor " + neighbor + " of node " + node)
                if neighbor not in self.closedList:  # if the neighbor hasn't been closedList
                    print("Neighbor " + neighbor + " is not in closed list so...")
                    self.totalCostWithHeuristic = tempWithOutHeuristic + self.getPathCost(node, neighbor) + self.getHeuristicValue(neighbor)
                    self.totalCostWithOutHeuristic = tempWithOutHeuristic + self.getPathCost(node, neighbor)
                    self.openList.put((self.totalCostWithHeuristic, neighbor, node, self.totalCostWithOutHeuristic))
                    self.totalAddedToOpenListCounter += 1
                else:
                    print("Neighbor " + neighbor + " is in the closed list. Do nothing with it.")


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
    'AD': 8,
    'BD': 4,
    'BF': 12,
    'BC': 5,
    'CE': 10,
    'DG': 20,
    'DE': 11,
    'EH': 10,
    'GH': 10,
    'HJ': 25,
    'EJ': 10,
    'FJ': 1,
    'CF': 2
}

# heuristic distances given bny h(Node)
heuristic_distances = {
    'hA': 14,
    'hB': 5,
    'hC': 2,
    'hD': 4,
    'hE': 11,
    'hF': 1,
    'hG': 28,
    'hH': 21,
    'hJ': 0
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
graphOne.heuristics.update(heuristic_distances)
graphOne.nodeCountOpen.update(nodeCount)
graphOne.nodeCountClosed.update(nodeCount)

graphOne.aStarSearch('A', 'J')