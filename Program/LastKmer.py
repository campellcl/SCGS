import os
import json
class EndNodes:

    def __init__(self, tokens_file_path):
    
        self.lastkmers =  self.grabKmers(tokens_file_path)
    
    def grabKmers(self, tokens_file_path):
        with open(tokens_file_path, 'r') as fp:
            data = json.load(fp=fp)
            lastkmers = []
            l = []
        #itereating through the submissions and grabing the last Kmer
        for sub_index, submission in enumerate(data):
        	#Getting token data from json file
            tokens = submission['tokens']
            #Creating a tuple for the last kmer
            finalNode = tuple(tokens[len(tokens) - 9 : len(tokens)])
            lastkmers.append(finalNode)
            l.append(finalNode)
            endSet = set(l)
        length = len(endSet)
        info = {'tokens' : endSet, 'size' : length}
        return info
    
    #Getter for amount of end tokens
    def size(self):
        return self.lastkmers['size']
    #Getter for end tokens
    def endKmers(self):
    	return self.lastkmers['tokens']