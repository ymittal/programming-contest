problem = input()
arr = []

while problem != "0 0 0 0":
    arr.append(problem)
    problem = input()

for problem in arr:
    vars = problem.split(" ")
    Z = int(vars[0])
    I = int(vars[1])
    M = int(vars[2])
    L = int(vars[3])
    vals = []
    while not(L in vals):
        vals.append(L)
        L = (Z*L+I)%M
    vals = vals[0:-1]
    print (len(vals) - vals.index(L) + 1)
