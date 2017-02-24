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
            # Append the token hash tuple as an immutable key if it doesn't already exist.
            token_hashes.setdefault(token_hash, []).append((sub_index, i))
    '''Build Graph Representation'''
    # Iterate over every submission and pull out kmers
    for sub_index, submission in enumerate(data):
        pass
        # TODO: build graph and vertices.
    print("loaded")

if __name__ == "__main__":
    working_dir = os.path.dirname(__file__)
    json_tokens_file_path = os.path.join(working_dir, "..\\Data\\tokens.json")
    main(tokens_file_path=json_tokens_file_path)


