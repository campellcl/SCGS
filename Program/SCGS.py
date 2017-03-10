"""
SCGS.py
Source Code Genome Sequencing
"""
__author__ = "Chris Campell"
__version__ = "2/17/2017"

import os
import json
import networkx as nx

def tupleToStr(s):
    s = str(s)
    s = ''.join(s.split(","))
    s = ''.join(s.split(" "))
    s = s[1 : len(s) - 1]
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
        # Iterate through all tokens in the given submission in groups of 9
        for i in range(len(submission) - (kmer - 1)):
            # Create the hash entry key with the submission index and the token sequence:
            token_hash = tuple(submission[i:i+kmer])
            token_hash2 = tuple(submission[i + 1: i + 1 + kmer])
            # Append the token hash tuple as an immutable key if it doesn't already exist.
            token_hashes.setdefault(token_hash, []).append((sub_index, i))
            #Adding elements to the graph
            if(token_hash in graph): #checking for kmer hash
                if(token_hash2 in graph[token_hash]): #checking for right kmer
                    k = None
                    #finding the tuple to update the amount of times it was used
                    for z in graph[token_hash][token_hash2]:
                        if(z[0] == sub_index): #if the index is found set k to the tuple
                            nk = z[2] + 1
                            graph[token_hash][token_hash2].append((z[0], z[1], nk))  # append the tuple with updated number of uses
                            graph[token_hash][token_hash2].remove(z) #remove the tuple
                            break
            else:
                graph.setdefault(token_hash, {}).setdefault(token_hash2, [(sub_index, i, 1)])
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
                f.write( gString + " -> " + iString + " [ label = \" " + str(g) + " \" ];\n") 
        f.write("\n\n}")
    f.close()

if __name__ == "__main__":
    working_dir = os.path.dirname(__file__)
    json_tokens_file_path = os.path.join(working_dir, "../Data/tokens.json")
    main(tokens_file_path=json_tokens_file_path)
