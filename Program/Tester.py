import networkx as nx
import json
from LastKmer import EndNodes
from SubmissionGraph import Info

json_path = '../Data/tokens.json'
with open(json_path, 'r') as fp:
	data = json.load(fp)

lastkmer = EndNodes(json_path)
lastkmerSize = lastkmer.size()
kmerSet=  lastkmer.endKmers()

info =  Info(json_path)
graph = info.graph()
end = info.end
'''
CHECKING IF NUMBER OF END NODES MATCH
'''
endList = []
for g in graph:
    for i in graph[g]:
        if( i == end):
            endList.append(g)

endListLen = len(endList)
endSet = set(endList)
endSetLen = len(endSet)

if(endListLen == lastkmerSize):
    print('PASSED: Nodes Numbers Match')

else:
    print('FAILED: Not a match')
    print(endList)
    print(kmerSet)
'''
CHECKING IF ENDING NODES MATCH
'''
if(len(kmerSet - endSet) == 0):
    print('PASSED: The last tokens match')
else:
    print('Diff:')
    print(kmerSet - endSet)