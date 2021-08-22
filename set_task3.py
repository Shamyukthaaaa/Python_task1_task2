set1 = {4,5,2,6,8,0}
set2 = {1,2,3,4}

#union
set3 = set1.union(set2)
print("Union of set1 and set2 is ",set3)

#intersection
set4 = set1.intersection(set2)
print("Intersection of set1 and set2 is ",set4)

#difference
set5 = set1.difference(set2)
print("Difference of set1 and set2 is ",set5)

#symmetric difference
set6 = set1.symmetric_difference(set2)
print("Difference of set1 and set2 is ",set6)
