import sys

a = 9.5

print(f"{a!r}",)
print(sys.getrefcount(a)) # ob_refcnt
print(type(a)) # ob_type
print(a) # ob_fval
print(id(a)) # the object's address