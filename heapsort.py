#Heapsort Algorithm (Chapter 6)

#max_heapify loop: O(lg n)
#build_max_heap loop: O(n)
#heapsort upper limit: O(n lg n)

#max_heap: structure where root is always greater than its leaves.

#i.e.: priority queues

A = [11,4,1,5,3,2,16,9,10,14,13,8,7]

def max_heapify(A,i):
	l = (2*i)+1
	r = (2*i)+2
	if(l<len(A) and A[l] > A[i]):
		maior = l
	else:
		maior = i
	if(r<len(A) and A[r] > A[maior]):
		maior = r
	if(maior != i):
		tmp =A[i]
		A[i] = A[maior]
		A[maior] = tmp		
		max_heapify(A,maior)
	 
def build_max_heap(A):
	for i in xrange( ((len(A)/2) -1),-1 ,-1):
		max_heapify(A,i)

def heapsort(A):
	print('[heapsort] input: '+str(A))
	
	build_max_heap(A)
	
	print('[heapsort] build_max_heap: '+str(A)) 
	
	B = []
	for i in xrange(len(A)-1,0,-1):
		tmp = A[0]
		A[0] = A[i]
		A[i] = tmp
		
		B.insert(0,A[i])
		
		A = A[0:len(A)-1]
		max_heapify(A,0)
		print('[heapsort] max_heapify: '+str(A))
	B.insert(0,A[0])
	return B

def main():
	B = heapsort(A)
	print('[heapsort] output:' +str(B))
	
if __name__ == "__main__": main()