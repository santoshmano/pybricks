


def min_cost(cost, start, dest):

    if start >= len(cost) or dest >= len(cost):
        return -1

    if start == dest or start == dest-1:
        return cost[start][dest]

    mincost = cost[start][dest]
    for mid in range(start+1, dest):
        tempcost = min_cost(cost, start, mid) + min_cost(cost, mid, dest)

        if tempcost < mincost:
            mincost = tempcost

    return mincost


def min_cost_mem(cost, mem, start, dest):

    if start >= len(cost) or dest >= len(cost):
        return -1

    if start == dest or start == dest-1:
        return cost[start][dest]

    if mem[start][dest] == -1:
        mincost = cost[start][dest]
        for mid in range(start+1, dest):
            temp = min_cost_mem(cost, mem, start, mid) \
                   + min_cost_mem(cost, mem, mid, dest)

            if temp < mincost:
                mincost = temp

            mem[start][dest] = mincost

    return mem[start][dest]


max_stations = 4
#cost = [0 for _ in range(0, max_stations) for _ in range(0, max_stations)]

cost = [[ 0,  4,  5,  9],
        [-1,  0,  2,  6],
        [-1, -1,  0,  1],
        [-1, -1, -1,  0]]

# mc(i,j) = mc(i, mid) + mc(mid,j)
print(min_cost(cost, 2, 3))
print(min_cost(cost, 1, 3))
print(min_cost(cost, 0, 3))
print(min_cost(cost, 0, 2))
print(min_cost(cost, 1, 2))


mem = [[-1 for _ in range(len(cost))] for _ in range(len(cost))]
print(min_cost_mem(cost, mem, 2, 3))
print(min_cost_mem(cost, mem, 1, 3))
print(min_cost_mem(cost, mem, 0, 3))
print(min_cost_mem(cost, mem, 0, 2))
print(min_cost_mem(cost, mem, 1, 2))

