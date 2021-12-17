from collections import Counter

with open("advent/14/14a.txt") as f:
    data = f.read()

polymer_template, rules = data.split("\n\n")
insertions = {}

for rule in rules.split("\n"):
    elems, elem = rule.split(" -> ")
    insertions[elems] = elems[0] + elem + elems[1]


for step in range(40):

    print(f"Step {step+1}")
    polymer_templates = []

    for i in range(len(polymer_template)-1):
        polymer_templates.append(polymer_template[i:i+2])

    current_templates = []

    for current_template in polymer_templates:

        i = 0
        while i < len(current_template)-1:
            sign = current_template[i:i+2]
            try:
                current_template = current_template[:i] + \
                    insertions[sign] + current_template[i+2:]
                i += 1
            except KeyError:
                pass

            i += 1

        current_templates.append(current_template)
    polymer_template = ""
    for temp in current_templates[:-1]:
        polymer_template += temp[:-1]
    polymer_template += current_templates[-1]

    print(len(polymer_template))

counts = Counter(polymer_template)
print(max(counts.values()) - min(counts.values()))
