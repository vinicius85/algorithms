import collections
import sys
import resource
from itertools import groupby

t = 0
s = 0
explored = set()
sorted_nodes = set()
leaders = {}
fin_times = {}

def scc(G,G_rev):
	global sorted_nodes
	
	print "[scc] - DFS 1st step...\n"
	dfs_loop(G_rev, '1st')
	
	sorted_nodes = sorted(fin_times, key=fin_times.get, reverse=True)
	
	print "[scc] - DFS 2nd step...\n"
	dfs_loop(G, '2nd')
	
	print "[scc] - Grouping SCCs...\n"
	out = collections.defaultdict(list)
	sizes = []
	for lead, vertex in groupby(sorted(leaders, key=leaders.get),key=leaders.get):
		out[lead] = list(vertex)
		sizes.append(len(out[lead]))
	return out,sizes
	
def dfs_loop(G,num_pass):
	
	global s
	global explored
	
	explored = set()
	
	if (num_pass == '1st'):
		for i in range(len(G.keys()),0,-1):
			if i not in explored:
				dfs(G,i,'1st')
	else:
		for i in sorted_nodes:
			if i not in explored:
				s = i
				dfs(G,i,'2nd')

def dfs(G,i,num_pass):
	
	global t
	global s
	global leaders
	global fin_times
	
	explored.add(i)
	
	if num_pass == '2nd':
		leaders[i] = s
	
	edges = G.get(i)
	for j in edges:
		if j not in explored:
			dfs(G,j,num_pass)
	t=t+1
	fin_times[i] = t
			
def buildGraph():
	data = open("SCC.txt","r")
	G = {}
	G_rev = {}
	for line in data:
		lst = [int(s) for s in line.split()]

		G.setdefault(lst[0],[]).append(lst[1])
		G_rev.setdefault(lst[1],[]).append(lst[0])
	
	maxVertex = max(G.keys())
	for i in range(1, maxVertex+1):
		if i not in G:
			G[i] = []
		if i not in G_rev:
			G_rev[i] = []
	
	return G,G_rev
	

def main():
	
	sys.setrecursionlimit(10 ** 6)
	resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))
	
	print "[scc] - processing file...\n"
	G,G_rev = buildGraph()
	
	print "[scc] - number of nodes = "+str(len(G.keys()))
	print "[scc] - building model...\n"
	
	sccs,sizes = scc(G,G_rev)
	
	print "[scc] - Reverse sorting SCCs...\n"
	
	sizes.sort(reverse=True)
	
	print "[scc] - Top 5 sccs = "+str(sizes[:5])

	
if __name__ == "__main__": main()