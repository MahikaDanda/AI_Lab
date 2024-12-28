from itertools import combinations

def unify(term1, term2, substitution={}):
    if substitution is None:
        return None
    elif term1 == term2:
        return substitution
    elif isinstance(term1, str) and term1.islower():
        return unify_var(term1, term2, substitution)
    elif isinstance(term2, str) and term2.islower():
        return unify_var(term2, term1, substitution)
    elif isinstance(term1, tuple) and isinstance(term2, tuple) and len(term1) == len(term2):
        return unify(term1[1:], term2[1:], unify(term1[0], term2[0], substitution))
    else:
        return None

def unify_var(variable, value, substitution):
    if variable in substitution:
        return unify(substitution[variable], value, substitution)
    elif value in substitution:
        return unify(variable, substitution[value], substitution)
    else:
        substitution[variable] = value
        return substitution

def resolve_clause(clause1, clause2):
    resolvents = []
    for term1 in clause1:
        for term2 in clause2:
            substitution = unify(term1, negate_term(term2))
            if substitution is not None:
                new_clause = (apply_substitution(clause1, substitution) | apply_substitution(clause2, substitution)) - {term1, term2}
                resolvents.append(frozenset(new_clause))
    return resolvents

def negate_term(predicate):
    return ('not', predicate) if isinstance(predicate, str) else predicate[1]

def apply_substitution(clause, substitution):
    return {apply_single_substitution(p, substitution) for p in clause}

def apply_single_substitution(predicate, substitution):
    if isinstance(predicate, str):
        return substitution.get(predicate, predicate)
    else:
        return (predicate[0],) + tuple(substitution.get(arg, arg) for arg in predicate[1:])

def resolution_proof(kb, query):
    negated_query = frozenset({negate_term(query)})
    clauses = kb | {negated_query}
    new_clauses = set()

    while True:
        for clause1, clause2 in combinations(clauses, 2):
            resolvents = resolve_clause(clause1, clause2)
            if frozenset() in resolvents:
                return True
            new_clauses.update(resolvents)
        if new_clauses.issubset(clauses):
            return False
        clauses |= new_clauses

kb = {
    frozenset({('Mother', 'Leela', 'Oshin')}),
    frozenset({('Alive', 'Leela')}),
    frozenset({('not','Mother', 'x','y')}),
    frozenset({('Parent','x','y')}),
    frozenset({('not','Parent', 'w', 'z')}),
    frozenset({('not','Alive','w','z')}),
    frozenset({('Older','w','z')}),
}

query = ('Older', 'Leela', 'Oshin')

result = resolution_proof(kb, query)
if result:
    print("Proved by resolution: Leela is older than Oshin.")
else:
    print("Cannot prove: Leela is not older than Oshin.")
