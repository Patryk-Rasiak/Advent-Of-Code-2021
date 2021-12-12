from collections import defaultdict, deque, Counter

# Dictionary of neighbors of all caves
neighbors = defaultdict(list)

with open("advent/12/12b.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

    for line in data:
        a, b = line.split("-")
        neighbors[a].append(b)
        neighbors[b].append(a)


# Function to check if we can visit a small cave twice
def can_visit_twice(neighbor, path):

    if neighbor in ["start", "end"]:
        return False
    else:
        # If all of the small caves appeared no more than once, return True
        for k, v in Counter(path).items():
            if k.islower() and v > 1:
                return False
        return True


count = 0

queue = deque([["start"]])

while queue:
    path = queue.popleft()
    last = path[-1]

    # If last element is the end, increment the counter
    if last == "end":
        count += 1
        continue

    # Check neighbors
    for neighbor in neighbors[last]:

        # If neighbor is uppercase or already in path or we haven't visited twice yet,
        # then add a copy of the current path to the queue
        if neighbor.isupper() or neighbor not in path or can_visit_twice(neighbor, path):
            path_copy = path.copy()
            path_copy.append(neighbor)
            queue.append(path_copy)

print(count)
