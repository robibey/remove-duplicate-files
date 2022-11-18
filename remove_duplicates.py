import os
import time
from collections import defaultdict

def user_input():
    '''User facing part of the script to determine what function the user
        wishes to run.'''

    user_response = input('Press 1 to find duplicates in folders and all sub-folders. ')

# Getting the filepaths to compare and running the find_duplicates function
    if int(user_response) == 1:
        while True:
            source_fp = input('Please input a source directory: ')
            if not os.path.exists(source_fp):
                print(f'Filepath "{source_fp}" does not exist!')
                continue
            dest_fp = input('Please input a destination directory: ')
            if not os.path.exists(dest_fp):
                print(f'Filepath "{dest_fp}" does not exist!')
                continue
            break
        find_duplicates(source_fp, dest_fp)

    if int(user_response) == 2:
        pass

def find_duplicates(source, dest):
    '''Compares files in a root directory and walking through all
        sub-folders to find any duplicate names. This function will
        walk through all sub-folders of the source and destination
        filepaths.'''
    
# Walk the source and sub-folders, append path and filename to a list
    t1 = time.time()
    source_files_list = defaultdict(list)
    for src_path, src_dirs, src_files in os.walk(source):
        for src_file in src_files:
            source_files_list[src_file].append(os.path.join(src_path, src_file))
# Walk the destination and sub-folders, append path and filename to a list
    dest_files_list = defaultdict(list)
    for dest_path, dest_dirs, dest_files in os.walk(dest):
        for dest_file in dest_files:
            dest_files_list[dest_file].append(os.path.join(dest_path, dest_file))

# Iterate both lists, if dfile = sfile, append sfile to list
    for item in source_files_list.values():
        if len(item) > 1:
            print(f'It appears you have {len(item)} files with the name {item[0].split(chr(92))[-1]}, '
                'if these are not exact duplicates and just have the same name, please rename the files '
                f'to have unique names. Here are the locations of all the files: {str(item)[1:-1]}')
    #print(dest_files_list.keys() & source_files_list.keys())
#TODO - just compare filenames in the list and return them if they match.
#TODO - could also compare other things such as modified time but this is mainly to find
# duplicate images.

user_input()