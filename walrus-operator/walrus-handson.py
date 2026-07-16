x = 'ABC'
# codes = [ord(y) for y in x]

# print(y) => Error

codes = [last:= ord(c) for c in x]
print(last)
print(codes)