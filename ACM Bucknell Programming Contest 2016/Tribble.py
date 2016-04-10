from itertools import *
arr = []
num = int(input())

for i in range(num):
    arr.append(input())

for startword in arr:
    chars = [c for c in startword]
    perms = []
    for perm in permutations(chars):
        word = ''
        for char in perm:
            word += char
        perms.append(word)
    perms.sort()
    perms = [perms[0]] + [perms[j] for j in range(1,len(perms)) if perms[j]!=perms[j-1]]
    for word in perms:
        print(word)