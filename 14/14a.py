with open("advent/14/14a.txt") as f:
    data = f.read().split("\n\n")

polymer_template = data[0]
rules = {}

for rule in data[1].split("\n"):
    k, v = rule.split(" -> ")
    rules[k] = v

elems = {k: 0 for k in rules.keys()}
counts = {k: 0 for k in set(rules.values())}


for i in range(len(polymer_template) - 1):
    elems[polymer_template[i:i+2]] += 1

for i in range(len(polymer_template)):
    counts[polymer_template[i]] += 1


for step in range(40):

    new_elems = {k: 0 for k in rules.keys()}

    for elem, count in elems.items():
        char = rules[elem]

        new_elems[elem[0] + char] += count
        new_elems[char + elem[1]] += count

        counts[char] += count

    elems = new_elems

print(max(counts.values()) - min(counts.values()))
