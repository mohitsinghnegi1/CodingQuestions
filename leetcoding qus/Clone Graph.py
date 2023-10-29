# Qus: https: // leetcode.com/problems/clone-graph/x


"""
# Definition for a Node.

"""


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        """
        Intution :
            store refrence of Node and copy in visited dict
            then do bfs or dfs both will work 
            
            at each level append copied child in the neighbor list
            
            if child already in visited dont append it to queue
        
        """

        # if there is no nodes return None
        if(node == None):
            return None

        # create a reference of root node ie val is 1
        par = Node(node.val)

        queue = [node]  # add root node
        visited = {}
        visited[node] = par  # add reference with resepect to the node

        while(queue):
            node1 = queue.pop(0)  # pop the front node in the queue

            for nei in node1.neighbors:  # do append all the child which are not visited in the queueu

                if(nei not in visited):
                    queue.append(nei)
                    # in case node is not in visited the create that node                       # reference and add it to the visited dict
                    visited[nei] = Node(nei.val)
                # add neighbors reference in the                         # reference node of current poped node.
                visited[node1].neighbors.append(visited[nei])

        # return the reference of root node
        return visited[node]


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if (node == None):
            return None

        head = Node(node.val, [])

        d = {}
        d[node] = head

        queue = [node]

        while (queue):

            n1 = queue.pop(0)

            for nei in n1.neighbors:

                if (nei not in d):
                    queue.append(nei)
                    d[nei] = Node(nei.val)

                # add this nei in d[n1]'s neighours
                d[n1].neighbors.append(d[nei])

        return head










