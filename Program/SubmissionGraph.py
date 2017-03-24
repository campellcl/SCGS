"""
SubmissionGraph.py
Source Code Genome Sequencing
"""
__author__ = "Chris Campbell, David Sawyer, Kevin Alverez"
__version__ = "3/23/2017"

import os
import json

class Info:
    '''
    TODO:
                -  Shortest Path Algorithm 
                - Clean up grap
    '''

    '''
    NOTE: 
                At the end of each submission go ahead and have the last kmer point
                to the FinalToken
    '''
    def __init__(self, tokens_file_path):
        self.info = self.createGraph(tokens_file_path)
        self.start = tuple((-1, -1, -1, -1, -1, -1, -1, -1, -1))
        self.end =  tuple((-2, -2, -2, -2, -2, -2, -2, -2, -2))

    #Creating the graph and engrams from student tokens.
    def createGraph(self, tokens_file_path):
        with open(tokens_file_path) as fp:
            data = json.load(fp=fp)
        token_hashes = {}
        graph = {}
        kmer = 9
        start =  tuple((-1, -1, -1, -1, -1, -1, -1, -1, -1))
        end =  tuple((-2, -2, -2, -2, -2, -2, -2, -2, -2))
        '''Build Hash Table'''
        # Iterate through every submission and retain its index.
        for sub_index, submission in enumerate(data):
            tokens = submission['tokens']
            startkmer = tuple(tokens[0 : kmer ])
            lastkmer = tuple(tokens[(len(tokens) - kmer ) : len(tokens) ])
            #Adding start and end nodes to graph
            graph.setdefault(start, {}).setdefault(startkmer, []).append((sub_index))
            graph.setdefault(lastkmer, {}).setdefault(end, []).append((sub_index))
            
            # Iterate through all tokens in the given submission in groups of 9
            for i in range(len(tokens) - (kmer - 1)):
                # Create the hash entry key with the submission index and the token sequence:
                token_hash = tuple(tokens[i : i + kmer])
                token_hash2 = tuple(tokens[i + 1: i + 1 + kmer])
                ''' Append the token hash tuple as an immutable key if it doesn't already exist
                Every other time'''
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
         #Storing engram and graph into the info term to be returned as a dictionary           
        info = { 'graph' : graph , 'engram' : token_hashes}
        return info
    #Getter for graph
    def graph(self):
    	return self.info['graph']
    #Getter for engram
    def engram(self):
    	return self.info['engram']
    def start():
       return self.start
    def end():
        return self.end