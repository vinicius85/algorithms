def buildGraph():
	data = open("dijkstraData.txt","r")
	G = {}
	for line in data:
		i = 0
		src = 0
		weight = {}
		
		for s in line.split():
			if i == 0:
				src = s
			else:	
				tokens = s.split(',')
				weight.setdefault(int(tokens[0]),int(tokens[1]))
			i+=1	
		
		G.setdefault(int(src),[]).append(weight)
	return G
	
	
def dijkstra(G,s,v):
	
	A = {}
	A.setdefault(s,0)
	
	X = set()
	X .add(s)
	V = G.keys()
	V.remove(s)
	
	while X != V:
			
	
	

def main():
		
	print "[dijkstra] - processing file...\n"
	G = buildGraph()
	
	print "[dijkstra] - building model...\n"

	V = [7,37,59,82,99,115,133,165,188,197]
	D = []
	for v in V:
		dist = dijkstra(G,1,v)
		D.append(dist)
	
	print '[dijkstra] '+str(D)
	
if __name__ == "__main__": main()