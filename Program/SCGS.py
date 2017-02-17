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
    print("loaded")

if __name__ == "__main__":
    working_dir = os.path.dirname(__file__)
    json_tokens_file_path = os.path.join(working_dir, "..\\Data\\tokens.json")
    main(tokens_file_path=json_tokens_file_path)


