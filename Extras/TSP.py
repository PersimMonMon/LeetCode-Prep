
def solve_tsp(G):
    length = len(G)

    # solve using Greedy, make False array
    visited = [False] * length
    visited[0] = True
    order = [0]            # note which node traveled to
    curr = 0

    for i in range(length-1):

        # reset values
        nearest = None
        lowest_val = float("inf")


        for j in range(length):
            if not visited[j] and G[curr][j] != 0:      # check if not 0 b/c can't travel to itself
                if G[curr][j] < lowest_val:
                    lowest_val = G[curr][j]
                    nearest = j

        if nearest is None:
            return None

        # append, update visited, and curr
        order.append(nearest)
        visited[nearest] = True
        curr = nearest

    # append initial and return order
    order.append(0)
    return order




