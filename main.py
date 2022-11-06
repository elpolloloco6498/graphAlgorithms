from pprint import pprint

graph = {
    'a': ['c','b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

graph2 = {
    'f': ['g','i'],
    'g': ['h'],
    'i': ['g','k'],
    'j': ['i'],
    'h': [],
    'k': []
}

edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n']
]

def depthFirstPrint(source, graph):
    stack = list()
    stack.append(source)

    while stack:
        current = stack.pop()
        print(current)
        for child in graph[current]:
            stack.append(child)

def breadthFirstPrint(source, graph):
    queue = list()
    queue.append(source)
    while queue:
        current = queue.pop(0)
        print(current)
        for child in graph[current]:
            queue.append(child)

def hasPath(graph, source, dest):
    stack = list()
    stack.append(source)
    verified = set()

    while stack:
        current = stack.pop()
        if current not in verified:
            print(current)
            verified.add(current)
            if current == dest:
                return True
            for child in graph[current]:
                stack.append(child)
    return False

def buildGraph(edges):
    graph = dict()
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def undirectedPath(edges, src, dest):
    graph = buildGraph(edges)
    print(hasPath(graph, src, dest))

undirectedPath(edges, 'i', 'l')