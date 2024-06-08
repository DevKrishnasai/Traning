# from collections import defaultdict
# def val():
#     return 0

# d = "polikujmnhytgbvfredcxswqaz"
# s = input()
# l = [" "]*len(d)

# dic  = defaultdict(val)

# for i in s:
#     dic[i]+=1
#     index = d.index(i)
#     l[index]=i

# s1 = ""
# for i in l:
#     if i!=" ":
#         s1+=i*dic[i]

# print(s1)

d = "polikujmnhytgbvfredcxswqaz"
s = input()
s1 = ""

for i in d:
    if i in s:
        s1+=i*s.count(i)

print(s1)
