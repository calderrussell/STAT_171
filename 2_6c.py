import sympy as sp

# --- 1) Enter your vectors (edit these if needed) ---
v1 = sp.Matrix([2, -1,  2,  3,  4])
v2 = sp.Matrix([-1, 2,  3,  1, -2])
v3 = sp.Matrix([-3, -2, 4, -1,  1])
v4 = sp.Matrix([3,  1, -2,  2,  1])

# --- 2) Build the matrix A with columns v1, v2, v3, v4 ---
A = sp.Matrix.hstack(v1, v2, v3, v4)   # 5x4

print("A =")
sp.pprint(A)

# --- 3) Find a nontrivial linear combination c1*v1 + c2*v2 + c3*v3 + c4*v4 = 0 ---
# This is the null space of A
ns = A.nullspace()
print("\nNullspace basis vectors (each gives coefficients [c1,c2,c3,c4]):")
for i, vec in enumerate(ns, start=1):
    print(f"c^{i} =")
    sp.pprint(vec)

if not ns:
    print("\nNullspace is trivial -> the columns are independent (no nontrivial relation).")
else:
    c = ns[0]  # take one dependency
    print("\nUsing the first nullspace vector c =")
    sp.pprint(c)

    # --- 4) Verify the dependence: A*c should be the zero vector in R^5 ---
    check = A * c
    print("\nCheck A*c (should be all zeros):")
    sp.pprint(check)

    # Also verify as a linear combination explicitly
    combo = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    print("\nCheck c1*v1 + c2*v2 + c3*v3 + c4*v4 (should be all zeros):")
    sp.pprint(combo)

    # --- 5) Solve for v4 in the span of v1,v2,v3: a*v1 + b*v2 + d*v3 = v4 ---
    B = sp.Matrix.hstack(v1, v2, v3)  # 5x3
    a, b, d = sp.symbols('a b d')
    sol = sp.linsolve((B, v4))  # solves B*[a,b,d]^T = v4

    print("\nSolutions to a*v1 + b*v2 + d*v3 = v4:")
    print(sol)

    # If a solution exists, print one clean set of coefficients
    if sol:
        sol_list = list(sol)
        if sol_list:
            coeffs = sol_list[0]
            print("\nOne solution (a, b, d) =")
            sp.pprint(coeffs)

            # verify
            verify_span = B * sp.Matrix(coeffs) - v4
            print("\nVerification B*[a,b,d]^T - v4 (should be zeros):")
            sp.pprint(verify_span)