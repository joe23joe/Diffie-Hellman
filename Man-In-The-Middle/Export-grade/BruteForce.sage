p = 0xde26ab651b92a129
g = 0x2
A = 0x75fd99ecf65fecd5

alice_secretKey = discrete_log(A, Mod(g, p))
print(alice_secretKey)

// alice_secretKey = 3694381458720902541