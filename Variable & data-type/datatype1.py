#int, float, str, list, tuple, set, dict
x=10
print(type(x))
y=3.14
print(type(y))
z='5'
print(type(z))
a=[10,20,30,40]
print(a)
b=(10,20,30,40)
print(type(b))
print(b)
c={10,20,30,10}
print(type(c)) # set -> it does not allow the duplicate elements 
print(c)
d={
    'name':'Gairik Sharma',
    'age':18,
    'email': 'gairik@gmail.com'
}
print(type(d))
print(d)
print(d.keys())
print(d.values())