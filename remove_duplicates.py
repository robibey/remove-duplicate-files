import os

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
    source_files_list = []
    for src_path, src_dirs, src_files in os.walk(source):
        for src_file in src_files:
            source_files_list.append(os.path.join(src_path, src_file))

# Walk the destination and sub-folders, append path and filename to a list
    dest_files_list = []
    for dest_path, dest_dirs, dest_files in os.walk(dest):
        for dest_file in dest_files:
            dest_files_list.append(os.path.join(dest_path, dest_file))

    for x in source_files_list:
        print(x.split('\\')[-1])
#TODO - just compare filenames in the list and return them if they match.
#TODO - could also compare other things such as modified time but this is mainly to find
# duplicate images.

user_input()