#binary search tree (chapter 12)
#complete tree ops: O(h) - search, min, max , pre, pos, insert, delete
#linear tree: O(n) - worst case

#TODO change representation to tree object

A = [5,3,7,2,5,None,8]

def inorder_tree_walk(A,i):
	if i<len(A) and A[i] is not None:
		inorder_tree_walk(A,2*i+1)
		print(A[i])
		inorder_tree_walk(A,2*i+2)

def tree_search(i,k):
	if A[i] is None or k == A[i]:
		return i
	if k < A[i]:
		return tree_search(2*i+1,k)
	else:
		return tree_search(2*i+2,k)
		
def main():
	inorder_tree_walk(A,0)
	print(tree_search(0,5))
	
if __name__ == "__main__": main()