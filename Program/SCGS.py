"""
SCGS.py
Source Code Genome Sequencing
"""
__author__ = "Chris Campell, David Sawyer"
__version__ = "3/18/2017"

import os
import json
import networkx as nx
'''Translates the tuple to a string for .dot file '''
def tupleToStr(s):
    s = "\""+str(s)+"\""
    return s

def main(tokens_file_path):
    """
    main -Main method for script SCGS. Reads source code tokens into memory.
    :param tokens_file_path:
    :return:
    """
    with open(tokens_file_path) as fp:
        data = json.load(fp=fp)
    token_hashes = {}
    graph = {}
    kmer = 9
    '''Build Hash Table'''
    # Iterate through every submission and retain its index.
    for sub_index, submission in enumerate(data):
        tokens = submission['tokens']
        # Iterate through all tokens in the given submission in groups of 9
        for i in range(len(tokens) - (kmer - 2)):
            # Create the hash entry key with the submission index and the token sequence:
            token_hash = tuple(tokens[i:i+kmer])
            token_hash2 = tuple(tokens[i + 1: i + 1 + kmer])
            ''' Append the token hash tuple as an immutable key if it doesn't already exist
             Every other time'''
            if(i%2 == 0):
                token_hashes.setdefault(token_hash, []).append((sub_index, i))
                token_hashes.setdefault(token_hash2, []).append((sub_index, i))
            #Adding elements to the graph
            if(token_hash in graph): #checking for kmer hash
                if(token_hash2 in graph[token_hash]): #checking for right kmer
                    k = None
                    # Was the new tuple inserted
                    insert = False;
                    #finding the tuple to update the amount of times it was used
                    for z in graph[token_hash][token_hash2]:
                        if(z[0] == sub_index): #if the index is found set k to the tuple
                            nk = z[2] + 1
                            graph[token_hash][token_hash2].append((z[0], z[1], nk))  # append the tuple with updated number of uses
                            graph[token_hash][token_hash2].remove(z) #remove the tuple
                            insert = True
                            break
                    #Checking for insertion
                    if(insert == False):
                        #Adding the tuple to the graph, because it was not inserted
                        graph[token_hash][token_hash2].append((sub_index, i, 1))
                else:
                    graph[token_hash][token_hash2] = [(sub_index, i, 1)]
            else:
                graph[token_hash] = {token_hash2 : [(sub_index, i, 1)]}
        fp.close()
    '''Build Graph Representation'''
    #Writing dot file to  graph.dot
    with open('graph.dot', 'w') as f: 
        # Begining of .dot file  
        f.write("digraph G {\n\n")
        for g in graph:
            #creating string for node id
            gString = tupleToStr(g)
            for i in graph[g].keys():
                iString = tupleToStr(i)
                f.write(  gString + "  ->  " + iString +";\n") 
        f.write("\n\n}")
    f.close()

if __name__ == "__main__":
    working_dir = os.path.dirname(__file__)
    json_tokens_file_path = os.path.join(working_dir, "../Data/tokens.json")
    main(tokens_file_path=json_tokens_file_path)
