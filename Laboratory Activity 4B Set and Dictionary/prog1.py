A = {'a', 'b', 'd', 'f', 'g'}
B = {'b', 'c', 'd', 'f', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# a. Count of common elements between A and B
common_AB = A.intersection(B)
print("a. Elements present in both A and B:", len(common_AB))

# b. Elements in B that are neither in A nor C
exclusive_B = B.difference(A.union(C))
print("b. Elements in B but not in A or C:", len(exclusive_B))

# c.i. Elements in C that are unique to it
unique_C = C.difference(A.union(B))
print("c.i:", unique_C)

# c.ii. Common elements between B and C
common_BC = B.intersection(C)
print("c.ii:", common_BC)

# c.iii. Elements in at least one set but not in all three
union_all = A.union(B, C)
intersection_all = A.intersection(B, C)
not_all_three = union_all.difference(intersection_all)
print("c.iii:", not_all_three)

# c.iv. Elements in both A and B but not in C
AB_not_C = A.intersection(B).difference(C)
print("c.iv:", AB_not_C)

# c.v. Elements exclusive to B (not in A or C)
exclusive_BC = B.difference(A.union(C))
print("c.v:", exclusive_BC)

# c.vi. Another way to get elements unique to B
unique_B = B - (A | C)
print("c.vi:", unique_B)
