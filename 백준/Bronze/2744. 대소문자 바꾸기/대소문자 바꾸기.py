import sys
sysinput = sys.stdin.readline

a = sysinput().rstrip()
b = ""
for c in a:
    if c.isupper():
        b+=c.lower()
    else:
        b+=c.upper()
print(b)