
# THE CLEVER WAY TO SOLVE 

import sympy as sp

def smallest_primitive_root(p):
    # we get the values that (p-1) can be divisible by p
    factors = sp.factorint(p - 1)     
    prime_factors = list(factors.keys())  
    
    # test each number g = 2, 3, 4, ...
    # if the number pass the test for each 3 values (prime_factors) then it must be the generater
    for g in range(2, p):
        is_generator = True
        for q in prime_factors:
            # If g^((p-1)/q) ≡ 1 mod p, then g is NOT a generator
            if pow(g, (p - 1) // q, p) == 1:
                is_generator = False
                break
        if is_generator:
            return g

if __name__ == "__main__":
    p = 28151
    g = smallest_primitive_root(p)
    print("Smallest generater for modulo", p, "is", g)



# ANY NORMAL DUDE SOLUTION


def is_generator_brute_force(g, p):
    powers = set()
    for k in range(1, p):
        val = pow(g, k, p)
        if val in powers:  # duplicate found → g cannot be the generater
            return False
        powers.add(val)
    return True

p = 28151
for g in range(2, p):
    if is_generator_brute_force(g, p):
        print("Smallest generater for modulo", p, "is", g)
        break
