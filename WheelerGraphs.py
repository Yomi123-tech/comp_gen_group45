class WheelerGraphs:
    def __init__(self):
        self.graph = {}
        self.node_labels = {}

    def addEdge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)

    def createGraph(self):
        numNodes = int(input("Enter the number of nodes: "))
        for _ in range(numNodes):
            node = input("Enter node: ")
            label = float(input("Enter the label for the node: "))
            self.graph[node] = []
            self.node_labels[node] = label

        numEdges = int(input("Enter the number of edges: "))
        for _ in range(numEdges):
            node1 = input("Enter the source node for the edge: ")
            node2 = input("Enter the target node for the edge: ")
            self.addEdge(node1, node2)

    def displayGraph(self):
        for node in self.graph:
            edges = ', '.join(self.graph[node])
            print(f"{node} (label {self.node_labels[node]}) -> {edges}")

    def checkZeroInDegreeFirst(self):
        zeroInDegreeNodes = set()
        for node in self.graph:
            if all(node != destination for edges in self.graph.values() for destination in edges):
                zeroInDegreeNodes.add(node)
        sortedNodesByLabel = sorted(self.graph, key=lambda x: self.node_labels[x])
        firstNodes = sortedNodesByLabel[:len(zeroInDegreeNodes)]
        for node in firstNodes:
            if node not in zeroInDegreeNodes:
                return False
        return True

    def checkNodeLabelOrdering(self):
        return list(self.graph) == sorted(self.graph, key=lambda x: self.node_labels[x])

    def checkConsistentDestinationOrdering(self):
        for node1 in self.graph:
            for node2 in self.graph:
                if node1 != node2:
                    commonDestinations = set(self.graph[node1]).intersection(self.graph[node2])
                    for dest in commonDestinations:
                        if self.node_labels[node1] > self.node_labels[node2]:
                            return False
        return True

    def isWheelerGraph(self):
        return self.checkZeroInDegreeFirst() and self.checkNodeLabelOrdering() and self.checkConsistentDestinationOrdering()

if __name__ == "__main__":
    wg = WheelerGraphs()
    wg.createGraph()
    wg.displayGraph()
    print("True of False: This is a Wheeler Graph:", wg.isWheelerGraph())