# Problem - Count number of binary tree given n nodes
#
# Given N nodes, there can be 1 root  for which there are
#   : 1->root left nodes
#   : root->N right nodes
#   -recursively do the above by choosing root in position 1 -> N
#
# Recurrence Relation
# T(n) = sum(K from 1->N) { T(k-1) + T(n-k) }
# T(1) = 1
# T(0) = 1
#
# Time Complexity - O()
# Space Complexity -
#
def binary_trees_nnodes(total_nodes):

    # 0 nodes = 1 null tree, 1 node = 1 root tree
    if total_nodes == 0 or total_nodes == 1:
        return 1

    sum = 0
    for root in range(1, total_nodes+1):

        left_nodes = root-1
        right_nodes = total_nodes-root

        lcount = binary_trees_nnodes(left_nodes)
        rcount = binary_trees_nnodes(right_nodes)

        sum += lcount*rcount

    return sum

for i in range(1, 5):
    print(i, binary_trees_nnodes(i))


