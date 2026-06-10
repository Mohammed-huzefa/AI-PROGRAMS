class FC:
    def __init__(self, r, f):
        self.r = r
        self.f = set(f)

    def apply(self):
        change = True
        while change:
            change = False
            for a, c in self.r:
                if a.issubset(self.f) and c not in self.f:
                    self.f.add(c)
                    change = True


rules = [
    ({"has_fur(tiger)"}, "mammal(tiger)"),
    ({"has_feathers(penguin)", "lays_eggs(penguin)"}, "bird(penguin)")
]

facts = {
    "has_fur(tiger)",
    "has_feathers(penguin)",
    "lays_eggs(penguin)"
}

fc = FC(rules, facts)
fc.apply()

print("Derived Facts:", fc.f)