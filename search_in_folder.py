# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:27:13 2024

@author: marku
"""


import os
 
def list_files_recursive(path='.'):
    path_list = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        else:
            path_list.append(full_path)
        
        return(path_list)
 
# Specify the directory path you want to start from
directory_path = './'
path_list = list_files_recursive(directory_path)

with open('config.toml') as f:
    # Read the contents of the file into a variable
    names = f.read()

    # Print the names
    print(names)