"""
SCGS.py
Source Code Genome Sequencing
"""
__author__ = "Chris Campell"
__version__ = "2/17/2017"

import os
import json
import networkx as nx

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
            #Graph instantiation?
            if(token_hash in graph):
                if(token_hash2 in graph[token_hash]):
                    k = None
                    for z in graph[token_hash][token_hash2]:
                        if(z[0] == sub_index):
                            k = z
                        if(k != None):
                            print k
                            nk = k[1] + 1
                            graph[token_hash][token_hash2].remove(k)
                            graph[token_hash][token_hash2].append((k[0], nk, 'k'))
                            print k[1] + 1
                        else:
                            graph[token_hash][token_hash2].append((sub_index, 1, 'k'))

            else:
                graph.setdefault(token_hash, {}).setdefault(token_hash2, [(sub_index, 1)])
    '''Build Graph Representation'''
    # Iterate over every submission and pull out kmers
    print("loaded")
    for i in graph:
        for j in i:
            print i
if __name__ == "__main__":
    working_dir = os.path.dirname(__file__)
    json_tokens_file_path = os.path.join(working_dir, "../Data/tokens.json")
    main(tokens_file_path=json_tokens_file_path)
