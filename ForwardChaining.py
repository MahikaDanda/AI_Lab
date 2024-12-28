class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def infer(self):
        derived_new = True
        while derived_new:
            derived_new = False
            for rule in self.rules:
                if rule.evaluate(self.facts):
                    derived_new = True


class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion

    def evaluate(self, facts):
        if all(condition in facts for condition in self.conditions):
            if self.conclusion not in facts:
                facts.add(self.conclusion)
                print(f"Derived: {self.conclusion}")
                return True
        return False


kb = KnowledgeBase()
kb.add_fact("American(Robert)")
kb.add_fact("Missile(T1)")
kb.add_fact("Owns(A, T1)")
kb.add_fact("Enemy(A, America)")

kb.add_rule(Rule(["Missile(T1)"], "Weapon(T1)"))
kb.add_rule(Rule(["Enemy(A, America)"], "Hostile(A)"))
kb.add_rule(Rule(["Missile(T1)", "Owns(A, T1)"], "Sells(Robert, T1, A)"))
kb.add_rule(Rule(["American(Robert)", "Weapon(T1)", "Sells(Robert, T1, A)", "Hostile(A)"], "Criminal(Robert)"))

kb.infer()

if "Criminal(Robert)" in kb.facts:
    print("Outcome: Robert is a criminal.")
else:
    print("Outcome: Unable to prove Robert is a criminal.")
