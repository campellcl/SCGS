import os
import json
class EndNodes:

    def __init__(self, tokens_file_path):
    
        self.endKmers =  self.grabKmers(tokens_file_path)
    
    def grabKmers(self, tokens_file_path):
        with open(tokens_file_path, 'r') as fp:
            data = json.load(fp=fp)
            lastKmer = []
            l = []
        #itereating through the submissions and grabing the last Kmer
        for sub_index, submission in enumerate(data):
        	#Getting token data from json file
            tokens = submission['tokens']
            #Creating a tuple for the last kmer
            finalNode = tuple(tokens[len(tokens) - 9 : len(tokens)])
            lastKmer.append(finalNode)
            #creating a set of end Kmers so that we can 
            #delete duplicates
            l.append(finalNode)
        endTokenTuple = set(l)
        length = len(endTokenTuple)
        info = {'tokens' : lastKmer, 'size' : length}
        return info
    #Getter for amount of end tokens
    def size(self):
        return self.endKmers['size']
    #Getter for end tokens
    def endTKmers(self):
    	return self.endKmers['tokens']