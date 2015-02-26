#input = [1,3,5,2,4,6]
#input = [1,5,3,2,4]
#input = [1,6,3,2,4,5]
#input = [ 9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0 ]
#input = [ 37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45 ]
#input = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54 ]

def count(A,n):
	#print 'A='+str(A)
	if n==1: return (A,0)
	else:
		(B,x) = count( A[0:n/2] , len(A[0:n/2]) )
		
		(C,y) = count( A[n/2:n] , len(A[n/2:n]) )
		
		(D,z) = countSplitInv( B, C , n )
	return D,(x+y+z)
	
def countSplitInv(B, C , n):
	D = []
	i = 0
	j = 0
	inv = 0
	for k in range(0,n):
		
		if i == len(B) and j < len(C):
			D.insert(k,C[j])
			j = j+1
			continue
		if j == len(C) and i < len(B):
			D.insert(k,B[i])
			i = i+1
			continue
		if j == len(C) and i == len(B) :
			break
			
		if  B[i] < C[j] :
			D.insert(k,B[i])
			i = i+1
		elif C[j] < B[i]:
			D.insert(k,C[j])
			j = j + 1
			inv = inv + len(B)-i
	return D,inv
	
def main():
	
	print "[inversions] - processing file...\n"
	input = lines = [int(line.strip()) for line in open('IntegerArray.txt')]
	
	print "[inversions] - done!"
	print "[inversions] - counting..."
	
	value = count(input, len(input))
	print('[inversions] output:' +str(value))
	
if __name__ == "__main__": main()