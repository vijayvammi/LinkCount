from __future__ import division
import numpy as np
from operator import mul

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(mul, xrange(n, n-r, -1))
    denom = reduce(mul, xrange(1, r+1))
    return numer//denom

def computeM(N):
	M = {}
	# for every number, this dictionary holds the list of 
	# number of sub-chains of length 1, 2, 3 ...
	for i in range(N):
		M[i] = np.zeros(N)
		#base cases
		if i == 0:
			M[i][0] = 1 # one sub-chain of length 1
			continue
		if i == 1:
			M[i][0] = 2 # two sub-chains of length 1
			continue
		# The number of subchains in all permutations having 
		# 1 and N as the last number is solved directly
		# by the previous comptuatoin.	
		M[i] = 2*M[i-1]
		# the number of sub-chains for all the permutations having
		# the last number as one of the inbetween numbers
		# could be run only half the number of times because of symmetric
		# property!!!
		for j in range(1, i):
			leftCount = len(range(0,j))
			rightCount = len(range(j,i))
			totalCount = leftCount + rightCount
			numComb = ncr(totalCount, leftCount)
			adds = np.zeros(N)	
			for k in range(N):
				rightIncrement = M[rightCount-1][k]
				adds[k:] += numComb*rightIncrement*M[leftCount-1][:N-k]
			M[i][1:] += adds[:-1]		
	
	#mean and std computations
	counts = M[N-1]
	total = (counts*np.arange(1,N+1)).sum()
	numPerms = counts.sum()	
	average = total/numPerms
	std = np.sqrt(1/numPerms*((np.arange(1, N+1)-average)**2*counts).sum())
	print 'total: ' + str(total) + '     ' + str(average) + '   std: ' + str(std)
