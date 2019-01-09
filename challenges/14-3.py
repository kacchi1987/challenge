class Dammy:
    pass

def Exact(a, b):
    if a is b:
        return True
    else:
        return False

a = Dammy()
b = a
c = Dammy()

print(Exact(a,b))
print(Exact(a,c))
