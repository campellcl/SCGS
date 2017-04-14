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

def main(tokens_file_path, fileType):
    """
    main -Main method for script SCGS. Writes graph files into a DOT file.
    :param tokens_file_path:
    :return:
    """
    graph_file_path = os.path.join(working_dir, '../Visuals/graph')
    fileType = fileType.split(" ")
    info = Info(tokens_file_path) #Making an instance of the graphizer module
    graph = info.graph() # getting the graph from Info module
    #Writing dot file to  graph.dot
    for i in  fileType: 
     if(i == "dot"):
         dotOutPutter(graph, graph_file_path)
     if(i == "csv"):
         csvOutPutter(graph, graph_file_path)
     if(i == "spreadsheet"):
        spreadsheetOutPutter(graph, graph_file_path)

def dotOutPutter(graph, graph_file_path):
    with open(graph_file_path+".dot", 'w') as f: 
        # Begining of .dot file 
        f.write("digraph {\n") 
        for g in graph:
            #creating string for node id
            gString = tupleToStr(g)
            for i in graph[g]:
                 iString = tupleToStr(i)
                 for k in graph[g][i]:
                    print(str(k))
                    weight = str(k[2])
                    f.write( gString +"-> " + iString +"[weight = "+weight+"];\n")
        f.write("}")
    f.close()
    print(".dot file written to /Visuals/graph.dot\n")

def csvOutPutter(graph, graph_file_path):
    with open(graph_file_path+".csv", 'w') as f: 
        # Begining of .dot file 
        for g in graph:
            #creating string for node id
            gString = tupleToStr(g)
           
            for i in graph[g].keys():
                iString = tupleToStr(i)
                weight = str(i[2])
                for i in weight:
                    f.write( gString +";" + iString+"\n") 
        f.write("}")
    f.close()
    print(".csv file written to /Visuals/graph.csv\n")

def spreadsheetOutPutter(graph, graph_file_path):
    with open(graph_file_path+"Spread.csv", 'w') as f: 
        # Begining of .dot file 
        f.write("Id; Source; Target; Weight\n") 
        for g in graph:
            #creating string for node id
            gString = tupleToStr(g)
           
            for i in graph[g].keys():
                iString = tupleToStr(i)
                weight = str(i[3])
                f.write( gString +";"+ gString +";" + iString+";"+ weight+"\n") 
        f.write("}")
    f.close()
    print("spreadsheet file written to /Visuals/graphSpread.csv\n")

if __name__ == "__main__":
    working_dir = os.path.dirname(__file__)
    json_tokens_file_path = os.path.join(working_dir, "../Data/tokens.json")
    tokens_file_path=json_tokens_file_path
    fileType = input("\nWhat file type(s) would you like to be printed?\n(Enter each option separated by a space)\nOptions: \ndot\ncsv\nspreadsheet\n")
    print(fileType)
    main(json_tokens_file_path , fileType)
