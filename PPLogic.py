import sympy

p = sympy.symbols('p')
q = sympy.symbols('q')
r = sympy.symbols('r')

prop1 = p
prop2 = sympy.Not(q)
prop3 = sympy.And(p, q)
prop4 = sympy.Or(p, q)
prop5 = sympy.Implies(p, q)
prop6 = sympy.Eq(p, q)

prop7 = sympy.Not(p)
prop8 = sympy.And(p, p)
prop9 = sympy.Or(p, p)
prop10 = sympy.Or(p, sympy.Not(p))
prop11 = sympy.And(p, sympy.Not(p))
prop12 = sympy.Implies(p, q).simplify()

prop15 = sympy.Eq(sympy.Or(p, q), sympy.Or(q, p))
prop16 = sympy.Eq(sympy.And(p, q), sympy.And(q, p))
prop17 = sympy.Eq(sympy.Or(p, sympy.Or(q, r)), sympy.Or(sympy.Or(p, q), r))
prop18 = sympy.Eq(sympy.And(p, sympy.And(q, r)), sympy.And(sympy.And(p, q), r))
prop19 = sympy.Eq(sympy.Or(p, sympy.And(q, r)), sympy.And(sympy.Or(p, q), sympy.Or(p, r)))

prop13 = sympy.Or(p, q, r)
prop14 = sympy.And(p, q, r)

p_value = True
q_value = False

print("p =", p_value, "q =", q_value)
print("prop1:", prop1.subs({p: p_value}))
print("prop2:", prop2.subs({q: q_value}))
print("prop3:", prop3.subs({p: p_value, q: q_value}))
print("prop4:", prop4.subs({p: p_value, q: q_value}))
print("prop5:", prop5.subs({p: p_value, q: q_value}))
print("prop6:", prop6.subs({p: p_value, q: q_value}))
print("prop7:", prop7.subs({p: p_value}))
print("prop8:", prop8.subs({p: p_value}))
print("prop9:", prop9.subs({p: p_value}))
print("prop10:", prop10.subs({p: p_value}))
print("prop11:", prop11.subs({p: p_value}))
print("prop12:", prop12.subs({p: p_value, q: q_value}))
print("prop15:", prop15.subs({p: p_value, q: q_value}))
print("prop16:", prop16.subs({p: p_value, q: q_value}))
print("prop17:", prop17.subs({p: p_value, q: q_value, r: p_value}))
print("prop18:", prop18.subs({p: p_value, q: q_value, r: p_value}))
print("prop19:", prop19.subs({p: p_value, q: q_value, r: p_value}))

def is_valid(proposition):
    return all(proposition.subs({p: p_val, q: q_val}) for p_val in [True, False] for q_val in [True, False])

print("Is prop1 valid?", is_valid(prop1))
print("Is prop2 valid?", is_valid(prop2))
print("Is prop3 valid?", is_valid(prop3))
print("Is prop4 valid?", is_valid(prop4))
print("Is prop5 valid?", is_valid(prop5))
print("Is prop6 valid?", is_valid(prop6))

print("Satisfiable prop1:", sympy.satisfiable(prop1))
print("Satisfiable prop2:", sympy.satisfiable(prop2))
print("Satisfiable prop3:", sympy.satisfiable(prop3))
print("Satisfiable prop4:", sympy.satisfiable(prop4))

entailment = all(
    (not prop1.subs({p: a, q: b}) or prop2.subs({p: a, q: b}))
    for a in [True, False]
    for b in [True, False]
)

print("Entailment:", entailment)

print("DNF:", sympy.to_dnf(prop13))
print("CNF:", sympy.to_cnf(prop13))
print("DNF:", sympy.to_dnf(prop14))
print("CNF:", sympy.to_cnf(prop14))
