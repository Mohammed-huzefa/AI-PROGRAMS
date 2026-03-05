def forward_chaining(rules, facts, goal):
    facts = set(facts)
    while True:
        added = False
        for cond, res in rules:
            if all(c in facts for c in cond) and res not in facts:
                facts.add(res)
                added = True
                if res == goal:
                    return True
        if not added:
            return False


def backward_chaining(rules, facts, goal):
    if goal in facts:
        return True
    for cond, res in rules:
        if res == goal:
            if all(backward_chaining(rules, facts, c) for c in cond):
                return True
    return False


rules = [
    (['hair','live young'],'mammal'),
    (['feathers','fly'],'bird')
]

facts = ['hair','live young']

if forward_chaining(rules,facts,'mammal'):
    print("Cat is Mammal")

facts = ['feathers','fly']

if backward_chaining(rules,facts,'bird'):
    print("Pigeon is Bird")