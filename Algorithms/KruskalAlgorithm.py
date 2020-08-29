# kruskal's algorithm is used to find minimum spanning tree - undirected , weighted graph

# kushkal is genrally applied on connected graph
# if kushkal is applied on disonnected graph then it will give minimum spanning tree of all disonnected components

class Graph(object):

    def __init__(self, v):
        self.graph = []  # this is a list where each index will contain a list in form [w,u,v]
        self.v = v

    def addEdge(self, u, v, w):
        self.graph.append([w, u, v])

    def krushkalMST(self):

        # to detect a cycle we need to use union find algorithm

        par = [-1]*self.v

        def find(u):

            while(par[u] > -1):
                u = par[u]
            return u

        # sort graph on the basis of weight bec we need to add minimum edge first in krushkal's algorithm if there is no cycle
        self.graph.sort(key=lambda x: x[0])

        for w, u, v in self.graph:

            paru = find(u)
            parv = find(v)

            if(paru != parv):
                #print par
                print u, " - ", w, " -> ", v

                # if parent are not same then perform union with path compression and ranking

                if(abs(par[paru]) > abs(par[parv])):
                    # add ranking
                    par[paru] += par[parv]
                    par[parv] = par[paru]
                    # note below statement par[v]=paru not par[v]=par[paru] otherwise it will give wrong ans
                    par[v] = paru

                else:
                    # add ranking
                    par[parv] += par[paru]
                    par[paru] = par[parv]
                    par[u] = parv
                    # add ranking


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.krushkalMST()
