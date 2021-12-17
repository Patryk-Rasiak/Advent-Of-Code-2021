import sys

data = [[int(c) for c in l.strip()] for l in open("advent/15/15a.txt")]


def step(ij, v, p, u, w, N):

    v[ij] = True
    u.remove(ij)
    i, j = ij // N, ij % N

    # Update neighbors
    for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        if 0 <= ni < N and 0 <= nj < N:
            nij = N * ni + nj

            if v[nij]:
                continue

            if p[ij] + w[nij] < p[nij]:
                p[nij] = p[ij] + w[nij]
                u.append(nij)

    # Min unvisited
    mij = mp = sys.maxsize
    for uij in u:
        if p[uij] < mp:
            mij = uij
            mp = p[uij]

    return mij


def solve(data):
    N = len(data)
    NN = N*N
    I = sys.maxsize
    w = []  # Weights, 1-dimension copy of input
    for i in range(N):
        w += data[i]

    v = [False for _ in range(NN)]  # Visited
    p = [I for _ in range(NN)]  # Paths
    u = []  # Unvisited items (ij indexes)
    p[0] = 0  # Start with top left corner
    u.append(0)
    uij = step(0, v, p, u, w, N)
    while u:
        uij = step(uij, v, p, u, w, N)
    return p[NN-1]  # Right bottom


print(solve(data))
