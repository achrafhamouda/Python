from functools import reduce
nombres = [12,45,67,34,89,23,10,5,76]
a = list(filter(lambda x : x % 2 == 0, nombres))
print(a)

b = list(map(lambda y : y**2,a))
print(b)

c = reduce(lambda x,y : x+y ,a)
print(c)

etudiants = [("Sara",17),("Ahmed",12),("Mohamed",19),("Meriam",14)]
n = list(filter(lambda m : m[1] >= 15, etudiants))
print(n)


v = list(map(lambda j :j[0],n))
print(v)