num = int(input())
arr = []

for i in range(num):
    arr.append(input())

for problem in arr:
    if "+" in problem:
        operator = "+"
    else:
        operator = "-"

    num1 = problem.split(operator)[0]
    num2 = problem.split(operator)[1]
    val = str(eval(problem))
    bigLen = max(len(num1), len(num2)+1, len(val))
    print(" "*(bigLen-len(num1))+num1)
    print(" "*(bigLen-len(num2)-1)+operator+num2)
    print("-"*bigLen)
    print(" "*(bigLen-len(val))+val)
    print()