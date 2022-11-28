from itertools import permutations
V = 4
s=0
vertex = []
for i in range(V):
    if i != s:
        vertex.append(i)

next_permutation = permutations(vertex)
print(next_permutation)