# Qus:https://leetcode.com/problems/snakes-and-ladders/

def minMoves(moves, end):
    # print(moves)
    queue = deque([])
    visited = {}

    # cell , distance, Note we are initially at first cell
    queue.append((1, 0))

    while(queue):
        v, d = queue.popleft()
        if(v == end):
            return d
        if(v in visited):
            continue
        visited[v] = True

        for i in range(v+1, min(v+7, end+1)):

            if(moves[i] != -1):
                queue.append((moves[i], d+1))
            else:
                queue.append((i, d+1))

    return -1


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        end = len(board)*len(board[0])

        moves = [-1]

        board.reverse()
        # print board

        flag = True

        for i in range(len(board)):
            if(flag):
                for j in range(len(board[0])):
                    moves.append(board[i][j])

            else:
                for j in range(len(board[0])-1, -1, -1):
                    moves.append(board[i][j])

            flag = False if flag else True
            # print flag
        # print moves
        return minMoves(moves, end)
