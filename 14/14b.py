from collections import Counter

with open("advent/14/14b.txt") as f:
    data = f.read()

polymer_template, rules = data.split("\n\n")
insertions = {}

for rule in rules.split("\n"):
    elems, elem = rule.split(" -> ")
    insertions[elems] = elems[0] + elem + elems[1]

for step in range(40):
    print(step+1)
    i = 0
    while i < len(polymer_template)-1:
        sign = polymer_template[i:i+2]
        try:
            polymer_template = polymer_template[:i] + \
                insertions[sign] + polymer_template[i+2:]
            i += 1
        except KeyError:
            pass

        i += 1

counts = Counter(polymer_template)

print(max(counts.values()) - min(counts.values()))
