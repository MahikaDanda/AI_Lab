def unify(term1, term2, substitution=None):
    if substitution is None:
        substitution = {}
    if term1 == term2:
        return substitution
    if is_var(term1):
        return unify_var(term1, term2, substitution)
    if is_var(term2):
        return unify_var(term2, term1, substitution)
    if is_compound(term1) and is_compound(term2):
        if term1[0] != term2[0] or len(term1[1]) != len(term2[1]):
            return None
        for arg1, arg2 in zip(term1[1], term2[1]):
            substitution = unify(arg1, arg2, substitution)
            if substitution is None:
                return None
        return substitution
    if isinstance(term1, list) and isinstance(term2, list):
        if len(term1) != len(term2):
            return None
        for elem1, elem2 in zip(term1, term2):
            substitution = unify(elem1, elem2, substitution)
            if substitution is None:
                return None
        return substitution
    return None

def unify_var(variable, expr, substitution):
    if variable in substitution:
        return unify(substitution[variable], expr, substitution)
    if expr in substitution:
        return unify(variable, substitution[expr], substitution)
    if occurs(variable, expr, substitution):
        return None
    substitution[variable] = expr
    return substitution

def occurs(variable, expr, substitution):
    if variable == expr:
        return True
    if is_compound(expr):
        return any(occurs(variable, arg, substitution) for arg in expr[1])
    if isinstance(expr, list):
        return any(occurs(variable, item, substitution) for item in expr)
    if expr in substitution:
        return occurs(variable, substitution[expr], substitution)
    return False

def is_var(term):
    return isinstance(term, str) and term.startswith('?')

def is_compound(term):
    return isinstance(term, tuple) and len(term) == 2 and isinstance(term[1], list)

if __name__ == "__main__":
    print("Input format:")
    print("Compound: ('predicate', ['arg1', 'arg2'])")
    print("Variable: '?var'")
    print("List: ['a', 'b']")
    print("Constant: 'a', 'b'\n")
    t1 = eval(input("Enter first term: "))
    t2 = eval(input("Enter second term: "))
    result = unify(t1, t2)
    if result is None:
        print("Result: Unification failed")
    else:
        print("Result: Unification successful")
        print("Substitution:", result)
