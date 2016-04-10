all_sets = []
office_num=0

while True:
    office_num += 1
    curr_set = input().split()
    n = int(curr_set[0])
    m = int(curr_set[1])
    c = int(curr_set[2])
    if(n==0 and m==0 and c ==0):
        break

    brks=[]
    brks_state = []
    bool_broken = False
    cur_cons=0
    max_cons=0
    for i in range(n):
        brks.append(int(input()))
    brks_state = [0]*len(brks)

    for i in range(m):
        brk_changed = int(input())-1
        brks_state[brk_changed]=(brks_state[brk_changed]+1)%2
        if(brks_state[brk_changed]==1):
            cur_cons += brks[brk_changed]
        else:
            cur_cons -= brks[brk_changed]
        if(cur_cons>c):
            bool_broken = True
        if(cur_cons>max_cons):
            max_cons = cur_cons
    all_sets.append([office_num, bool_broken, max_cons])

for set1 in all_sets:
    print("Office " + str(set1[0]))
    if(set1[1]):
        print("Fuse was blown.")
    else:
        print("Fuse was not blown.")
        print("Maximal power consumption was " + str(set1[2]) + " amperes.")