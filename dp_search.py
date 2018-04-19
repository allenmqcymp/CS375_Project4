# dynamic programming search algorithm for the subset sum problem
# CS375 Project 4


def dp_search(l, k):
    # 0 is the trivial case
    if k == 0:
        return True

    n = len(l)
    # we will use a n x k boolean matrix to represent the state
    Q = [ [None] * k for _ in range(n) ]

    # fill the state table bottom up
    for i in range(n):
        for j in range(k):
            fill(Q, i, j, k, l)

    return Q[n-1][k-1]


def fill(Q, i, j, k, l):
    # base case
    # we assume that the smallest sum that starts is 1
    if i == 0:
        subset_sum = l[0]
        Q[i][j] = (subset_sum == j + 1)
    else:
        # take into account list indexing fencepost error
        current_elem = l[i]
        # take into account 0 indexing
        if current_elem == j + 1:
            Q[i][j] = True
        elif Q[i - 1][j]:
            Q[i][j] = True
        elif current_elem < j + 1:
            Q[i][j] = Q[i - 1][j - current_elem]
        else:
            Q[i][j] = False


def main():
    print(dp_search([1, 2, 4, 6, 10], 28))


if __name__ == "__main__":
    main()