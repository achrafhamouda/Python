dimensions = (20,50,100)
print(dimensions[0])
# dimensions[0] = 1

set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

# L'union des deux sets
a = set_a.union(set_b)
print(a)

# L'intersection des deux sets
b = set_a.intersection(set_b)
print(b)

# Les éléments de set_a qui ne sont pas dans set_b
c = set_a - b
print(c) 