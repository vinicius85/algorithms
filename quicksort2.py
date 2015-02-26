comparison = 0

def quicksort(A,p,n):	
	global comparison
	if p<n:
		#print 'A='+str(A)
		
		choosePivot(A,p,n)
		part = partition(A,p,n)	
		comparison += (n-p-1)			
				
		quicksort(A,p,part)
		quicksort(A,part+1,n)

def choosePivot(A,p,n):	
	#A[p],A[n-1] = A[n-1],A[p]
	#A[p] = A[p]
	f = A[p]
	index = (p+n-1)/2
	m = A[index]
	l = A[n-1]
	s = sorted([f,m,l])[1]        
	if   s == m:
		A[p],A[index]=A[index],A[p]
	elif s == l:
		A[p],A[n-1] = A[n-1],A[p]

def partition(A,l,r):	
	p = A[l]
	i = l+1
	for j in range(l+1,r):
		if A[j] < p:
			A[j],A[i] = A[i],A[j]			
			i += 1		
	A[l],A[i-1] = A[i-1],A[l]
	return i-1
	

def main():
	print "[quicksort] - processing file...\n"

	input = lines = [int(line.strip()) for line in open('quicksort.txt')]
	#input = [3,9,8,4,6,10,2,5,7,1]
	print('[quicksort] length:' +str(len(input)))		
	quicksort(input, 0, len(input))
	print('[quicksort] output:' +str(input))
	print('[quicksort] comparisons:' +str(comparison))
	
if __name__ == "__main__": main()
