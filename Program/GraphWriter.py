"""
SCGS.py
Source Code Genome Sequencing
"""
__author__ = "David Sawyer, Chris Campbell, Kevin Alverez"
__version__ = "3/29/2017"
''' This Program takes a JSON file called tokens.json and outputs a
bruijn graph containing the token data.
'''
import os
from  SubmissionGraph import Info

'''Translates the tuple to a string for .dot file '''
def tupleToStr(s):
    s = "\""+str(s)+"\""
    return s

def main(tokens_file_path, fileType):
    """
    main -Main method for script SCGS. Writes graph files into a DOT, CSV, or Spreadsheat file.
    :param tokens_file_path:
    :return:
    """
    #getting file to place output file.
    graph_file_path = os.path.join(working_dir, '../Visuals/graph')
    fileType = fileType.split(" ")
    info = Info(tokens_file_path) #Making an instance of the Info class in the  SubmissionGraph module
    graph = info.graph() # getting the graph from the  Info class
    #writing an output file based on user input 
    for i in  fileType: 
     if(i == "dot"):
         dotOutPutter(graph, graph_file_path)
     if(i == "csv"):
         csvOutPutter(graph, graph_file_path)
     if(i == "spreadsheet"):
        spreadsheetOutPutter(graph, graph_file_path)
#outputs dot file
def dotOutPutter(graph, graph_file_path):
    with open(graph_file_path+".dot", 'w') as f: 
        # Begining of .dot file 
        f.write("digraph {\n") 
        #Iterating through each key in the dictionary representing the graph
        for g in graph:
            #creating string for node id
            gString = tupleToStr(g)
            #Iterating through each dictionary key that  is contained in the dictionary that is linked to the 'g' key.
            for i in graph[g]:
                #turning second dictionary key into a string for a graph id
                 iString = tupleToStr(i)
                 weight = 0
                 #iterating through the list linked to the  'i' key  adding the weight up,
                 for j in graph[g][i]:
                     weight += j[2]
                 weight = str(weight)
                 #Printing the edge information to the dot file.
                 f.write( gString +"-> " + iString +"[weight = " + weight+"];\n")
        f.write("}")
    f.close()
    print(".dot file written to /Visuals/graph.dot\n")
#outputs csv file
def csvOutPutter(graph, graph_file_path):
    with open(graph_file_path+".csv", 'w') as f: 
        # Begining of .csv file 
        for g in graph:
            #creating string for node id
            gString = tupleToStr(g)
             #Iterating through each dictionary key that  is contained in the dictionary that is linked to the 'g' key.
            for i in graph[g]:
                 #turning second dictionary key into a string for a graph id
                 iString = tupleToStr(i)
                 weight = 0
                 #iterating through the list linked to the  'i' key  and for printing n rows where n is equal to the weight.
                 for j in graph[g][i]:
                     weight = j[2]
                     for w in range(weight):
                        f.write( gString +"," + iString +"\n")
    f.close()
    print(".csv file written to /Visuals/graph.csv\n")
#outputs a spreadsheat file 
def spreadsheetOutPutter(graph, graph_file_path):
    with open(graph_file_path+"Spread.csv", 'w') as f: 
        # Begining of .csv file  that is customized so Gephi reads it as a spreadsheet file
          f.write("Id; Source; Target; Weight\n") 
          for g in graph:
              #creating string for node id
              gString = tupleToStr(g)
               #Iterating through each dictionary key that  is contained in the dictionary that is linked to the 'g' key.
              for i in graph[g]:
                    #turning second dictionary key into a string for a graph id
                   iString = tupleToStr(i)
                   weight = 0
                   #iterating through the list linked to the  'i' key  and for printing n rows where n is equal to the weight.
                   for j in graph[g][i]:
                        weight += j[2]
                   weight = str(weight)
                   #Printing the edge information to the dot file.
                   f.write( gString +";"+ gString +";" + iString +"; " + weight+"\n")
    f.close()
    print("spreadsheet file written to /Visuals/graphSpread.csv\n")

if __name__ == "__main__":
    working_dir = os.path.dirname(__file__)
    json_tokens_file_path = os.path.join(working_dir, "../Data/tokens.json")
    tokens_file_path=json_tokens_file_path
    #getting user input for what type of file they want. 
    fileType = input("\nWhat file type(s) would you like to be printed?\n(Enter each option separated by a space)\nOptions: \ndot\ncsv\nspreadsheet\n")
    print(fileType)
    main(json_tokens_file_path , fileType)
