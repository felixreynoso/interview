from collections import defaultdict

#Graph Data Structure Implementation
class Graph:
    def __init__(self, gdict={}):
        self.vertices = set(gdict.keys())
        self.adj = gdict
    
    def __str__(self):
        return self.adj.__str__()

    def getVertices(self):
        return list(self.vertices)
    
    def getEdges(self):
        edges = []
        for v in self.getVertices():
            for u in self.adj[v]:
                if {u,v} not in edges:
                    edges.append({u,v})
        return edges

    def addVertex(self, vrtx):
        self.vertices.add(vrtx)
        if vrtx not in self.adj:
            self.adj[vrtx] = []

    def addEdge(self, edge):
        u, v = edge
        self.addVertex(u)
        self.addVertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def connectedComponents(self):
        cc = []
        visited = dict.fromkeys(self.getVertices(), False)

        for v in self.getVertices():
            if visited[v]== False:
                # visited[v] = True
                # cc.append(self.BFSUtil(v, visited))
                tmp = []
                cc.append(self.DFSUtil(v, visited, tmp))

        return cc
        
    def BFSUtil(self, vrtx, visited):
        tmp = []
        queue = [vrtx]

        while queue:
            vrtx = queue.pop(0)
            tmp.append(vrtx)

            for adjVrtx in self.adj[vrtx]:
                if visited[adjVrtx] == False:
                    visited[adjVrtx] = True
                    queue.append(adjVrtx)
        return tmp
            
    def DFSUtil(self, vrtx, visited, tmp):
        tmp.append(vrtx)
        visited[vrtx] = True
        
        for adjVrtx in self.adj[vrtx]:
            if visited[adjVrtx] == False:
                tmp = self.DFSUtil(adjVrtx, visited, tmp)
        return tmp


# Sample input provided by Georgi
input = [
    ["felix", "felix1@gmail.com", "felix2@gmail.com"],
    ["felix", "felix2@gmail.com", "felix3@gmail.com"],
    ["felix", "felix4@gmail.com"],
    ["mariel", "mariel1@gmail.com", "mariel3@gmail.com"],
    ["mariel", "mariel4@gmail.com", "mariel5@gmail.com"],
    ["tom", "tom1@gmail.com", "tom2@gmail.com"],
    ["tom", "tom2@gmail.com", "tom3@gmail.com"]
]

# SOLUTION
people = defaultdict(lambda:[])

# Scan input and append emails to the corresponding person
for entry in input:
    name = entry[0]
    people[name].append(entry[1:])

#initialize results var which will hold a graph for every person
results  = {}

for person in people.keys():
    results[person] = Graph({})


# Add emails to the graph
for person in people:
    for edges in people[person]:

        if len(edges) == 1:
            results[person].addVertex(edges[0])
        else:
            for i in range(len(edges)-1):
                results[person].addEdge((edges[i],edges[i+1]))

# Print results 
for person in results.keys():
    cc = results[person].connectedComponents()
    for component in cc:
        print(person+':', ', '.join(component))