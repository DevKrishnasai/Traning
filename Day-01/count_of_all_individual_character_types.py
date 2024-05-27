s = input()
d = {
    "lv":0,
    "uv":0,
    "sp":0,
    "lc":0,
    "uc":0,
    "d":0
}
for i in s:
    if i.isdigit():
        d["d"]+=1
    elif i.lower():
        if i in ["a","e","i","o","u"]:
            d["lv"]+=1
        else:
            d["lv"]+=1
    elif i.upper():
        if i in ["A","E","I","O","U"]:
            d["uv"]+=1

        else:
            d["cv"]+=1
    else:
        d["sp"]+=1
print(d)

