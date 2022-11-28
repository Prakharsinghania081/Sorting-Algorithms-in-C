import random

#==================================================
def partitionBetter(L, start, stop):
	pivot = L[start]
	wall  = start

	for scout in range(start+1, stop+1):
		if L[scout] < pivot:
			wall = wall + 1
			L[wall], L[scout] = L[scout], L[wall]
	#LOOP ENDS HERE

	L[wall], L[start] = L[start], L[wall]
	return wall # returning to us the index/position of the pivot

int partition() {
	int L, start, stop, pivot, wall;
	pivot = L[start]
	wall = start
	
	int scout; 
	for (scout = start+1; scout< stop+1; scout = scout+1) {}

}

#==================================================
# take list L, sort everything between positions start and stop (inclusive)
def quickSort(L, start, stop):

	# protection against stupidity 
	# helps us stop in edge cases
	if stop <= start:
		return

	p = partitionBetter(L, start, stop)
	quickSort(L, start, p-1)  # sort the "lesser" list
	quickSort(L, p+1,   stop) # sort the "greater" list


#==================================================
def blah():
	# create a shuffled list of length n, starting from 100
	X = [23,43,21,1,2,4,23,11,15] 

	quickSort(X, 0, len(X)-1)
	print(X)
	

blah()

