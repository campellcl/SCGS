import json
from LastKmer import EndNodes
from SubmissionGraph import Info
from io import BufferedReader
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

''' Misc  ''' 
t = (1, 14, 25)
l = [1, 14, 25]
print(t[0:4])
print(l[-1])

record = info.data[0]
record = record['tokens']
lastKmerRecord = record[len(record )- 9: len(record)]
print(record)
print(record[len(record)  : len(record) + 1])
print("****")
weightL = 3
for w in range(weightL):
    weight = str(1) 
    print(weight)
# for i in range(len(record) - (9 )):
#     # Create the hash entry key with the submission index and the token sequence:
#     token_hash = tuple(record[i : i + 9])
#     token_hash2 = tuple(record[i + 1: i + 1 + 9])
#     token_hash = str(token_hash)
#     token_hash2 = str(token_hash2)
#     print(token_hash + ": : " +token_hash2 + "\n")
# print(record[len(record) - 9 : len(record) - 1])
# print(record[0])


# print(len(record))
# print(record[0:132])

# for g in graph:
#     #creating string for node id
#     for i in graph[g]:
#         for j in graph[g][i]:
#             print(j)

