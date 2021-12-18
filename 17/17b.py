
# Initialize data
data = open("advent/17/17b.txt").read()[13:]
xs, ys = data.split(", ")
tx1, tx2 = [int(x) for x in xs[2:].split("..")]
ty1, ty2 = [int(y) for y in ys[2:].split("..")]


def step(S, vel_x, vel_y):
    S[0] += vel_x
    S[1] += vel_y

    if vel_x > 0:
        vel_x -= 1
    elif vel_x < 0:
        vel_x += 1

    vel_y -= 1

    return S, vel_x, vel_y


def is_in_target(S):
    global tx1, tx2, ty1, ty2

    return tx1 <= S[0] <= tx2 and ty1 <= S[1] <= ty2


def solve(tx1, tx2, ty1, ty2):
    S = [0, 0]
    hits = {}
    for vel_x in range(-1000, 1000):
        for vel_y in range(-1000, 1000):
            S = [0, 0]
            curr_vel_x = vel_x
            curr_vel_y = vel_y

            # Maximum height of these velocities
            max_y = 0
            while True:
                S, curr_vel_x, curr_vel_y = step(S, curr_vel_x, curr_vel_y)
                if S[1] > max_y:
                    max_y = S[1]
                if is_in_target(S):
                    if (vel_x, vel_y) not in hits.keys() or hits[(vel_x, vel_y)] < max_y:
                        hits[(vel_x, vel_y)] = max_y
                # If bullet is under the target area and still falls down, break the loop
                if S[1] < ty1 and curr_vel_y < 0:
                    break

    return len(hits.keys())


result = solve(tx1, tx2, ty1, ty2)
print(result)
