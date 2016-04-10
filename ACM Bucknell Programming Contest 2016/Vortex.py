strings = []
lengths = []
lengths2=[]
finals = []

while True:
    n = input()
    if(n.strip()=='0'):
        break

    strings.append(n.strip())
    lengths2.append(n.strip().replace('-',''))
    nums = []
    for x in range( len(n)):
        try:
            if(n[x] == 'X' ): # and x == (len(n)-1)
                nums.append(10)
            else:
                nums.append(int(n[x]))
        except Exception:
            pass

    lengths.append(len(nums))
    sum1 = 0
    nums2 = []
    sum2 = 0

    for val in nums:
        sum1 += val
        nums2.append(sum1)
    for val in nums2:
        sum2 += val
    finals.append(sum2)

for x in range(len(finals)):
    if(lengths[x]!= 10 or finals[x]%11 != 0 or len(lengths2[x]) != 10):
        print (strings[x] + ' is incorrect.')
    elif(finals[x]%11 == 0 and len(lengths2[x]) == lengths[x]):
        print (strings[x] + " is correct.")
    

        
            
