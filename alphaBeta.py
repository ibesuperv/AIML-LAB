from math import log2

leaves = [30, 1, 6, 5, 1, 2, 10, 20]
n = len(leaves)
DEPTH = int(log2(n))

LEAF_START =  2 ** DEPTH

def alphabeta(node, depth, alpha, beta, maxPlayer):
    if depth == 0:
        return leaves[node  - LEAF_START]
    
    if maxPlayer:
        maxEva = float('-inf')
        for child in [node * 2, node * 2 + 1]:
            eva = alphabeta(child, depth - 1, alpha, beta, False)
            maxEva = max(maxEva, eva)
            alpha = max(maxEva, alpha)
            if alpha >= beta:
                break
        return maxEva
    else:
        minEva = float('inf')
        for child in [node * 2, node * 2 + 1]:
            eva = alphabeta(child, depth - 1, alpha, beta, True)
            minEva = min(minEva, eva)
            alpha = min(minEva, alpha)
            if alpha >= beta:
                break
        return minEva
    
print("Evaaluated Value: ", alphabeta(1, DEPTH, float("-inf"), float('inf'), True))