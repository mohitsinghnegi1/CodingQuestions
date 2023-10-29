# Qus:https://www.codingninjas.com/studio/problems/985311?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0


def stronglyConnectedComponents(n, edges):
    # Write your code here

    graph = {}

    for i in range(n):
        graph[i] = []

    for u, v in edges:
        graph[u].append(v)

    # graph is done now , find the scc
    # first get topologic sort in reverse order
    visited = {}
    topo = []

    def dfs(src, topo, graph):
        visited[src] = True

        for v in graph[src]:
            if (v not in visited):
                dfs(v, topo, graph)

        topo.append(src)

    for u in range(n):
        if (u not in visited):
            dfs(u, topo, graph)

    # then transpose the edges

    revGraph = {}
    for i in range(n):
        revGraph[i] = []

    for u, v in edges:
        revGraph[v].append(u)

    # then perform the dfs again and print the nodes in a SCC
    def print_scc(scc):
        print(scc)
        for u in scc:
            print(u, )

    visited = {}

    ans = []
    for u in topo[::-1]:

        if (u not in visited):
            scc = []
            dfs(u, scc, revGraph)
            # print_scc(scc)
            ans.append(scc)
            # print()

    return ans






