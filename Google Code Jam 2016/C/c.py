import math

def isPrime(num):
	'''Checks if a number is prime'''
	if num == 2:
		return True
	if num%2 == 0 or num<=1:
		return False
	for i in range(3, int(math.sqrt(num))+1, 2):
		if num%i == 0:
			return False
	return True

def convertBase(num, base):
	'''Converts and returns num in specified base'''
	res = 0
	bits = list(str(num))
	for i in range(len(bits)):
		if bits[i] == '1':
			res += base**(len(bits)-1-i)
	return res

def toBinary(num):
	res = ''
	while num >= 2:
		res = str(num%2) + res
		num = num//2
	if num == 1:
		return int('1' + res)
	else:
		return int(res)

def checkJamCoin(num):
	'''Does everthing'''
	if num%10 == 0:
		return False

	string = ''
	for base in range(10,1,-1):
		converted = convertBase(num,base)
		if isPrime(converted):
			return False
		else:
			string = str(divisor(converted)) + ' ' + string
	return str(num) + ' ' + string + '\n'

def divisor(num):
	'''Returns a divisor'''
	for i in range(2, num):
		if num%i == 0:
			return i

with open('C-large-practice.in','r') as fin:
	with open('output.out','w') as fout:
		line = fin.readlines()[1].split()
		N = int(line[0]) # length of a Jam Coin
		J = int(line[1]) # J number of Jam Coins
		fout.write('Case #1:\n')

		count = 0
		start = 2**(N-1) # Base 10 (decimal)

		while count < J:
			result = checkJamCoin(toBinary(start))
			if result:
				count += 1
				# print (count)
				fout.write(result)
			start += 1