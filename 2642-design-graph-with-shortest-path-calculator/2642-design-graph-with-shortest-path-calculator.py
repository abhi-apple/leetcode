class Graph:
    def __init__(self, n: int, edges: List[List[int]]):

        self.adjacencyList = [[] for _ in range(n)]


        for edge in edges:
            self.adjacencyList[edge[0]].append((edge[1], edge[2]))


    def addEdge(self, edge: List[int]):
        self.adjacencyList[edge[0]].append((edge[1], edge[2]))


    def shortestPath(self, node1: int, node2: int) -> int:
        return self.dijkstra(node1, node2)


    def dijkstra(self, start: int, end: int) -> int:
        n = len(self.adjacencyList)
        distances = [float('inf')] * n
        distances[start] = 0


        priorityQueue = [(0, start)]

        while priorityQueue:
            currentCost, currentNode = heapq.heappop(priorityQueue)


            if currentCost > distances[currentNode]:
                continue


            if currentNode == end:
                return currentCost


            for edge in self.adjacencyList[currentNode]:
                neighbor, edgeLength = edge
                newRouteCost = edgeLength + distances[currentNode]


                if distances[neighbor] > newRouteCost:
                    distances[neighbor] = newRouteCost
                    heapq.heappush(priorityQueue, (newRouteCost, neighbor))


        return -1 if distances[end] == float('inf') else distances[end]
