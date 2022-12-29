import random

names = ['john', 'jane', 'doe', 'smith', 'alice', 'bob']
domains = ['gmail', 'yahoo', 'outlook', 'protonmail', 'aol']
locals = ['com', 'net', 'org', 'edu']

name = random.choice(names)
domain = random.choice(domains)
local = random.choice(locals)

email = f'{name}@{domain}.{local}'

print(email)

