"""
SCGS.py
Source Code Genome Sequencing
"""
__author__ = "David Sawyer, Chris Campbell, Kevin Alverez"
__version__ = "3/23/2017"
'''Checking to see how many different ennding tokens there are in the 
submission data and storing for the shortest path algorithm'''
import os
from  SubmissionGraph import Info
'''Translates the tuple to a string for .dot file '''
def tupleToStr(s):
    s = "\""+str(s)+"\""
    return s

def main(tokens_file_path):
    """
    main -Main method for script SCGS. Writes graph files into a DOT file.
    :param tokens_file_path:
    :return:
    """
    info = Info(tokens_file_path) #Making an instance of the graphizer module
    graph = info.graph() # getting the graph from Info module
    
    #Writing dot file to  graph.dot
    with open(graph_file_path, 'w') as f: 
        # Begining of .dot file  
        f.write("digraph G {\n\n")
        for g in graph:
            
            #creating string for node id
            gString = tupleToStr(g)
            iString = None
            for i in graph[g].keys():
                if(iString == None):
                    iString = tupleToStr(i)
                iString = iString + " " + tupleToStr(i)
            f.write(  gString + "  ->  {" + iString +"};\n") 
        f.write("}")
    f.close()

if __name__ == "__main__":
    working_dir = os.path.dirname(__file__)
    graph_file_path = os.path.join(working_dir, '../Visuals/graph.dot')
    json_tokens_file_path = os.path.join(working_dir, "../Data/tokens.json")
    main(tokens_file_path=json_tokens_file_path)
