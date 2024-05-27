
password = input()
lower = upper = spl = digit= 0


n = len(password)


for char in password:
    if char.isdigit():
        digit=1
    elif char.islower():
        lower=1
    elif char.isupper():
        upper=1
    else:
        spl=1


if n >= 8:
    if lower and upper and digit and spl:
        print(-1)
    else:
        print(4 -lower-upper-digit-spl)
else:
    print(max(8-n,4 - lower-upper-digit-spl))
