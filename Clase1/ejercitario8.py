a = True; b = True
x = (a and (not b)) or ((not a) and b) or (a and b)
print(x)

a = True; b = False
x = (a and (not b)) or ((not a) and b) or (a and b)
print(x)

a = False; b = True
x = (a and (not b)) or ((not a) and b) or (a and b)
print(x)

a = False; b = False
x = (a and (not b)) or ((not a) and b) or (a and b)
print(x)