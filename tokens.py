import json
'''Ben Langmead De Bruijn Graph assembly (Keynote Slides)
	prints graph tp command line'''
def graphPrint(graph):
	for i in graph:
		print "----------"
		print i[0]
		print "----------"
		print "   ||     "
		print "   ||     "
		print "   ||     "
		print "----------"
		print i[1]
		print "---------"
		print "         "
		print "         "
		print "         "
		print "         "
#Splits the string into kme: x - string; j - kmer
def splitter(x, j):
	nodes = [] # A list of nodes of each k-mer
	sub = [] # temperary holding for the k-mer
	''' looping through the and adding each number into the 
		up to the kth element and then adds it to the node list
		as a separate node'''
	for i in x: 
		sub.append(i)
		if(len(sub) == j): # if j is the kth element 
			nodes.append(sub) #add it to the node list
			sub = sub[1:j] # clear sub/ add the second position
				           # in the list
	return nodes
'''constructs graph in the graph'''
def graphStruct(nodes):
	graph = []
	prev = nodes[0]
	for i in nodes:
		boo = False
		if(prev != i):
			for j in graph:
				if(j[0] == prev):
					idx = graph.index(j)
					j = graph.pop(idx)
					j = [prev,[j[1],i]]
					graph.append(j)
					boo = True
					break
		
		if(boo == False and prev != i):
			newNode = [prev, i]
			if(graph == None):
				graph = [newNode]
			else:
				graph.append(newNode)
		prev = i
	return graph

s = open('tokens.json', 'r')
tokenlist = json.load(s)  #translate json tokens to python lists
tokensubset = tokenlist # pulling a subset of the list of lists
kmer = int(input("Enter in an interger for splitting the data: "))
nodes = []
for t in tokensubset:
	nodes.append(splitter(t, kmer - 1)) # list of nodes created by current string
nList = nodes[0]
graph = graphStruct(nList)
print tokenlist[0]
#graphPrint(graph)

